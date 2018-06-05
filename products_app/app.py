import csv
import os



def menu(username="cvs212", products_count=20):
    menu = f"""
    -----------------------------------
    INVENTORY MANAGEMENT APPLICATION
    -----------------------------------
    Welcome {username}!
    There are {products_count} products in the database.
        operation | description
        --------- | ------------------
        'List'    | Display a list of product identifiers and names.
        'Show'    | Show information about a product.
        'Create'  | Add a new product.
        'Update'  | Edit an existing product.
        'Destroy' | Delete an existing product.
    Please select an operation: """ # end of multi- line string. also using string interpolation
    return menu

def read_products_from_file(filename="products.csv"):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"READING PRODUCTS FROM FILE: '{filepath}'")
    products = []
    with open(filepath, "r") as csv_file:
        reader = csv.DictReader(csv_file) # assuming your CSV has headers, otherwise... csv.reader(csv_file)
        for row in reader:
            #print(row["name"], row["price"])
            products.append(dict(row))
    return products

def write_products_to_file(filename="products.csv", products=[]):
    filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #print(f"OVERWRITING CONTENTS OF FILE: '{filepath}' \n ... WITH {len(products)} PRODUCTS")
    with open(filepath, "w") as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        writer.writeheader() #id,name,aisle,department,price
        for p in products:
            writer.writerow(p)


def reset_products_file(filename="products.csv", from_filename="products_default.csv"):
    print("RESETTING DEFAULTS")
    products = read_products_from_file(from_filename)
    #print(products)
    write_products_to_file(filename, products)


def list_products(products):
    #filename = "products.csv"
    #filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #products = []
    #with open(filepath, "r") as csv_file:
        #reader = csv.DictReader(csv_file)
        #for row in reader:
            #products.append(dict(row))
    print("--------------------")
    print("LISTING " + str(len(products)) + " PRODUCTS:")
    print("--------------------")
    for product in products:
        print("#" + product["id"] + ": " + product["name"])

def show_products(products):
    #filename = "products.csv"
    #filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #products = []
    #with open(filepath, "r") as csv_file:
        #reader = csv.DictReader(csv_file)
        #for row in reader:
            #products.append(dict(row))
    show_products_operation = input("Please type the identifier of the product that you want to see: ")
    matching_product = [product for product in products if product["id"] == show_products_operation]
    matching_product_index = matching_product[0]
    print(matching_product_index)


def create_products(products):
    #filename = "products.csv"
    #filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #products = []
    user_defined_name = input("Please enter the 'name' of the new product: ")
    user_defined_aisle = input("Great job. Now enter the 'aisle' of the product: ")
    user_defined_department = input("Almost done! Now enter the product's 'department': ")
    user_defined_price = input("One last step! Please enter the product's 'price': ")
    #with open(filepath, "r") as csv_file:
        #reader = csv.DictReader(csv_file)
        #for row in reader:
            #products.append(dict(row))
    created_product = {"id": len(products) + 1, "name": user_defined_name, "aisle": user_defined_aisle, "department": user_defined_department, "price": user_defined_price}
    products.append(created_product)
    print("--------------------")
    print("CREATING A NEW PRODUCT: ")
    print("--------------------")
    print(created_product)
    #with open(filepath, "w") as csv_file:
        #writer = csv.DictWriter(csv_file, fieldnames=["id", "name", "aisle", "department", "price"])
        #writer.writeheader() #id,name,aisle,department,price
        #for p in products:
            #writer.writerow(p)

def update_products(products):
    #filename = "products.csv"
    #filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #products = []
    #with open(filepath, "r") as csv_file:
        #reader = csv.DictReader(csv_file)
        #for row in reader:
            #products.append(dict(row))
    user_selected_product = input("Ok. Please select the product identifier: ")
    matching_selected_product = [product for product in products if product["id"] == user_selected_product]
    matching_selected_product_index = matching_selected_product[0]
    updated_product_id = int(user_selected_product)
    updated_product_name = input("What is the new 'name' of the product? (Currently: " + products[int(user_selected_product) - 1]["name"] + "): ")
    updated_product_aisle = input("What is the new 'aisle' of the product? (Currently: " + products[int(user_selected_product) - 1]["aisle"] + "): ")
    updated_product_department = input("What is the new 'department' of the product? (Currently: " + products[int(user_selected_product) - 1]["department"] + "): ")
    updated_product_price = input("What is the new 'price' of the product? (Currently: " + products[int(user_selected_product) - 1]["price"] + "): ")
    products[int(user_selected_product) - 1] = {"id": updated_product_id, "name": updated_product_name, "aisle": updated_product_aisle, "department": updated_product_department, "price": updated_product_price}
    print("--------------------")
    print("UPDATING PRODUCT: ")
    print("--------------------")
    print(products[int(user_selected_product) - 1])

def destroy_products(products):
    #filename = "products.csv"
    #filepath = os.path.join(os.path.dirname(__file__), "db", filename)
    #products = []
    #with open(filepath, "r") as csv_file:
        #reader = csv.DictReader(csv_file)
        #for row in reader:
            #products.append(dict(row))
    user_selected_product_destroy = input("Ok. Please put the identifier of the product that you want to destroy: ")
    matching_selected_product_destroy = [product for product in products if product["id"] == user_selected_product_destroy]
    matching_selected_product_destroy_index = matching_selected_product_destroy[0]
    print("--------------------")
    print("DESTROYING A PRODUCT: ")
    print("--------------------")
    print(products[int(user_selected_product_destroy) - 1])
    del products[int(user_selected_product_destroy) - 1]


def run():
    products = read_products_from_file()
    user_operation = input((menu(username="cvs212", products_count=len(products))))
    if user_operation == "List" or user_operation == "list":
        list_products(products)
    elif user_operation == "Show" or user_operation == "show":
        show_products(products)
    elif user_operation == "Create" or user_operation == "create":
        create_products(products)
    elif user_operation == "Update" or user_operation == "update":
        update_products(products)
    elif user_operation == "Destroy" or user_operation == "destroy":
        destroy_products(products)
    elif user_operation == "Reset" or user_operation == "reset":
        reset_products_file(products)
    else:
        print("You didn't enter a correct operation. Please select an operation from the menu.")
        return run()
    write_products_to_file(products=products)

# only prompt the user for input if this script is run from the command-line
# this allows us to import and test this application's component functions
if __name__ == "__main__":
    run()
