"""
Micah Joshua Rahardjo
"""
def main(): #main function
    try:
        inventory = {"F01" : ["Orange","Fruit",2.99,1000] , "F02" : ["Apple","Fruit",1.99,5000],   #base dictionary
                     "F03" : ["Banana","Fruit",1.5,490] , "D01" : ["Milk","Dairy",7.5,500], 
                     "D02" : ["Cheese","Dairy",15,840] , "D03" : ["Yogurt","Dairy",5.5,700], 
                     "V01" : ["Carrot","Vegetable",3.8,890] , "V02" : ["Celery","Vegetable",3.99,990], 
                     "V03" : ["Bean","Vegetable",4.5,1500] , "V04" : ["Potato","Vegetable",6,1000]}
        menu (inventory)
    except Exception as e: #ignore error if happened
        print ("Please Enter a numeric number.")
        main()


def menu(inventory): #menu function
    choice = 0
    while choice != 10:
        print("Inventory database operations")     #menu
        print ("1. Show all items")
        print ("2. Look up the inventory")
        print ("3. Add an item to the inventory")
        print ("4. Change an item ")
        print ("5. Delete an item")
        print ("6. Find items given category")
        print ("7. Item count, average price by category")
        print ("8. Most expensive item by category")
        print ("9. Total price by item")
        print ("10. Quit the program")
        print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        choice = int(input("Please select your choice: "))

        
        if choice == 1:   #command when user enter a certain number
            showAll(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""') #separator
        elif choice == 2:
            lookUp(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        elif choice == 3:
            add(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        elif choice == 4:
            change(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        elif choice == 5:
            delete(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        elif choice == 6:
            category(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        elif choice == 7:
            itemCount(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        elif choice == 8:
            mostExpensive(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        elif choice == 9:
            totalPrice(inventory)
            print ('"""""""""""""""""""""""""""""""""""""""""""""""""')
        elif choice == 10:
            pass
        else:
            print ("-----------------------------------")
            print ("Please enter the correct number....") #if the user input other number
            print ("-----------------------------------")

    print ("Thankyou for using my menu program")
            

    
def showAll(inventory): #show all item function

    print ("---------------------------------------")
    print ("ID \tItems")
    print ("---------------------------------------")
        
    for k, v in inventory.items():
        print (k,'\t',v)

def lookUp(inventory):  #look up an item function

    ID = input("Please enter object iD: ")
    print (inventory.get(ID,"The object ID doesn't exist!"))

def add(inventory):#add an item function
    ID = input("Please enter a new object ID that you want to add: ")
    cList = ["Fruit", "Dairy", "Vegetable"]
    
    if ID not in inventory: #checks if there are an existing item id
        name = input ("Please enter the new object's name: ")
        category = input("Please enter the new object's category: ")
        while category not in cList:
            print("There are only 3 category: Fruit, Vegetable, and Dairy. Try again..")
            category = input ("Please enter the item's category: ")
        price = float(input ("Please enter the new object's price: "))
        count = int(input ("Please enter the new object's count: "))
        inventory[ID] = [name,category,price,count] #adding the item
        print ("Item added!")
    else:
        print ("ID already existed")

def change(inventory):   #change an item function
    ID = input("Please enter the object ID that you want to change: ")
    Quit = 'y'
    cList = ["Fruit", "Dairy", "Vegetable"]
    
    if ID not in inventory:
        while ID not in inventory:
            print ("The Object ID does not exist.")
            ID = input("Please Enter a valid ID: ")
    name = input ("Please enter the new object's name: ")
    category = input ("Please enter the new object's category: ")
    while category not in cList:
        print ("Invalid Category. Try again...")
        category = input ("Please enter item category: ")
    price = float(input ("Please enter the new object's price: "))
    count = int(input ("Please enter the new object's count: "))    
        
    inventory [ID] = [name,category,price,count]

    print ("Item updated!")

def delete(inventory):   #delete an item function
    ID = input("Please enter the object ID that you want to delete: ")
    Quit = 'y'
    if ID not in inventory:
        while ID not in inventory:
            print ("The Object ID does not exist.")
            Quit = input ("Do you want to try again? \n[y/n] ")
            if Quit == 'y':
                ID = input("Please enter another ID: ")
            else:
                break
    if Quit != 'n':        
        del inventory[ID]   #delete an ID

    print("Object has been deleted!")

def category(inventory):   #show all item in a category function
    category = input("Please enter the category: ")
    List = [] # a new list for the category

    for k, v in inventory.items(): #adding an item in a certain category to the list
        if v[1] == category:
            List.append(v[0])
    if List == []:
        print("The Category does not exist")
    else:
        print(List)
        
def itemCount(inventory):     #shows item name and the average price for each category
    List = []
    
    for k,v in inventory.items(): #adding all category to the new list without repetition
        if v[1] not in List:
            List.append(v[1])
    
    for n in range(len(List)): # to count the number of item name in a category
        c = 0 #item count
        for k,v in inventory.items():
            if List[n] == v[1]:
                c += 1
        print (f"{List[n]} count: {c}")

    for n in range(len(List)): # to find the average of a category
        s = 0 #item price sum
        c = 0
        for k,v in inventory.items(): #the price sum for a certain category
            if List[n] == v[1]:
                s += v[2]
        for k,v in inventory.items():
            if List[n] == v[1]:
                c += 1
        
        print (f"Average unit price of {List[n]}: {s/c}")
            
    
def mostExpensive(inventory): #shows the most expensive item in each category
    List = []

    for k,v in inventory.items():
        if v[1] not in List:
            List.append(v[1])
            
    for n in range(len(List)): # to find the most expensive item in a certain category
        List2 = []
        a = 0
        for k,v in inventory.items():
            if List[n] == v[1]:
                List2.append(v[2])
                if v[2] > a:
                    item = v[0]
                    a = v[2]
                    
        print (f"The most expensive item in the {List[n]} category is: {item} {max(List2)}")
    

def totalPrice(inventory): #shows the total price for each item
    for k,v in inventory.items():
        print (f"Item id = {k} item = {v[0]}, total price = {v[2]*v[3]}")


    
main() #execute

    
