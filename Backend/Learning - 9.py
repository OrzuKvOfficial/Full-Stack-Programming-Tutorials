import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        print(f'Fayl yaratildi: {event.src_path}')
        
    def on_modified(self, event):
        print(f'Fayl o‘zgartirildi: {event.src_path}')
        
    def on_deleted(self, event):
        print(f'Fayl o‘chirildi: {event.src_path}')

if __name__ == "__main__":
    path = "."  # Kuzatiladigan papka manzili (joriy papka)
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
