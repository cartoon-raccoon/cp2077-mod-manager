import sqlite3
import xdg

class DatabaseConn:
    def __init__(self, dbfile=None):
        if dbfile is None:
            dbfile = xdg.BaseDirectory.xdg_data_home
        self.database = sqlite3.connect(dbfile)
        
        # create tables if needed
        self.database.execute("""CREATE TABLE IF NOT EXISTS mods
        (
                name TEXT,
                id INT,
                summary TEXT,
                author TEXT,
                version TEXT,
                packagefile TEXT,
                updated_date TEXT,
                install_date TEXT,
                dependencies TEXT
        )""")