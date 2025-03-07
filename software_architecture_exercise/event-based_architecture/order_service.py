import json


class OrderService:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.order_count = 0

    def create_order(self, product_name: str, quantity: int):
        order = {
            'order_id': self.order_count,
            'product_name': product_name,
            'quantity': quantity
        }
        self.order_count += 1
        print(f"Order Created: {json.dumps(order)}")
        self.event_bus.publish('order_created', order)
