from configparser import ConfigParser
import xdg # type: ignore
import os

class Config:
    def __init__(self, file=None):
        if file is None:
            file = xdg.BaseDirectory.xdg_config_home
        elif not os.path.exists(file):
            raise FileNotFoundError
        
        cp = ConfigParser()
        cp.read(file)
        
        self.apikey = file['ApiKey']
        self.gamedir = file['GameDirectory']