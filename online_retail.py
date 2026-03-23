import pandas as pd
import numpy as np
from datetime import datetime

class OnlineRetailSystem:
    def __init__(self):
        # 1. Real-time inventory management
        self.inventory = {
            'item_001': {'name': 'Laptop', 'stock': 50, 'base_price': 1000, 'demand_factor': 1.0, 'competitor_price': 950},
            'item_002': {'name': 'Smartphone', 'stock': 150, 'base_price': 500, 'demand_factor': 1.2, 'competitor_price': 520},
            'item_003': {'name': 'Headphones', 'stock': 10, 'base_price': 100, 'demand_factor': 2.0, 'competitor_price': 90},
        }
        
        # 2. Personalized recommendations (mock data)
        self.user_profiles = {
            'user_1': {'browsing_history': ['item_001', 'item_003'], 'purchase_patterns': ['electronics']},
            'user_2': {'browsing_history': ['item_002'], 'purchase_patterns': ['mobile']}
        }

    def dynamic_pricing(self, item_id):
        """
        Adjusts prices based on demand, competitor pricing, and inventory levels.
        """
        item = self.inventory.get(item_id)
        if not item:
            return None
        
        price = item['base_price'] * item['demand_factor']
        
        # Adjust for inventory levels (scarcity)
        if item['stock'] < 20:
            price *= 1.15  # 15% increase due to low stock
            
        # Adjust related to competitor pricing
        if price > item['competitor_price']:
            price = max(item['competitor_price'] * 0.98, item['base_price'] * 0.9) 
            
        return round(price, 2)

    def personalized_recommendations(self, user_id):
        """
        Deliver tailored recommendations by analyzing browsing history and purchase patterns.
        """
        user = self.user_profiles.get(user_id)
        if not user:
            return []
            
        recommendations = []
        if 'item_001' in user['browsing_history']:
            recommendations.append({'item': 'item_003', 'reason': 'Customers who bought Laptops also bought Headphones'})
            
        if 'electronics' in user['purchase_patterns']:
            recommendations.append({'item': 'item_002', 'reason': 'Based on your interest in electronics'})
            
        return recommendations
        
    def manage_inventory(self, item_id, quantity_sold):
        """
        Dynamically manage inventory levels in real-time, optimizing stock levels and replenishment.
        """
        item = self.inventory.get(item_id)
        if not item:
            return False
            
        item['stock'] -= quantity_sold
        print(f"Sold {quantity_sold} of {item['name']}. Remaining stock: {item['stock']}")
        
        # Replenishment
        if item['stock'] < 20:
            print(f"ALERT: Stock for {item['name']} is low! Triggering replenishment schedule...")
            item['stock'] += 100
            print(f"Restocked 100 units. New stock of {item['name']}: {item['stock']}")
            
        return True

def main():
    system = OnlineRetailSystem()
    df_inventory = pd.DataFrame.from_dict(system.inventory, orient='index')
    print("Initial Inventory:")
    print(df_inventory[['name', 'stock', 'base_price']])
    print("\n" + "="*40 + "\n")
    
    print("1. Dynamic Pricing Strategy:")
    for item_id in system.inventory.keys():
        current_price = system.dynamic_pricing(item_id)
        print(f"Item: {system.inventory[item_id]['name']} | Computed Dynamic Price: ${current_price}")
        
    print("\n" + "="*40 + "\n")
    print("2. Personalized Recommendations:")
    for user_id in system.user_profiles.keys():
        recs = system.personalized_recommendations(user_id)
        print(f"User {user_id} Recommendations: {recs}")
        
    print("\n" + "="*40 + "\n")
    print("3. Real-Time Inventory Management:")
    print("Simulating a transaction: Selling 8 Headphones (Item 003)...")
    system.manage_inventory('item_003', 8)

if __name__ == "__main__":
    main()
