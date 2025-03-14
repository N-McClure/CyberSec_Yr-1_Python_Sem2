import threading
import time

class WriteNotes(threading.Thread):
    def __init__(self):
        super().__init__()
        # Override the run() method from Thread.
    def run(self):
        print("Staring writing a note...")
        time.sleep(3)
        print("Finished writing a note.")


if __name__ == '__main__':
    print("Checking Main thread...")
    writer = WriteNotes() # Creates a WriteNotes() object.
    print(f'Thread Status: {writer.is_alive()}')
    
    print("Starting Main thread...")
    writer.start() # Starts the WriteNotes() object's run() method.
    print(f'Thread Status: {writer.is_alive()}')
    
    print("Sending Main thread to sleep...")
    time.sleep(0.5)
    print(f'Thread Status: {writer.is_alive()}')
    
    print("Joining Main thread to the WriteNotes thread..")
    writer.join() # Waits for the WriteNotes() object's run() method to finish.
    print(f'Thread Status: {writer.is_alive()}')
    
    print(f'Both threads are Done...')
    print(f'Thread Status: {writer.is_alive()}')
