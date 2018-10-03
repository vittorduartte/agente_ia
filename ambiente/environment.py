import os
import random

class Environment:
    
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def generate_Environment(self):
        
        environment = []

        for i in range(self.length):
            listaux = []
            for j in range(self.width):
                listaux.append(random.randrange(2))
            environment.append(listaux)

        return environment
    

# env = Environment(10,10).generate_Environment()

# for i in range(len(env)):
#     for j in range(len(env[i])):
#         if env[i][j] == 0:
#             print('[Linha: ', i+1, ' - Coluna: ',j+1,', Limpo]\n')
#         else:
#             print('[Linha: ', i+1, ' - Coluna: ',j+1,', Sujo]\n')

