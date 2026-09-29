# Grocery Store Billing System

grocery_cart = []     # stores list of alll the products added by the customer.

def add_items():
    name = input("enter product name: ")
    price = float(input("enter the price of the addded product: "))          # this function stores all the product , prices, qty
    qty = float(input("enter the qty of products added : "))                   #added by the customer.

    item = {"name": name,
        "price": price,
        "qty": qty}
    
    grocery_cart.append(item)

    print("cart updated with product")

def view_items():                  #function to acces items in your cart
    if len(grocery_cart)==0:
        print("your cart is empty, add some items")
        pass

    for item in grocery_cart:
        amount = item["price"] * item["qty"]                # calculation of amount of prodcuts.


        print("items in cart: ", item["name"])
        print("price of items:", item["price"])
        print("qty of items:", item["qty"]) 
        print("amount:", amount)
            
def get_total():
    total = 0

    for item in grocery_cart:
        amount = item["price"] * item["qty"]
        total = total + amount

    return total


def add_discount(total):                    #function to add discount on the bill
    discount = 0

    if total >= 7000:
        discount = (total * 10) / 100          #  discount of 10% will be given on total amount of 7000 or above.

    elif total >= 5000:
        discount =(total* 7.5)/  100            # discount of 7.5% will be given on total of 5000 or above

    elif total >= 3000:
        discount = (total*5)/ 100               # discont of 5% will be given on total of 3000 or above

    else:
        print("congratulations! , you won a free voucher")     # a free voucher will be given for doing shopping of any amount 
                                                               # below 3000
    return discount


def final_bill():

    if len(grocery_cart) == 0:
        print("add items to calculate bill")
        return

    total = get_total()

    dicsount = add_discount(total)

    final_amount = total - dicsount
    print(final_amount)

#**************************
#    GROCERY STORE
#****************************


while True:
    print("1, add product")
    print("2. show cart")
    print("3. show total")
    print("4. cal final bill")
    print("5. exit")


    choice = int(input("enter your choice: "))

    if choice == 1:
        add_items()

    elif choice == 2:
        view_items()

    elif choice == 3:
        total = get_total()
        print(total)
       
    elif choice == 4:
        final_bill()

    elif choice == 5:
        print("thank you for shopping with us")

        break
    else:
        print("please enter a valid choice")
        

    




