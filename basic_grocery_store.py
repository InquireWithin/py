"""
#data type, access/update, insert/delete, orderable?, elements unique?
Array, o(c), o(n), yes, no
List, o(c), o(n), yes, no
Dict, o(c), o(c), (no for python <3.6, yes for python >3.7), (Keys = yes, values = no)
Set, o(c), o(c), no, Yes
Stack, o(c), o(c), Yes, no
Queue, o(c), o(c), yes, no
"""
import random
import math
import array_utils
import arrays
import node_stack
import array_queue
#create a class for a grocery store item, every item has a name (ex. Item#7),
#a price between 1 and 20$, and a weight between one and 10 pounds
class Item:
    __slots__ = ["__name", "__price", "__weight"]
    def __init__(self, name, price, weight):
        self.__name = name
        self.__price = price
        self.__weight = weight
    def get_name(self):
        return self.__name
    def get_price(self):
        return self.__price
    def get_weight(self):
        return self.__weight

    def set_name(self, label):
        self.__name = label
    def set_price(self, val):
        self.__price = val
    def set_weight(self, amount):
        self.__weight = amount

    #add the ability to get a string representation of the grocery item including all attributes
    def __str__(self):
        return self.__name + ", $" + str(self.__price) + ", " + str(self.__weight) + " lbs"

    def __repr__(self):
    
        return "Grocery Item: " \
            + "\n name=" + self.__name \
            + "\n price=$" + str(self.__price) \
            + "\n weight=" + str(self.__weight) + " lbs"
    #allow two items to be compared
    def __eq__(self, other):
        return self.__name == other.__name and \
            self.__price == other.__price and \
            self.__weight == other.__weight
    #provide support for using grocery items in a set or as keys in a dict
    def __hash__(self):
        return hash(self.__name) * self.__price * self.__weight
        #or use return hash(self.__str())
    #enable sorting of items by name
    def __lt__(self, other):
        return self.__name < other.__name
def fill_store():

#creates a data structure to represent the store, and fills it
#100 grocery items. the customer needs to be able to quickly find an item using only its name
    store = dict()
    for number in range(1, 101):
        name = "item #" + str(number)
        weight = random.randint(1, 10)
        price = random.randint(1, 20)
        item = Item(name, price, weight)
        store[name] = item
    return store

class Customer:
    __slots__ = ["__shopping_list", "__cart", "__bags"]
    def __init__(self, cart, bags, shopping_list):
        self.__cart = set() #set
        self.__bags = [] #list
        self.__shopping_list = shopping_list #list

    def get_bags(self):
        return self.__bags
    def get_cart(self):
        return self.__cart
    def get_list(self):
        return self.__shopping_list

    def shop(self, store):
        #find each of the items on the customer's list and add it to their cart
        _list = self.__shopping_list
        for name in _list:
            if name in store:
                item = store[name]
                self.__cart.add(item)

    def unload(self, belt): #belt should be a queue

        #unload all of the items from the cart onto the cashier belt
        #return that belt
        for item in self.__cart:
            belt.enqueue(item)

    def add_bag(self, bag):
        #add it to customer
        #return?
        new_bag = node_stack.Stack()
        self.__bags.append(new_bag)
def make_shopping_list(store):
    all_items = []
    for name in store:
        all_items.append(name)
    random.shuffle(all_items)
    shopping_list = all_items[:25]
    #customer = Customer(all_items, [], shopping_list)
    return shopping_list
def pack(customer, belt):
    #simulate a cashier packing customers items into bags
    #cashier will pack items ne on top of the other
    #as long as thenext item to be packed has a weight that is less than or equal to it
    #use a stack for a bag

    #implementation:
    #for every item on the belt
    #if item.get_weight() > max_weight:
    #   max_weight = item.get_weight()
    #   max_weight_item = item
    
    #as long as there is at least one more item in the belt remove the next item
    #if the item at the top of the current bag has a weight that is equal or heavier than this item,
    #pack it into the bag
    #if the new item is heavier, make a new bag and pack it into that bag
    #at some point the bags need to be added to the customer
    bag = node_stack.Stack()
    customer.add_bag(bag)
    while not belt.is_empty():
        item = belt.dequeue()
        if bag.is_empty():
            bag.push(item)
        else:
            top_item = bag.peek()
            if item.get_weight() <= top_item.get_weight():
                bag.push(item)
            else:
                bag = node_stack.Stack()
                customer.add_bag(bag)
                bag.push(item)

def unpack(customer):
    #unpack each of the customer's bags and print the items as they are unpacked
    bags = customer.get_bags()
    number = 0
    for bag in bags:
        number +=1
        print("unpacking bag #", number, sep="")
        while not bag.is_empty():
            item = bag.pop()
            print(" ", item)

def main():
    store = fill_store()
    shopping_list = make_shopping_list(store)
    #print(shopping_list)
    cart = set()
    bags = []
    customer = Customer(cart, bags, shopping_list)
    customer.shop(store)
    print(customer.get_cart())
    belt = array_queue.Queue()
    customer.unload(belt)
    #print(belt.size(), belt)
    pack(customer, belt)
    bags = customer.get_bags()
    for bag in bags:
        print(bag)
    unpack(customer)
    # for name in store:
    #     item = store[name]
    #     print(item)

    # item1 = Item("Item #1", 10, 1)
    # item2 = Item("Item #2", 1, 10)
    # print(item1)
    # print(repr(item1))
    # print(hash(item1))
    # print(item1 < item2)
    # print(item1 == item2)
if __name__ == "__main__":
    main()