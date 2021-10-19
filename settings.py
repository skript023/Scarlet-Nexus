import json
import os
from logger import g_logger

class Settings():
    def dpg_load_config(self, key:str):
        file_location = "json/gui setting.json"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        if not os.path.isfile(file_location) and not os.access(file_location, os.R_OK):
            g_logger.log_to_console(g_logger.info, "Gui settings")
            with open(file_location, 'w') as db_file:
                db_file.write(json.dumps({"Height":800, "Width":600, "Font":15}, indent=4))
        self.file = open(file_location)
        self.options = json.loads(self.file.read())
        self.file.close()
        return self.options[key]

    def dpg_save_config(self, key:str, value=0):
        file_location = "json/gui setting.json"
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        self.temp = open(file_location)
        self.json_temp = json.load(self.temp)
        self.temp.close()
        self.json_temp[key] = value
        self.new_file = open(file_location, "w")
        json.dump(self.json_temp, self.new_file, indent=4)
        self.new_file.close()

g_settings = Settings()