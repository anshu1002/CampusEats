class OrderStore:
    def __init__(self):
        self.orders = {}

    def create(self, order):
        self.orders[order.order_id] = order
        return order

    def get(self, order_id):
        return self.orders.get(order_id)

    def list(self, customer_id=None, status=None):
        orders = list(self.orders.values())

        if customer_id is not None:
            orders = [
                order for order in orders
                if order.customer_id == customer_id
            ]

        if status is not None:
            orders = [
                order for order in orders
                if order.status == status
            ]

        return orders

    def update(self, order):
        self.orders[order.order_id] = order
        return order