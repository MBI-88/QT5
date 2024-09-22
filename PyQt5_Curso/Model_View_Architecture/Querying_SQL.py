"""
@autor: MBI
Description: Script for developmnet of Querying SQL

The process is the same for all databases — create the database object, set
the name and the open the database to initialize the connection. However, if
you want to connect to a remote database there are a few extra parameters.

Editing the database

Strategy                                Description
QSqlTableModel.OnFieldChange            Changes are applied automatically, when the user deselects the edited cell.
QSqlTableModel.OnRowChange              Changes are applied automatically, when the user selects a different row.
QSqlTableModel.OnManualSubmit           Changes are cached in the model, and written to the database only when
                                        .submitAll() is called, or discarded when revertAll() is called.

You can set the current edit strategy for the model by calling .setEditStrategy
on it. For example —  self.model.setEditStrategy(QSqlTableModel.OnRowChange)

Selecting columns

Often you will not want to display all the columns from a table. You can select
which columns to display by removing columns from the model. To do this
call .removeColumns() passing in the index of the first column to remove and
the number of subsequent columns

self.model.removeColumns(2, 5)

Once removed the columns will no longer be shown on the table. You can
use the same name-lookup approach used for column labelling to remove
columns by name

columns_to_remove = ['name', 'something']
for cn in columns_to_remove:
    idx = self.model.fieldIndex(n)
    self.model.removeColumns(idx, 1)


Filtering a table

Pattern               Description
field="{}"            Field matches the string exactly.
field LIKE "{}%"      Field begins with the given string.
field LIKE "%{}"      Field ends with the given string.
field LIKE "%{}%"     Field contains the given string.



Displaying related data with

Relationships in relational databases are handled through foreign keys. These
are a (usually) numeric value, stored in a column of one table, which
references the primary key for a row in another table.
An example of a foreign key in our example tracks table would be album_id or
genre_id. Both are numeric values which point to records in the album and
genre table respectively. Displaying these values to the user (1, 2, 3.. etc.) is not 
helpful because they have no meaning themselves.


The QSqlRelation object accepts three arguments, first the related table we
will be pulling data from, the foreign key column on that table, and finally the
column to pull data from.


"""
#==== Packages ====#

import sys,re
from PyQt5.QtCore import QSize,Qt 
from PyQt5.QtSql import (QSqlDatabase, QSqlRelationalDelegate,QSqlTableModel,
                        QSqlRelation,QSqlRelationalTableModel,QSqlQuery,QSqlQueryModel)
from PyQt5.QtWidgets import (QApplication,QMainWindow,QTableView,
                            QLineEdit,QVBoxLayout,QWidget,QHBoxLayout)


#==== Class ===#

db = QSqlDatabase("QSQLITE")
db.setDatabaseName("Model_View_Architecture\\chinook.sqlite")
db.open()

class MainWindowSQL(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)

        self.model.setTable('Track') # table name
        self.model.select()

        self.setMinimumSize(QSize(1024,600))
        self.setCentralWidget(self.table)


# Sorting columns
class MainWindowSQLSorting(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)

        self.model.setTable("Track")
        #self.model.setSort(2,Qt.DescendingOrder) # sorting by  index columns
        idx = self.model.fieldIndex("Milliseconds") # sorting by name columns
        self.model.setSort(idx,Qt.DescendingOrder)
        self.model.select()

        self.setMinimumSize(QSize(1080,600))
        self.setCentralWidget(self.table)

# Columns titles
class MainWindowsSQLColumnsTitle(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QTableView()
        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)
        
        self.model.setTable('Track')
        #self.model.setHeaderData(1,Qt.Horizontal,'Name')
        #self.model.setHeaderData(2,Qt.Horizontal,'Albun (ID)')
        #self.model.setHeaderData(3,Qt.Horizontal,'Media Type (ID)')
        #self.model.setHeaderData(4,Qt.Horizontal,'Genre (ID)')
        #self.model.setHeaderData(5,Qt.Horizontal,'Composer')

        # Using a dict
        column_title:dict[str,str] = {
            "Name": "Name",
            "AlbumID": "Album (ID)",
            "MediaTypeId": "Media Type (ID)",
            "GenreId": "Genre (ID)",
            "Composer": "Composer",
        }
        for n,t in column_title.items():
            idx = self.model.fieldIndex(n)
            self.model.setHeaderData(idx,Qt.Horizontal,t)

        self.model.select()

        self.setMinimumSize(QSize(1080,600))
        self.setCentralWidget(self.table)

# Filter field
class MainWindowsSQLFilter(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        container = QWidget()
        layout = QVBoxLayout()

        self.search = QLineEdit()
        self.search.textChanged.connect(self.update_filter)
        self.table = QTableView()

        layout.addWidget(self.search)
        layout.addWidget(self.table)
        container.setLayout(layout)

        self.model = QSqlTableModel(db=db)
        self.table.setModel(self.model)

        self.model.setTable('Track')
        self.model.select()

        self.setMinimumSize(QSize(1080,600))
        self.setCentralWidget(container)
    
    def update_filter(self,s) -> None:
        s = re.sub("[\W_]+","",s)
        filter_str = 'Name LIKE "%{}%"'.format(s)
        self.model.setFilter(filter_str)


# Displaying related data with QSqLReationalTableModel
class MainWindowsSQLRelation(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QTableView()
        self.model = QSqlRelationalTableModel(db=db)
        self.table.setModel(self.model)
        #relation = QSqlRelation('<realated_table','<related_table_foregin_key_column','<column_to_display>')
        
        self.model.setTable('Track')
        self.model.setRelation(2,QSqlRelation('Album','AlbumId','Title'))
        self.model.setRelation(3,QSqlRelation('MediaType','MediaTypeId','Name'))
        self.model.setRelation(4,QSqlRelation('Genre','GenreId','Name'))
        
        # Edit related fields
        delegate = QSqlRelationalDelegate(self.table)
        self.table.setItemDelegate(delegate)

        self.model.select()
        self.setMinimumSize(QSize(1080,600))
        self.setCentralWidget(self.table)

# Generic queries with QSqLQueryModel
dbquery = QSqlDatabase('QSQLITE')
dbquery.setDatabaseName("Model_View_Architecture\\chinook.sqlite")
dbquery.open()

class MainWindowSQLQuery(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        self.table = QTableView()
        self.model = QSqlQueryModel()
        self.table.setModel(self.model)
        
        #query = QSqlQuery("Select Name,Composer From Track",db=dbquery)
        #self.model.setQuery(query)

        # Parametrized queries to protect SQL databes
        query = QSqlQuery(db=dbquery)
        query.prepare(
            "Select Name, Composer, Album.Title From Track "
            "Inner join Album on Track.AlbumId = Album.AlbumId "
            "Where Album.Title like '%' || :album_title || '%' "
        )
        query.bindValue(":album_title","Sinatra")
        query.exec_()

        self.model.setQuery(query)
        self.setMinimumSize(QSize(1080,600))
        self.setCentralWidget(self.table)

# Query Model to searching
class MainWindowSQLSearch(QMainWindow):
    def __init__(self) -> None:
        super().__init__()
        container = QWidget()
        layout_search = QHBoxLayout()

        self.track = QLineEdit()
        self.track.setPlaceholderText("Track name...")
        self.track.textChanged.connect(self.update_query)

        self.composer = QLineEdit()
        self.composer.setPlaceholderText('Artist  name...')
        self.composer.textChanged.connect(self.update_query)
        
        self.album = QLineEdit()
        self.album.setPlaceholderText('Album name...')
        self.album.textChanged.connect(self.update_query)
        
        layout_search.addWidget(self.track)
        layout_search.addWidget(self.composer)
        layout_search.addWidget(self.album)

        layout_view = QVBoxLayout()
        layout_view.addLayout(layout_search)

        self.table = QTableView()
        layout_view.addWidget(self.table)

        container.setLayout(layout_view)

        self.model = QSqlQueryModel()
        self.table.setModel(self.model)

        self.query = QSqlQuery(db=dbquery)
        self.query.prepare(
            "Select Name, Composer, Album.Title From Track "
            "Inner join Album on Track.AlbumId=Album.AlbumId Where "
            "Track.Name like '%' || :track_name || '%' and "
            "Track.Composer like '%' || :track_composer || '%' and " # keep space in the end sentence
            "Album.Title like '%' || :album_title || '%' "
        )

        self.update_query()

        self.setMinimumSize(QSize(1080,600))
        self.setCentralWidget(container)
    
    def update_query(self,s=None) -> None:
        track_name = self.track.text()
        track_composer = self.composer.text()
        track_album = self.album.text()

        self.query.bindValue(":track_name",track_name)
        self.query.bindValue(":track_composer",track_composer)
        self.query.bindValue(":album_title",track_album)

        self.query.exec_()
        self.model.setQuery(self.query)




#==== Main ====#

app = QApplication(sys.argv)
#window = MainWindowSQL()
#window = MainWindowSQLSorting()
#window = MainWindowsSQLColumnsTitle()
#window = MainWindowsSQLFilter()
#window = MainWindowsSQLRelation()
#window = MainWindowSQLQuery()
window = MainWindowSQLSearch()
window.show()
app.exec_()
