
from watchdog.events import FileSystemEventHandler


paths_used_by_os = ['\\AppData\\Local\\D3DSCache\\', 
                    '\\AppData\\Local\\Microsoft\\Edge\\',
                    '\\AppData\\Local\\Temp\\']


def is_suspicious(string):
     extension = string.split('.')[-1]
     if extension in ['exe', 'dll', 'bat', 'ps1']:
         return extension
     else:
         return None
     

class Handler(FileSystemEventHandler):
    def __init__(self):
        self.suspicious_paths = {}
        self.written_paths = {}
        self.created_folders = []
        

    def on_created(self, event):
        event_path = event.src_path
        in_active_paths = False

        if event.is_directory:
            self.created_folders.append(event_path)
        
        else:
            
            for p in paths_used_by_os:
                if p in event_path:
                    in_active_paths = True
                    extension = is_suspicious(event_path)
                    if extension: 
                        self.suspicious_paths[f'{len(self.suspicious_paths.keys())}'] = {'type': extension, 
                                                                                         'path': event_path}
                        print(f'\nSuspicious file created: {event_path}')
                        break 