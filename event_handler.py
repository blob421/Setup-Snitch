
from watchdog.events import FileSystemEventHandler
from os_paths import SUSPICIOUS_EXTS, EXCEPTIONS_BY_PATH
import time
import os
import re 
def get_program_path():
    print('\nEnter the setup installation path')
    install_dir = input("E.g. (C:\\ProgramFiles\\newapp) : ")
    return install_dir

def match_os_path(file_path):
    for folder, ext_list in EXCEPTIONS_BY_PATH.items():
        if folder in file_path:
            return ext_list
    return None



class Handler(FileSystemEventHandler):
    def __init__(self):
        self.suspicious_paths = {}
        self.written_paths = set()
        self.created_folders = []
        self.files_created_main = 0
      
        self.sus_events = {}

        self.start_time = time.time()

        self.excluded_dirs = set()
        self.init_phase = True
        print('Configuring ... , the program will start in ~ 20 seconds')
    
        
    def on_created(self, event):
   
       self.handle_moved_create(event.src_path, event)
                      
    def on_moved(self, event):
    
        self.handle_moved_create(event.dest_path, event)

    def on_modified(self, event):
        path = event.src_path
        if "System32\\drivers\\etc\\hosts" in path:
            self.sus_events['hosts modified'] = (
            "The hosts file was modified. It’s often caused by a browser, but still worth checking ."
    )

              
    
    def handle_moved_create(self, path, event):
        self.path = path
        dirname = os.path.dirname(self.path)

        if dirname in self.excluded_dirs: return

        elif self.init_phase:
            now = time.time()
            self.excluded_dirs.add(dirname)
            if self.start_time < now - 20:

                install_path = get_program_path()
                paths_chunks = install_path.split('\\')
                self.program_path = '\\'.join(paths_chunks)
                print('\nWatcher starting ...')
                print('Press "ctrl + c" when you are done to print your report')
                self.init_phase = False
        
        else:
            _, self.ext = os.path.splitext(self.path)
            if self.ext == '': 
                 return 
            else: 
                self.ext = self.ext.split('.')[1]

            time.sleep(0.05)
            
            if event.is_directory and not self.init_phase:
                if self.is_NSIS():
                     return
                self.created_folders.append(self.path)

            elif not self.init_phase and (self.program_path in self.path): 
                self.files_created_main += 1

            else:
            
                 
                self.sus_len = len(self.suspicious_paths)

                extensions = match_os_path(self.path)
                

                if extensions:  ### HANDLE FILES WRITTEN IN SYSTEM DIRS 
                    if self.is_NSIS():
                              return
                         
                    elif not self.ext in extensions and self.ext in SUSPICIOUS_EXTS:
                            self.handle_sus()
           
                else:
                    ### HANDLE FILES WRITTEN ANYWHERE ELSE AND SUS
                    if self.ext in SUSPICIOUS_EXTS:
                        self.handle_sus()

                    else:  ### Add even if not necessarily harmful to show activity outside of main
                        self.written_paths.add(self.path) 
                        

    def handle_sus(self):
         
                    self.suspicious_paths[self.sus_len] = {'path': self.path, 'type': self.ext, 
                                                           }

    def is_NSIS(self):

        if '\\AppData\\Local\\Temp' in self.path:
                    reg_string = r'^[A-Za-z]:\\([^\\]+\\)*AppData\\Local\\Temp\\ns[a-zA-Z0-9]{4}\.tmp\\?$'
                    if re.search(reg_string, self.path):
                        return True
        return False