
# Modification date: Thu Jan 30 22:21:44 2020

# Production date: Sun Sep  3 15:43:43 2023

class Hooman:
    def __init__(self, name, health, armor, power, stamina):
        self.name = name
        self.health = health
        self.armor = armor
        self.power = power
        self.stamina = stamina

Jason = Hooman("Jason", 100, 50, 100, 200/100)
Jackson = Hooman("Jackson", 200, 0, 50, 150/100)

def savaş(x,y):
    while x.health > 0 or y.health > 0:
        if int(x.armor) > 0:
            int(y.power) - int(x.armor)
            if int(x.armor) > 0:
                int(x.health) - int(y.power/2)
            print(y.name + " karakteri " + x.name + " karakterine saldırdı! Kalan can: " + str(x.health) + " Kalan zırh: " + str(x.armor) + ".")
            int(x.power/2) - int(y.health)
            print(y.name + " karakteri " + x.name + " karakterine saldırdı! Kalan can: " + str(x.health) + " Kalan zırh: " + str(x.armor) + ".")
        elif int(x.armor) < 0:
            int(x.health) - int(y.power)
            print(y.name + " karakteri " + x.name + " karakterine saldırdı! Kalan can: " + str(x.health) + " Kalan zırh: " + str(x.armor) + ".")
            if x.health < 0:
                print("Oyunu " + y.name + " kazandı!")
                input("Bitti.")
                break


        if int(y.armor) > 0:
            int(x.power) - int(y.armor)
            if int(y.armor) > 0:
                int(y.health) - int(x.power/2)
            print(x.name + " karakteri " + y.name + " karakterine saldırdı! Kalan can: " + str(y.health) + " Kalan zırh: " + str(y.armor) + ".")
            int(x.power/2) - int(y.health)
            print(x.name + " karakteri " + y.name + " karakterine saldırdı! Kalan can: " + str(y.health) + " Kalan zırh: " + str(y.armor) + ".")
        elif int(y.armor) < 0:
            int(y.health) - int(x.power)
            print(x.name + " karakteri " + y.name + " karakterine saldırdı! Kalan can: " + str(y.health) + " Kalan zırh: " + str(y.armor) + ".")
            if y.health < 0:
                print("Oyunu " + x.name + " kazandı!")
                input("Bitti.")
                break
                




print(savaş(Jason, Jackson))