import datetime as date
import shutil
import os
import inspect
import os.path

class bcolors():
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

class Logger(bcolors):
    def __init__(self) -> None:
        time = date.datetime.now()
        self.posix_time = f"[{time.hour}:{time.minute}:{time.second}]"
        self.is_signature_loaded = False
    
    def log_to_console(self, message:str):
        caller_filename_full = inspect.stack()[1].filename
        caller_filename_only = os.path.splitext(os.path.basename(caller_filename_full))[0]
        file_location = '%s\\Ellohim External\\Ellohim Log.log' %  os.environ['APPDATA']
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        time = date.datetime.now()
        file = open(file_location,"a")
        # \n is placed to indicate EOL (End of Line)
        file.write(f"[{time.hour}:{time.minute}:{time.second}] [{caller_filename_only}.pyc:{inspect.stack()[1][2]}:{inspect.stack()[1][3]}] {message} \n")
        print(f"[{time.hour}:{time.minute}:{time.second}] {message}")
        file.close() #to change file access modes

    def logger(self, message:str):
        print(f"{self.posix_time} {message}")

    def log_to_file(self, message:str):
        caller_filename_full = inspect.stack()[1].filename
        caller_filename_only = os.path.splitext(os.path.basename(caller_filename_full))[0]
        file_location = '%s\\Ellohim External\\Ellohim Log.log' %  os.environ['APPDATA']
        os.makedirs(os.path.dirname(file_location), exist_ok=True)
        time = date.datetime.now()
        file = open(file_location,"a")
        # \n is placed to indicate EOL (End of Line)
        file.write(f"[{time.hour}:{time.minute}:{time.second}] [{caller_filename_only}.pyc:{inspect.stack()[1][2]}:{inspect.stack()[1][3]}] {message} \n")
        file.close() #to change file access modes

    def clean_log_file(self):
        file_location = '%s\\Ellohim External\\Ellohim Log.log' %  os.environ['APPDATA']
        open(file_location,"w").close()

    def copy_file(self, src, dst):
        shutil.copyfile(src, dst)

    def rename_file(self, scr, dst):
        os.rename(scr, dst)

g_logger = Logger()