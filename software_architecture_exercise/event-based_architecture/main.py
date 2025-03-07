from event_bus import EventBus
from order_service import OrderService
from inventory_service import InventoryService
from notification_service import NotificationService
import time

if __name__ == "__main__":
    event_bus = EventBus()
    event_bus.start_listening()

    order_service = OrderService(event_bus)
    inventory_service = InventoryService(event_bus)
    notification_service = NotificationService(event_bus)

    order_service.create_order("Product-0", 0)
    time.sleep(1)  # allow events to be processed before doing the next process
    order_service.create_order("Product-1", 10)
    time.sleep(1)
