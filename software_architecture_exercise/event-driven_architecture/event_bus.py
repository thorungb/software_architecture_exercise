import threading
import queue
import time
import json
from typing import Callable, Dict


class EventBus:
    def __init__(self):
        self.subscribers = {}
        self.event_queue = queue.Queue()
        self.is_running = False
        self.thread = None

    def subscribe(self, event_type: str, callback: Callable):
        if event_type not in self.subscribers:
            self.subscribers[event_type] = []
        self.subscribers[event_type].append(callback)

    def publish(self, event_type: str, data: Dict):
        event = {
            'type': event_type,
            'data': data,
            'timestamp': time.time()
        }
        self.event_queue.put(event)

    def start_listening(self):
        if self.is_running:
            return

        self.is_running = True
        self.thread = threading.Thread(target=self._process_events)
        self.thread.daemon = True
        self.thread.start()

    def _process_events(self):
        while self.is_running:
            try:
                event = self.event_queue.get(timeout=1)
                event_type = event['type']

                if event_type in self.subscribers:
                    for callback in self.subscribers[event_type]:
                        try:
                            callback(event['data'])
                        except Exception as e:
                            print(f"Error in callback for {event_type}: {e}")
                self.event_queue.task_done()
            except queue.Empty:
                pass

    def stop(self):
        self.is_running = False
        if self.thread:
            self.thread.join()
