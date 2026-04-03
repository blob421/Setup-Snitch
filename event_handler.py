
from watchdog.events import FileSystemEventHandler
from os_paths import os_paths, SUSPICIOUS_EXTS
import time
import os

def match_os_path(file_path):
    for folder, ext_list in os_paths.items():
        if folder in file_path:
            return ext_list
    return None



class Handler(FileSystemEventHandler):
    def __init__(self, install_path):
        self.suspicious_paths = {}
        self.written_paths = set()
        self.created_folders = []
        self.files_created_main = 0
        paths_chunks = install_path.split('\\')
        self.program_path = '\\'.join(paths_chunks)
        self.sus_events = {}

        self.start_time = time.time()

        self.excluded_dirs = set()
        self.init_phase = True
        print('Configuring ... , the program will start in ~ 15 seconds')
        
    def on_created(self, event):
   
       self.handle_moved_create(event.src_path, event)
                      
    def on_moved(self, event):
    
        self.handle_moved_create(event.dest_path, event)

    def on_modified(self, event):
        path = event.src_path
        if "System32\\drivers\\etc\\hosts" in path:
            self.sus_events['hosts modified'] = (
            'The hosts file was modified. This can be used to block or redirect internet access.'
    )

              
    
    def handle_moved_create(self, path, event):
        self.path = path
        dirname = os.path.dirname(self.path)

        if dirname in self.excluded_dirs: return

        elif self.init_phase:
            now = time.time()
            self.excluded_dirs.add(dirname)
            if self.start_time < now - 15:
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
                self.created_folders.append(self.path)

            elif self.program_path in self.path and not self.init_phase:
                self.files_created_main += 1

            else:
            
                 
                self.sus_len = len(self.suspicious_paths)

                extensions = match_os_path(self.path)
                

                if extensions:  ### HANDLE FILES WRITTEN IN SYSTEM DIRS 
                    if not self.ext in extensions:
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