
from watchdog.events import FileSystemEventHandler
from os_paths import os_paths, SUSPICIOUS_EXTS
import psutil
import os 

def match_os_path(file_path):
    for folder, ext_list in os_paths.items():
        if folder in file_path:
            return ext_list
    return None

def get_recent_writers(path):
    writers = []
    for p in psutil.process_iter(['pid', 'name', 'open_files']):
        try:
            for f in p.info['open_files'] or []:
                if f.path == path:
                    writers.append(p.info['name'])
        except:
            pass
    return writers

  
class Handler(FileSystemEventHandler):
    def __init__(self, install_path):
        self.suspicious_paths = {}
        self.written_paths = []
        self.created_folders = []
        self.files_created_main = 0
        paths_chunks = install_path.split('\\')
        self.program_path = '\\'.join(paths_chunks)

    def on_created(self, event):
       self.handle_moved_create(event.src_path, event)
                      

    def on_moved(self, event):
    
        self.handle_moved_create(event.dest_path, event)

    def handle_moved_create(self, path, event):
        self.path = path
        
        self.ext = self.path.split('.')[-1] or '???'
        
        
        if event.is_directory:
            self.created_folders.append(self.path)

        elif self.program_path in self.path:
            self.files_created_main += 1

        else:
            self.writters = get_recent_writers(self.path) or '???'
                 
            self.sus_len = len(self.suspicious_paths)
            extensions = match_os_path(self.path)


            if extensions:  ### HANDLE FILES WRITTEN IN SYSTEM DIRS 
                  if not self.ext in extensions:
                        self.handle_sus()
            else:
                       ### HANDLE FILES WRITTEN ANYWHERE ELSE AND SUS
                 if self.ext in SUSPICIOUS_EXTS:
                      self.handle_sus()

                 else: ### HANDLE FILES WRITTEN ANYWHERE ELSE BUT NOT SUS, save their dir names
                      dirparts = self.path.split('\\')[0:-1]
                      dirname = '\\'.join(dirparts)
                     
                      self.written_paths.append(dirname)

    def handle_sus(self):
         
                    self.suspicious_paths[self.sus_len] = {'path': self.path, 'type': self.ext, 
                                                           'program': self.writters}