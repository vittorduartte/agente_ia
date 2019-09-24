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
    
    def __init__(self, world_visible):
        self.world_visible = world_visible

    def current_State(self, right_now):
        
        if right_now == 0:
            return False

        else:
            return True


class Actuator:

    def __init__(self, env):
        self.env = env
        
    def clean_Here(self, here):
        self.env[here] = 0
        return self.env

class Agent:

    def __init__(self, sensor, actuator):
        self.sensor = sensor
        self.actuator = actuator

    def now_Alive(self):

        for line in range(len(self.sensor.world_visible)):
            
            for column in range(len(self.sensor.world_visible[line])):

                    if self.sensor.current_State(self.sensor.world_visible[line][column]):
                        
                        self.actuator.clean_Here(self.environment[line][column])
                        
                        self.

                    
                    else:

                        result = self.actuator.next_Frame(self.environment[line][column])

        return result

    # def generate_Log_Status(list_state):
    #     now = datetime.now()
    #     now = now.strftime('%d/%m/%Y_%H:%M:%S')
    #     log = open('log'+now,'w+')
    #     log.writelines(str(list_state))
    #     log.close()
    #     return "O log foi gerado com sucesso!"
