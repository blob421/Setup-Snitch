

from watchdog.observers import Observer
import time
from print_report import get_report
from event_handler import Handler
          

observer = Observer()
observed_path = 'C:\\'
handler = Handler()

observer.schedule(handler, observed_path, recursive=True)
observer.start()
print('\nWELCOME TO SETUP SNITCH')
print('=======================')
try:
    print('Watcher starting ...')
    print('Press "ctrl + c" when you are done to print your report')
    while True:
        time.sleep(1)
        observer.join(1)
        
except KeyboardInterrupt:
    get_report(handler)
    observer.stop()

observer.join()
