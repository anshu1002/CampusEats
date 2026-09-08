class OrderItem:
    def __init__(self, item_id, quantity):
        self.item_id = item_id
        self.quantity = quantity

    def as_json(self):
        return {
            "item_id": self.item_id,
            "quantity": self.quantity
        }


class Order:
    def __init__(self, order_id, customer_id, items, status="created"):
        self.order_id = order_id
        self.customer_id = customer_id
        self.items = items
        self.status = status

        # Internal field
        self.internal_id = "INTERNAL-" + order_id

    def as_json(self):
        return {
            "order_id": self.order_id,
            "customer_id": self.customer_id,
            "items": [item.as_json() for item in self.items],
            "status": self.status
        }


def validate(data):
    """
    Validate the incoming create-order request.
    Returns (True, None) when valid.
    Returns (False, error_message) when invalid.
    """

    if not isinstance(data, dict):
        return False, "Request body must be a JSON object."

    if "customer_id" not in data:
        return False, "customer_id is required."

    if "items" not in data:
        return False, "items is required."

    if not isinstance(data["customer_id"], str):
        return False, "customer_id must be a string."

    if not isinstance(data["items"], list):
        return False, "items must be an array."

    if len(data["items"]) == 0:
        return False, "items must contain at least one item."

    for item in data["items"]:

        if not isinstance(item, dict):
            return False, "Each item must be an object."

        if "item_id" not in item:
            return False, "item_id is required."

        if "quantity" not in item:
            return False, "quantity is required."

        if not isinstance(item["item_id"], str):
            return False, "item_id must be a string."

        if not isinstance(item["quantity"], int):
            return False, "quantity must be an integer."

        if item["quantity"] < 1:
            return False, "quantity must be at least 1."

    return True, None