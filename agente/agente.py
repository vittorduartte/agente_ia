import os
from datetime import datetime 

 #   def analisa_Estados(self):
        
    #     list_state = []

    #     for line in range(len(self.environment)):
            
    #         for column in range(len(self.environment[line])):
                
    #             if  self.environment[line][column] == 0:
                    
    #                 aux = self.environment[line][column]
    #                 self.environment[line][column] = 'x'

    #                 # log = '[ Posição: ' + str(line) +' x '+str(column)+' - '+' Limpo ]'
    #                 # list_state.append(log)

    #                 print(self.environment)
    #                 self.environment[line][column] = aux                      
                    
    #             else:

    #                 aux = self.environment[line][column]
    #                 self.environment[line][column] = 'x'

    #                 # log = '[ Posição: ' + str(line) +' x '+str(column)+' - '+' Sujo ]'
    #                 # list_state.append(log)
                    
    #                 print(self.environment)
    #                 self.environment[line][column] = aux
                    

    #     return list_state

class Sensor:
    
    def __init__(self, actually):
        self.actually = actually

    def current_State(self):
        
        if self.actually == 0:
            return False
        
        else:
            return True


class Actuator:

    def __init__(self, environment):
        self.environment = environment
        
    def clean_Frame(self):
        self.environment == 0
        return self.enviroment

    def next_Frame(self):
        return self.environment

class Agente:

    def __init__(self, environment, sensor, actuator):
        self.environment = environment
        self.sensor = sensor
        self.actuator = actuator

    def in_activity(self):

        for line in range(len(self.environment)):
            
            for column in range(len(self.environment[line])):

                    if self.sensor.current_State(self.environment[line][column]):
                        
                        result = self.actuator.clean_Frame(self.environment[line][column])
                    
                    else:

                        result = self.actuator.next_Frame(self.environment[line][column])

        return result

    def generate_Log_Status(list_state):
        now = datetime.now()
        now = now.strftime('%d/%m/%Y_%H:%M:%S')
        log = open('log'+now,'w+')
        log.writelines(str(list_state))
        log.close()
        return "O log foi gerado com sucesso!"
