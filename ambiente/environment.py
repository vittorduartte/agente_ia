import os



matrizB = [[1,2,3],[4,5,6],[7,8,9]]

class Environment:
    
    def __init__(self, matrix):
        self.matrix = matrix
    
    def get_Position(self):
        # for line in range(len(self.matrix)):
        #     for element in range(len(self.matrix[line])):
        #         print (self.matrix[line][element])
    
env = Environment(matrizB)
print(env.get_Position())





# file.writelines(str(lista))
# file.close()