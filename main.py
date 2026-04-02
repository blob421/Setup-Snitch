

from watchdog.observers import Observer
import time
from print_report import get_report
from event_handler import Handler
import os        

def get_program_path():
    print('Enter the setup installation path')
    install_dir = input("E.g. (C:\\ProgramFiles\\newapp) : ")
    return install_dir



print('\nWELCOME TO SETUP SNITCH')
print('=======================\n')

PROGRAM_PATH = get_program_path()

observer = Observer()
observed_path = 'C:\\'
handler = Handler(PROGRAM_PATH)

observer.schedule(handler, observed_path, recursive=True)
observer.start()


try:
    print('\nWatcher starting ...')
    print('Press "ctrl + c" when you are done to print your report')
    while True:
        time.sleep(1)
        observer.join(1)
        
except KeyboardInterrupt:
    get_report(handler)
    try: 
      observer.stop()
      print('\n\nPress "ctrl + c" to exit the program')
      while True:
          
          time.sleep(10)
    except KeyboardInterrupt:
        os._exit(0)

