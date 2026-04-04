

from watchdog.observers import Observer
import time
from print_report import get_report
from event_handler import Handler
import os        






print('\nWELCOME TO SETUP SNITCH')
print('=======================\n')



observer = Observer()
observed_path = 'C:\\'
handler = Handler()

observer.schedule(handler, observed_path, recursive=True)
observer.start()


try:

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

