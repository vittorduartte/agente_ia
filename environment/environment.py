import os
import random

class Environment:
    
    def __init__(self, length, width):
        
        self.length = length
        self.width = width
        self.env = []
        
        for i in range(length):
            listaux = []
            for j in range(width):
                listaux.append(random.randrange(2))
            self.env.append(listaux)

    def view_All_States(self):
        
        for i in self.env:
            print(i)

    def as_List(self):
        
        return list(self.env)
    
    def update_Now(self, new):
        self.env = new
        pass


