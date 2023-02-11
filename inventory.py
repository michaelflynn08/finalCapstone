from tabulate import tabulate
#========The beginning of the class==========
class shoes:
    # we initilise the shoe object below. we turn cost and quantity into an integer so it works with functions later.
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = int(cost)
        self.quantity = int(quantity)
    
    def get_cost(self):
        
        return self.cost
       

    def get_quantity(self):
        
        return self.quantity
       

    def __str__(self):
        
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}" 
    
    def __repr__(self):
        
        return f"{self.country},{self.code},{self.product},{self.cost},{self.quantity}"

    



#=============Shoe list===========

shoe_list = []

#==========Functions outside the class==============
# here we creae a function which reads the lines in the file and for each line creates a Shoes class objective. 
# it then appends the objectives to the shoe list.
def read_shoes_data():
    with open("inventory.txt","r") as r:
        for line in r.readlines()[1:]:
            country, code, product, cost, quantity = line.split(",")
            shoe_list.append(shoes(country, code, product, cost, quantity))
    
# with this function we are creating a new shoe object. 
# after input from the user we add this object to the shoe_list and the invetory file.    
def capture_shoes():
    new_country = input("what is the country :")
    new_code = input("what is the 5 digit product code :")
    new_product = input("what is the name of this product :")
    new_cost = int(input("how much does a pair of these shoes cost :"))
    new_quantity = int(input("how many of these shoes are in stock :"))
    new_code = "SKU" + new_code  
    shoe_list.append(shoes(new_country, new_code, new_product, new_cost, new_quantity))
    with open("inventory.txt","a") as w:
        w.write(str(shoes("\n" + new_country, new_code, new_product, new_cost, new_quantity)))
   
# the view all function lets the user view all the stock in an easy to read table using tabulate
def view_all():
    
    print(tabulate([(shoe.country, shoe.code, shoe.product, shoe.cost, shoe.quantity)for shoe in shoe_list], 
    headers=['country', 'code', 'product', 'cost', 'quantity']))


# for this function for every object in the list we check if it is below the current lowest quantity.
# if it is that becomes the lowest number. we then check this for every item.
# leaving us with the product that needs restocking at the end and the option to restock
def re_stock():
    global shoe_list
    usefull_num = float('inf')
    useful_product = ""
    for shoe in shoe_list:
        if shoe.quantity <= usefull_num:
            usefull_num = shoe.quantity
            useful_product = shoe.product

    print("\nthere are only " + str(usefull_num) + " " + useful_product + " remaining")
    r_stock = input("would you like to restock 50 pairs of this shoe? enter y for yes, n for no :")
    if r_stock.lower() == "y":
        for shoe in shoe_list:
            if shoe.product == useful_product:
                shoe.quantity = shoe.quantity + 50      
        shoe_data = ( ", ".join( repr(e) + "\n" for e in shoe_list ) )
        shoe_replace = shoe_data.replace(", ", "")
        print(shoe_replace)
        
        
        with open("inventory.txt","w") as s:
            s.write("Country,Code,Product,Cost,Quantity\n" + shoe_replace )
    
    elif r_stock.lower() == "n":
        print("\nwill not restock\n")
    
    else:
        print("\ninvalid input please try again!\n")


# here we have the user enter a 5 digit product code. 
# this will search for the shoe based on this code and print out the matching object.
def seach_shoe():
    search_code = int(input("please enter the 5 digit code of the product you would like to select :"))
    search_code = "SKU" + str(search_code)
    print(search_code)
    match_found = False
    for shoe in shoe_list:
        if shoe.code == search_code:
            print("\n" + str(shoe) + "\n")
            match_found = True    
    if match_found == False:
        print("no match found. please try again!\n")
   
# below we find the value of every shoe by multiplying the cost per shoe by the quantity.
# we then add this information to a list then tabulate the list so its easy to read for the user
item_value = []
def value_per_item():
    for shoe in shoe_list:
        shoe_value = shoe.cost * shoe.quantity
        item_value.append(shoe.product + "," + str(shoe_value))
    
    print(tabulate([(item.split(","))for item in item_value], headers=['product', 'value']))

# this function is the exact same as the lowest_quant but finding the highest.
def highest_qty():
    highest_usefull_num = 0
    highest_useful_product = ""
    for shoe in shoe_list:
        if shoe.quantity >= highest_usefull_num:
            highest_usefull_num = shoe.quantity
            highest_useful_product = shoe.product

    print("\nthere are " + str(highest_usefull_num) + " " + "'" + highest_useful_product + "'")
    print(highest_useful_product + " is for sale!\n")
   

#==========Main Menu=============
menu = ""

while menu == "":
    read_shoes_data()
    menu = input('''select one of the following options below
c - capture_shoe
va - view all
r - restock
s - search shoe
v - value
x - find sale
e - exit
: ''').lower()

    if menu == "c": 
        capture_shoes()
        menu = ""
    elif menu == "va": 
        view_all()    
        menu = ""

    elif menu == "r": 
        re_stock()
        menu = ""
    
    elif menu == "s": 
        seach_shoe()
        menu = ""
    elif menu == "v": 
        value_per_item()
        menu = ""
    
    elif menu == "x": 
        highest_qty()
        menu = ""

    elif menu == "e": 
        print("\ngoodbye!\n")

    else:
        print("invalid input please try again\n")
        menu = ""



