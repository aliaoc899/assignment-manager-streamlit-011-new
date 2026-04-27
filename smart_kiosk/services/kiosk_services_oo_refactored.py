import uuid
from typing import Optional, List, Dict

class OrderManager:
    def __init__(self,inventory: List,orders: List) -> None:
        self.orders= orders
        self.inventory = inventory

    def place_order(self, item_id: str, quantity: int) -> Optional[Dict]:
        # find item in the inventory
        item = self.find_inventory_item_by_item_id(item_id)
        # if it exists -> 
        if item:
            if item["stock"] >= quantity:
                item["stock"] = item["stock"] - quantity
                total_cost = item["unit_price"] * quantity
            
                # if the stock > the quantity asked
                # reduce the inventory 
                # then place the new order
                new_order = {
                    "order_id": str(uuid.uuid4()),
                    "item_id": item_id,
                    "quantity": quantity,
                    "status": "placed",
                    "total_cost": total_cost
                }
                self.orders.append(new_order)
                return new_order


    def find_inventory_item_by_item_id(self, item_id: str) -> Optional[Dict]:
        for item in self.inventory:
            if item.get('item_id') == item_id:
                return item
        return None
        

    def update_order_status(self):
        pass

    def cancel_order(self):
        pass

    def count_orders_for_item_by_item_id(self):
        pass