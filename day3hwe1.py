from IPython.display import clear_output

#homework
### 1) Build a Shopping Cart <br>
#You can use either lists or dictionaries. The program should have the following capabilities:</b><br><br>
 #Takes in input 
 #Stores user input into a dictionary or list <br>
 #The User can add or delete items <br>
 #The User can see current shopping list <br>
 #The program Loops until user 'quits' <b Upon quiting the program, print out all items in the user's list 


#I will build the cart with list method

mylist = {}
shoitems = {
   'apple':2,
   'banana':3,
   'mango':4,
}
# user name input
username = input("please enter your name:")
#welcome messgage
welcomemessage = (f"welcome to my store{username}" )
#ask user if they want to proceed
letsshop = ("would you like to start shopping (yes/no): ")
while letsshop.lower() == "yes":
    start_shop = input("add your items: ")
    if start_shop in shoitems:
        howmany = int(input('How many you want:'))
        shoitems.update({start_shop:{"quantity":howmany,"subtotal":shoitems[start_shop]*howmany}})
        print(shoitems)
    else:
        print("unable to add unavailable item")
        letsshop = ("would you like to add more shopping items (yes/no): " )
    else:
print("\n")
print("****Bill Summary***** ")
print("\n")
print("Item    Quantity    SubTotal")
total=0

  for key in shoitems:
    print(f"{key}    {shoitems[key]['quantity']}        {shoitems[key]['subtotal']}")

    total = shoitems[key] ['subtotal'] + total

    print(f"Total: {total}")
  print("***********Thank You********")
  print("Hope to see you back soon!")
        




