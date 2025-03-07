class NotificationService:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.event_bus.subscribe('order_created', self.handle_order_created)

    def handle_order_created(self, order_data):
        order_id = order_data['order_id']
        product_name = order_data['product_name']
        print(f"Sending notification for Order ID: {order_id} - {product_name}")
