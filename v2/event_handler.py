
from watchdog.events import FileSystemEventHandler
from os_paths import os_paths, SUSPICIOUS_EXTS
import time
import psutil
import os 
import threading


opened_files = {}

         

def match_os_path(file_path):
    for folder, ext_list in os_paths.items():
        if folder in file_path:
            return ext_list
    return None

def find_setup(name):
     print(f"Waiting for {name} to start...")
     while True:
        processes = psutil.process_iter(['pid', 'name'])
        proc_list = [p for p in processes]
        for p in proc_list:
            if p.info['name'] == name:
            
                return p
        time.sleep(0.2)

def list_family_processes(proc):
     
    family = {proc.pid}
    for child in proc.children(recursive = True):
       family.add(child.pid)
    return family
          
          

class Handler(FileSystemEventHandler):
    def __init__(self, setup_name):
        self.process_family = {}

        self.suspicious_paths = {}
        self.written_paths = []
        self.created_folders = []
        self.sus_events = {}

        self.main_process = find_setup(setup_name)
        self.process_family = list_family_processes(self.main_process)

        threading.Thread(target=self.process_handle, daemon=True).start()

        print(self.process_family)
        
    def on_created(self, event):
        if not self.folder_match(event.src_path): return 

        self.handle_moved_create(event.src_path, event)
                      

    def on_moved(self, event):
        if not self.folder_match(event.dest_path): return 
       
        self.handle_moved_create(event.dest_path, event)

    def on_modified(self, event):
        if not opened_files.get(event.src_path, None):
            return
        path = event.src_path
        if "System32\\drivers\\etc\\hosts" in path:
            self.sus_events['hosts modified'] = (
            'The hosts file was modified. This can be used to block or redirect internet access.'
    )

              
    
    def handle_moved_create(self, path, event):
        self.path = path
        print(path)
        _, self.ext = os.path.splitext(self.path)
        
        if self.ext == '' : 
             return
        
        time.sleep(0.05)
        if event.is_directory:
            self.created_folders.append(self.path)

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

                else: ### HANDLE FILES WRITTEN ANYWHERE ELSE BUT NOT SUS, save their dir names
                    dirparts = self.path.split('\\')[0:-1]
                    dirname = '\\'.join(dirparts)
                    
                    self.written_paths.append(dirname)

    def handle_sus(self):
         
                    self.suspicious_paths[self.sus_len] = {'path': self.path, 'type': self.ext, 
                                                           }
    def folder_match(self, path):
        dirname = os.path.dirname(path)
        now = time.time()
        print(opened_files)
        for opened_path, info in opened_files.items():
            opened_dir = os.path.dirname(opened_path)
            print(opened_dir)
            print(dirname)
            # same directory?
            if opened_dir == dirname:
                # within 150ms window?
                if now - info['time'] < 0.15:
                    return True

        return False
                      
    def process_handle(self):
        global opened_files
        noisy = ['C:\\Program Files\\WindowsApps\\', 'C:\\Windows\\Fonts\\']
        while True:
            for proc in psutil.process_iter(['pid', 'name']):
                    
                    try:
                        for f in proc.open_files():
                            if "C:\\Program Files\\WinRAR" in f.path:
                                print(proc.info['name'])
                                self.process_family.add(proc.pid)
                    except:
                        pass
                    
            now = time.time()
            if not self.process_family: return 

            for pid in list(self.process_family):
                try:
                    proc = psutil.Process(pid)
                    files = [f.path for f in proc.open_files()]
                    for file in files:
                        _, ext = os.path.splitext(file)
                        if ext == '.mui' or ext == '.sdb': continue
                        if any(file.startswith(n) for n in noisy):
                            continue
                        
                        opened_files[file] = {'time': now}
                    


                except psutil.NoSuchProcess:
                
                    self.process_family.discard(pid)
                    
            cutoff = now - 0.15    
            to_delete = []
            for path, info in opened_files.items():
                if info['time'] < cutoff:
                    to_delete.append(path)

            for p in to_delete:

               del opened_files[p]       

            time.sleep(0.05)