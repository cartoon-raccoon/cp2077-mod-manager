import urllib3
import json

from cpmm.mods import CyberpunkMod

globalhttp = urllib3.PoolManager()

BASE_API_URL = "https://api.nexusmods.com/v1/games/cyberpunk2077/mods"

class ApiError(Exception):
    def __init__(self, data, status):
        self.msg = json.loads(data)["message"]
        self.status = status
        
    def __repr__(self):
        return f"Nexus Mods returned error {self.status}:\n{self.msg}"
        

def get_mod_data(id, apikey, raw=False):
    resp = globalhttp.request("GET", f"{BASE_API_URL}/{id}.json",
                              headers={"apikey": apikey})
    if resp.status != 200:
        raise ApiError(resp.data, resp.status)
    parsed = json.loads(resp.data)
    
    if raw:
        return parsed
    else:
        return CyberpunkMod(
            parsed["name"], 
            parsed["mod_id"],
            parsed["summary"],
            parsed["author"],
            parsed["updated_timestamp"]
        )
    
def get_mod_files(id, apikey):
    resp = globalhttp.request("GET", f"{BASE_API_URL}/{id}/files.json",
                              headers={"apikey", apikey})
    if resp.status != 200:
        raise ApiError(resp.data, resp.status)
    return json.loads(resp.data)

def download_file(mod_id, file_id, apikey):
    pass # todo