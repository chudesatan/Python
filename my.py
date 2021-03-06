#!/usr/bin/python3
# -*- coding: utf-8 -*-
class Animal:

    name = ""
    weight = 0
    typesList = [ ["Cow", "milk", "muu"], ["Sheep", "wool", "bee"], ["Hen", "eggs", "kokoko"], ["Goose", "eggs", "Ga-ga"], ["Duck", "eggs", "krya"], ["Goat", "milk", "bee"] ]

    def setName(self, name):
        self.name = name
   
    def setWeight(self, weight):
        self.weight = weight
    
    def getName(self):
        return self.name
    
    def getWeight(self):
        return self.weight
        
    def toFeed(self):
        print("eating")

class HomeAnimal(Animal):
    def __init__(self, t, n, w):
        self.types = t
        self.name = n
        self.weight = w
        for t in self.typesList:
            if (t[0] == self.types):
                self.types = t
                print(self.types[0], self.types[1])
    def krik(self):
        print(self.types[2])
        
if __name__ == '__main__':

    animals = []
    animals.append(HomeAnimal("Cow", "Манька", 150))
    animals.append(HomeAnimal("Sheep", "Барашек", 50))
    animals.append(HomeAnimal("Sheep", "Кудрявый", 60))
    animals.append(HomeAnimal("Goat", "Рога", 30))
    animals.append(HomeAnimal("Goat", "Копыта", 35))
    animals.append(HomeAnimal("Duck", "Кряква", 5))
    animals.append(HomeAnimal("Goose", "Серый", 7))
    animals.append(HomeAnimal("Goose", "Белый", 8))
    animals.append(HomeAnimal("Hen", "Ко-Ко", 3))
    animals.append(HomeAnimal("Hen", "Кукареку", 2))
    allWeight = 0
    maxWeightAnimalCount = 0
    maxWeightAnimalName = ""
    for animal in animals:
        animal.krik()
        allWeight += animal.getWeight()
        if animal.getWeight() > maxWeightAnimalCount:
          maxWeightAnimalName = animal.getName()
          maxWeightAnimalCount = animal.getWeight()
           
    print("Общий вес:")
    print(allWeight)
    print("Самое тяжелое животное:")
    print(maxWeightAnimalName, maxWeightAnimalCount)
