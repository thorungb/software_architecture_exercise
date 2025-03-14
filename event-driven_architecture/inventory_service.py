class InventoryService:
    def __init__(self, event_bus):
        self.event_bus = event_bus
        self.inventory = {}
        self.event_bus.subscribe('order_created', self.handle_order_created)

    def handle_order_created(self, order_data):
        product_name = order_data['product_name']
        quantity = order_data['quantity']

        if product_name in self.inventory:
            self.inventory[product_name] -= quantity
        else:
            self.inventory[product_name] = 100 - quantity

        print(f"Inventory Updated: {product_name} stock reduced by {quantity}")
