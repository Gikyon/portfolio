
import csv

with open ("Items_Micah.csv", "w", newline='') as file:
    field_name = ["iid","name","category","price"]
    writer = csv.DictWriter(file, fieldnames=field_name)

    content = [
        {"iid" : 1,"name" : "Banana","category" : "Fruit","price" : 0.60},
        {"iid" : 2 ,"name" : "Orange","category" : "Fruit","price" : 1.25},
        {"iid" : 3 ,"name" : "Beef","category" : "Meat","price" : 5.25},
        {"iid" : 4,"name" : "Milk","category" : "Dairy","price" : 5.50},
        {"iid" : 5 ,"name" : "Carrot","category" : "Vegetable","price" : 1.10},
        {"iid" : 6 ,"name" : "Beans","category" : "Vegetable","price" : 2.75},
        {"iid" : 7,"name" : "Chicken","category" : "Meat","price" : 3.45},
        {"iid" : 8 ,"name" : "Chips","category" : "Snacks","price" : 2.00},
        {"iid" : 9 ,"name" : "Cookies","category" : "Snacks","price" : 5.60},
        {"iid" : 10,"name" : "Cheese","category" : "Dairy","price" : 7.85}
    ]
    writer.writeheader()
    writer.writerows(content)
