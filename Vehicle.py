#! /usr/bin/env python

import random
import time

class vehicle(object):
    make = "generic"
    model = "generic"
    Odometer = 0
    GasInTank = 40
    MaxGasInTank = 40
    NumberOfTurns = 0
    MaxNumberOfPassengers = 4
    CurrentNoOfPass = 1
    #Funds = 300
    LoveOfLife = False
    LengthOfTrip = random.randint(10000, 20000)
    stateOfDriver = 0
    GiveUp = 0
    zombie = 0
    DaysOfZombie = 0
    
    #defining vars
    def __init__(self):
        self.make = raw_input("What company is the maker of your car? ")
        self.model = raw_input("What kind of "+ self.make + " car is your car?[e.g. (chevy) Impala] ")
        self.NumberOfPassengers = raw_input("How many people can your car seat? ")
        LoveOfLife = raw_input("Will you take the love of your life with you on this trip?(yes or no?) ")
        if LoveOfLife.lower() == "yes":
            print "Ok, ARE YOU SURE????? Aparently you are so, NO TAKEBACKS!!\n"
        else:
            print "Ok. You are set!\n"


    def drive(self):
        time = raw_input("How long do you want to drive in hours?")
        while time > 24:
            time = int(raw_input("There are only 24 hours in the day! Re-input | "))
        while time < 0 and self.make.lower != "delorian":
            time = int(raw_input("You don't own a Delorian! Re-input | "))
        while time < 0 and self.make.lower == "delorian":
            time = int(raw_input("You don't own THE Delorian! Re-Input | "))
        zombie = random.randint(25,50)
        odometer = odometer - (time * 40)
        #def self.fill():


    def zombie_drive(self):
        time = raw_input("How long would you like to drive for? HURRY!!")
        while time > 24:
            time = int(raw_input("There are only 24 hours in the day! Re-input | "))
        while time < 0 and self.make.lower != "delorian":
            time = int(raw_input("You don't own a Delorian! Re-input | "))
        while time < 0 and self.make.lower == "delorian":
            time = int(raw_input("You don't own THE Delorian! Re-Input | "))
        odometer = odometer - (time * 80)
"""
        attack = random.randint(1,4)
        if attack = 4:
            print "Look out! A zombie is apporaching your car!"
            StartOfClock = time.time()
            print "What do you do?"
            print "\n"
            print "1| shoot it"
            print "2| hug it"
            print "3| punch it"
            HumanAttack = raw_input("What do you do? | ")
            EndOfClock = time.time()
            if EndOfClock-StartOfClock > 15 or (HumanAttack != 1 and HumanAttack != 3):
                "The zombie ate you, YOU LOSE!"
            return END == 1
            if HumanAttack = 3:
                state = random.randint(0,1)
                if state = 0:
                    print "You died..."
                    return END == 1
            if HumanAttack = 1:
                "Nice shot!"
                return END = 0
"""
#---------------Main Code--------------------------------------

car = vehicle()

print "Hello! Now that you have set up your vehicle, you will go for a road trip."
print "You got extremely drunk last night out of boredom and you wake up in your car with just enough gas to get to the closest gas station and 300$ in your pocket\n"
print "Despite the hangover you get the car full with gas, and promptly afterwards you fall asleep. The next day...\n"


while car.Odometer < car.LengthOfTrip and car.zombie != 50 and car.GiveUp != 1:
    print "You are driving a", car.make, car.model + "."
    print "You have driven", str(car.Odometer) + "\\" + str(car.LengthOfTrip) + " Km."
    #print "You have", car.GasInTank + "\\40 Gallons of gas at the moment.\n"
    print "What would you like to do?"
    print "\n\t1) Drive"
    #print "\t2) Pruchase Gasoline"
    print "\t2) give up"
    option = raw_input("|")

    while option == (1 or 2):
        if option == 1:
            car.drive()
            option == 0
        #if option = 2
        #   car.fill()
        #   return option = 0
        if option == 2:
            print "Quitter!"
            GiveUp == 1
        else:
            option = raw_input("That's not an option... | ")
if car.Odometer > car.LengthOfTrip:
    print "nice job, you managed to not crash your car"

"""
if car.zombie = 50
    print "There is a zombie outbreak! Thankfully the city you are trying to get to has a safe house!"
    print "Hurry! The speed limit is now 80 MPH, but don't get too fatigued!"

    while car.Odometer < Car.LengthOfTrip and GiveUp != 1
        print "You are driving a", car.make, car.model + "."
        print "You have driven", car.Odometer + "\\" + car.LengthOfTrip + "."
        #print "You have", car.GasInTank + "\\40 Gallons of gas at the moment.\n"
        print "What would you like to do?"
        print "\n\t1) Drive"
        #print "\t2) Pruchase Gasoline"
        print "\t3) give up"
        option = raw_input("|")

        if option = 1
            car.zombie_drive()
            return option == 0
        #if option = 2
        #    car.fill()
        #    return option = 0
        if option = 2 # change ot 3 if gasoline is implemented
            print "Quitter!"
            GiveUp == 1
"""