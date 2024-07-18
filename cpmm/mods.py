import datetime
import re

# subdirectories of the game install folder where various things go
GAMEDIR_SUBDIRS = [
    "archive",
    "bin",
    "engine",
    "mods",
    "r6",
    "red4ext",
    "tools",
]

class CyberpunkMod:
    """An object representing data about a Cyberpunk 2077 mod.
    """
    
    FILENAME_REGEX = r"^(.+)-([0-9]{4,6})-(([0-9]{1,2}-){1,4})([0-9]+)\.(7?zip|rar|xz)$"
    
    def __init__(self, 
                 name, id, summary, author, 
                 version, package_file, updated_date,
                 install_date=None):
        self.name = name
        self.id = int(id)
        self.summary = summary
        self.author = author
        self.version = version
        self.package_file = package_file
        # convert date to datetime object
        if isinstance(updated_date, str):
            # if str, assume it is formatted to Nexus formatting
            pass
        elif isinstance(updated_date, int):
            # if int, assume it is a unix timestamp
            updated_date = datetime.datetime.fromtimestamp(updated_date)
        self.updated_date = updated_date
        self.install_date = install_date
        
    def install(self, config):
        # if we have an install date, it's already installed
        if self.install_date is not None:
            return
        
        # todo
    
    @staticmethod
    def parse_data_from_filename(filename):
        matcher = re.compile(CyberpunkMod.FILENAME_REGEX)
        matches = matcher.match(filename)
        if matches is None:
            return None
        try:
            raw_filename = matches.group(1)
            # all int conversions should succeed, otherwise we have a regex bug
            mod_id = int(matches.group(2))
            version = ".".join(matches.group(3)[:-1].split("-"))
            updated_timestamp = int(matches.group(5))
        except IndexError:
            pass # todo: raise some sort of error to transition to manual entry
        
        # todo: pull data from nexus to ensure we have a match,
        # then construct the mod object and return it