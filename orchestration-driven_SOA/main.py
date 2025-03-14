class OrderService:
    order_counter = 1234  # Starting order ID
    
    def create_order(self, customer_id, product_id, quantity):
        self.order_counter += 1
        print(f"Order Created: Customer ID {customer_id}, Product ID {product_id}, Quantity {quantity}, Order ID {self.order_counter}")
        
        return {"order_id": self.order_counter, "customer_id": customer_id, "product_id": product_id, "quantity": quantity}


class PaymentService:
    payment_counter = 101  # Starting payment ID
    
    def process_payment(self, order_id, amount):
        self.payment_counter += 1
        print(f"Processing payment for Order ID {order_id}, Amount: ${amount}, Payment ID {self.payment_counter}")
        if amount > 1000:
            print("Payment requires manual intervention. Order halted.")
            return {"payment_id": None, "status": "Manual Check Required"}
        if amount < 0:
            print("Invalid payment amount. Payment failed.")
            return {"payment_id": None, "status": "Failed"}
        print("Payment processed successfully.")
        return {"payment_id": self.payment_counter, "status": "Success"}


class InventoryService:
    def check_inventory(self, product_id, quantity):
        print(f"Checking inventory for Product ID {product_id}, Quantity {quantity}")
        available = quantity <= 10  # Simulating stock availability check
        print("Inventory available." if available else "Insufficient inventory.")
        
        return {"available": available}
    
    def update_inventory(self, product_id, quantity):
        print(f"Updating inventory for Product ID {product_id}, Quantity {quantity}")
        
        return {"status": "Updated"}


class ShippingService:
    shipping_counter = 202  # Starting shipping ID
    
    def arrange_shipping(self, order_id, customer_id):
        self.shipping_counter += 1
        print(f"Arranging shipping for Order ID {order_id} to Customer {customer_id}, Shipping ID {self.shipping_counter}")
        if customer_id == -1:
            print("Invalid customer ID. Shipping failed.")
            return {"shipping_id": None, "status": "Failed"}
        print("Shipping arranged successfully.")
        
        return {"shipping_id": self.shipping_counter, "status": "Arranged"}


# Orchestration Engine
class OrderOrchestrator:
    def __init__(self):
        self.order_service = OrderService()
        self.payment_service = PaymentService()
        self.inventory_service = InventoryService()
        self.shipping_service = ShippingService()
    
    def process_order(self, customer_id, product_id, quantity, price):
        print("Starting order processing...")
        order = self.order_service.create_order(customer_id, product_id, quantity)
        
        payment = self.payment_service.process_payment(order["order_id"], quantity * price)
        if payment["status"] == "Manual Check Required":
            print("OrderOrchestrator: Payment requires manual review. Order halted.")
            return
        if payment["status"] != "Success":
            print("OrderOrchestrator: Payment failed. Order cannot proceed.")
            return
        
        inventory_status = self.inventory_service.check_inventory(product_id, quantity)
        if not inventory_status["available"]:
            print("OrderOrchestrator: Order cannot be processed due to insufficient inventory.")
            return
        
        self.inventory_service.update_inventory(product_id, quantity)
        shipping = self.shipping_service.arrange_shipping(order["order_id"], customer_id)
        if shipping["status"] == "Failed":
            print("OrderOrchestrator: Shipping failed. Order cannot proceed.")
            return
        
        print(f"Order {order['order_id']} processed successfully! Shipping status: {shipping['status']}")
        print("--- Order Process Completed ---")
        
        return {
            "order": order,
            "payment": payment,
            "shipping": shipping
        }

# Main Application
if __name__ == "__main__":
    orchestrator = OrderOrchestrator()
    print("\n--- Processing First Order ---")
    result1 = orchestrator.process_order(customer_id=1, product_id=100, quantity=5, price=50)
    print("Final Order Processing Result:", result1)
    
    print("\n--- Processing Second Order ---") # This order will fail due to insufficient inventory
    result2 = orchestrator.process_order(customer_id=2, product_id=200, quantity=12, price=75)
    print("Final Order Processing Result:", result2)
    
    print("\n--- Processing Third Order ---") # This order will require manual payment review
    result3 = orchestrator.process_order(customer_id=3, product_id=300, quantity=3, price=30)
    print("Final Order Processing Result:", result3)
    
    print("\n--- Processing Fourth Order ---")  # This order will fail due to invalid payment amount
    result4 = orchestrator.process_order(customer_id=4, product_id=400, quantity=1, price=-10)
    print("Final Order Processing Result:", result4)
    
    print("\n--- Processing Fifth Order ---")  # This order will fail due to invalid customer ID
    result5 = orchestrator.process_order(customer_id=-1, product_id=500, quantity=2, price=20)
    print("Final Order Processing Result:", result5)
