"""
generate random products and print a summary of them
"""

from acme import Product
import random

adj = ['Awesome', 'Shiny', 'Impressive',
    'Portable', 'Improved']
noun = ['Anvil', 'Catapult' 'Disguise' 'Mousetrap', '???']

def generate_products(num_products=30):
    products = []
    for i in range (30):
        products.append((i, {
        'name': (random.choice(adj) + " " + random.choice(noun)),
        'price': random.randint(5, 100),
        'weight': random.randint(5, 100),
        'flammability': random.uniform(0.0, 2.5)
        }))
    return products

def inventory_report(products):
    names = [] 
    for product in range(len(products)):
        names.append(products[product][1]['name'])
    prices = [] 
    for product in range(len(products)):
        prices.append(products[product][1]['price'])
    weights = []
    for product in range(len(products)):
        weights.append(products[product][1]['weight'])
    flammabilities = []
    for product in range(len(products)):
        flammabilities.append(products[product][1]['flammability'])

    message = ("ACME CORPORATION OFFICIAL REPORT \n")
    nunique = len(set(names))
    avg_price = sum(prices)/len(prices)
    avg_weight = sum(weights)/len(weights)
    avg_flammability = sum(flammabilities)/len(flammabilities)

    return message, nunique, avg_price, avg_weight, avg_flammability

if __name__ == '__main__':
    inventory_report(generate_products())
