"""
Course: PROG23199
o Assignment No.: 3
o Your Name: Micah Joshua Rharadjo
o Your Sheridan Student Id: 991687206
o Instructor’s name: Syed Tanbeer
"""

import threading
import random
import time

my_lock = threading.Lock()
storage = 0 # req 5
fed_animal = 0 # req 5

def deposit():
    """Depositing foods in random number between 1-10, on a 0.5 second interval

    Args:
        cond (method): method that is from threading.Condition
        synchronized (decorator): using in the locking mechanism

    Returns:
        int : adding the number of food in the storage
    """
    global storage
    global fed_animal
    global cond
    while True:
        time.sleep(1)
        amount = random.randint(1,10) # req 2 amount of food deposits are randomize
        my_lock.acquire()
        storage += amount
        my_lock.release()
        print(f'(+)     {amount} kg of food has been deposited')

        sentence = f'current food in storage --> {storage} kg'
        length = len(sentence)
        for x in range(0,length+1):
            print('-', end='')
        print()
        print(sentence,'|')
        for x in range(0,length+1):
            print('-', end='')
        print('\n')
        with cond:
            cond.notify_all()

        if fed_animal == n:
            break

# animal class req 7
class animal(threading.Thread):
    """Animal class for req 7

    Args:
        threading (function): inheriting from threading.Thread class

    Methods:
        __init__ : initializing the object
        get_fed : accessor for the attribute self.fed
        Micah_get_hungry : accessor for the attribute self.hungry
        get_ate : accessor for the attribute self.ate
        get_name : accessor for the attribute self.name
        run : method to start thread, objects of animals will get hungry concurently and eat if there are enough food
    """
    def __init__(self, name , amount):
        super().__init__()
        self.fed = 0 # req 4 tracking the fed animals
        self.hungry = 0
        self.ate = 0
        self.name = name
        self.amount = amount

    def get_fed(self): #accessorfor self.fed
        return self.fed
    
    def micah_get_hungry(self): #accessor for self.hungry
        return self.hungry
    
    def get_ate(self): #accessor for self.ate
        return self.ate 
    
    def get_name(self): #accessor for self.name
        return self.name

    
    def run(self):
        global storage
        global fed_animal
        global cond
            
        with cond:
            
            print (f'The {self.name} is hungry')
            self.hungry += 1 # part of req 9

            while (self.amount > storage):
                print (f'There is not enough food for {self.name}. Wait for more deposit.')
                cond.wait()
            
            my_lock.acquire()
            storage -= self.amount
            my_lock.release()

            self.ate += self.amount
            print(f'(-)     {self.amount} kg of food has been eaten by {self.name}') # req 14
            self.fed += 1
            print (f'{self.name} fed count : {self.fed}') # req 14
            fed_animal += 1
            print (f'Animal fed count : {fed_animal}') # req 14

            sentence = f'current food in storage --> {storage} kg' # req 14
            length = len(sentence)
            for x in range(0,length+1):
                print('-', end='')
            print()
            print(sentence,'|')
            for x in range(0,length+1):
                print('-', end='')
            print('\n')

def micah_object(): # req 8
    """Function to automate object initialize, having datacollection(list) to pass on other function as per say in req 8
    """
    global n
    global animal_list
    animal_dict = {'elephant': 15,'girrafe': 9, 'horse' : 5, 'zibra': 5, 'deer': 3}
    animal_list = []
    lists = [num for num in range(n)]

    for num in range(n):
        name , food = random.choice(list(animal_dict.items())) 
        lists[num] = animal(name, food)
        animal_list.append(lists[num])        

def start_object(list, de):
    """Function to automate start threads

    Args:
        list (list): The animal list that were made by micah_object function
    """

    de.start()

    for k in list:
        k.start()
        k.join()

    de.join()

def new_dict(list):
    """
    Making a new dictionary so it looks better

    Args:
        list (list): fed animal list (animal_list)

    Returns:
        dictionary : dictionary with metadata = name : [consumed food, Hungry count, Fed count]
    """
    new_dict = {}
    foodE = 0
    hungryE = 0
    ateE = 0
    foodG = 0
    hungryG = 0
    ateG = 0
    foodH = 0
    hungryH = 0
    ateH = 0
    foodZ = 0
    hungryZ = 0
    ateZ = 0
    foodD = 0
    hungryD = 0
    ateD = 0

    for k in list:
        if k.get_name() == 'elephant':
            foodE += 15
            hungryE += 1
            ateE += 1
            new_dict['elephant'] = [foodE, hungryE, ateE]
        elif k.get_name() == 'girrafe':
            foodG += 9
            hungryG += 1
            ateG += 1
            new_dict['girrafe'] = [foodG, hungryG, ateG]
        elif k.get_name() == 'horse':
            foodH += 5
            hungryH += 1
            ateH += 1
            new_dict['horse'] = [foodH, hungryH, ateH]
        elif k.get_name() == 'zibra':
            foodZ += 5
            hungryZ += 1
            ateZ += 1
            new_dict['zibra'] = [foodZ, hungryZ, ateZ]
        else:
            foodD += 3
            hungryD += 1
            ateD += 1
            new_dict['deer'] = [foodD, hungryD, ateD]

    return new_dict


def micah_highest_consumed(dict): #req 10
    """function to determine the highest consumer of all

    Args:
        dict (dictionary): new dictionary that were made in new_dict

    Returns:
        string:  the name of animal that consumes the heaviest food
    """
    ate_dict = {}
    
    for k, v in dict.items():
        ate_dict[k] = v[1]

    x = max(ate_dict, key=ate_dict.get)
    return x

def micah_hungriest_animal(dict): #req 9
    """Function to determine the hungriest animal

    Args:
        dict (dictionary): new dictionary that were made in new_dict
    Returns:
        string:  The name of animal that has the highest hungry count
    """
    hungry_dict = {}

    for k, v in dict.items():
        hungry_dict[k] = v[1]

    x = max(hungry_dict, key=hungry_dict.get)
    return x

def total_food_consumed(dict):
    """Function to calculate the total of food that were consumed

    Args:
        dict (dictionary): new dictionary that were made in new_dict

    Returns:
        int:  The total weight of food that were consumed
    """
    food_eaten = []
    total = 0

    for k,v in dict.items():
        food_eaten.append(v[0])

    for x in food_eaten:
        total += x

    return total

if __name__ == '__main__':

    """Main Thread to run functions and provide output
    """
    #input
    print('\t\t\t Zoo Animal Feeding') #header req 12
    print('\t\t\tMicah Joshua Rahardjo')
    print('\t\t\t    991-687-206')
    print ('\t   --------------- Start Feeding ---------------')
    print('')
    z = lambda a : a*1
    n = z(*map(int,input("Please enter the number of animals to be fed =  ").split()))# input to when to stop req 6 and req 13


    #process
    cond = threading.Condition()
    animal_list = []

    de = threading.Thread(target=deposit)
    micah_object()
    start_object(animal_list,de)

    new_dictionary = new_dict(animal_list)
    

    highest_consumed = micah_highest_consumed(new_dictionary) # req 15
    hungriest = micah_hungriest_animal(new_dictionary)
    total = total_food_consumed(new_dictionary)

    # Output
    
    print(f'%%%%%%%%%%%%%%%%%%%%%%% SUMMARY %%%%%%%%%%%%%%%%%%%%%%%')
    print('')
    for k, v in new_dictionary.items():
        print(f'{k} got hungry {v[1]} time(s), fed {v[2]} time(s), consumed {v[0]} kg')
    print (f'The animal {highest_consumed} consumed the most')
    print (f'The animal {hungriest} was the hungriest')
    print (f'The total food that were consumed {total} kg')
