'''
This Code Uses a Hidden API from DMarket To get the buyers order!
Please Respect The LICENSE of This Repository!
Remember This is an unofficial DMarket Bot, please respect the DMarket Terms of Service
Use this code at your own risk
Developers are advised to review DMarket's terms of service before using this software
Thanks Hope You Use This Repository Well!
'''

import requests
from datetime import datetime
from urllib.parse import quote

item_name = "AUG | Chameleon (Factory New)"  # PUT HERE THE NAME OF THE ITEM
root = "https://api.dmarket.com"
endpoint = f"/order-book/v1/market-depth?title={quote(item_name)}&gameId=a8db&filters=floatPartValue%5B%5D=any"  # Theres another endpoint, if this one doesn't give the right value try this one, f"/order-book/v1/market-depth?title={quote(item_name)}&gameId=a8db&filters=phase%5B%5D=any,floatPartValue%5B%5D=any"
url = root + endpoint

def use_API():
        params = {}
            
        timestamp = int(datetime.now().timestamp())
        
        headers = {
                'X-Sign-Date': str(timestamp),
                'X-Request-Sign': 'PUT HERE YOUR SIGNATURE'
            }

        response = requests.get(url, headers=headers, params=params)
        offers_names = response.json()  # Gets the API response
        extracted_data = [{'price': obj['price']} for obj in offers_names['orders']]  # Takes the buyers orders prices from the response
        organized_data = extracted_data[0]  # Gets the highest buyers order
            
        return f"Highest Price: {organized_data}\n All Buyers Orders: {extracted_data}"
    
print("\n", use_API(), "\n")
