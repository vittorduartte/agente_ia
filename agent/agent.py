import os
from datetime import datetime 

class Agent:

    def __init__(self, sensor, actuator):
        self.sensor = sensor
        self.actuator = actuator

    def now_Alive(self, env):

        for line in range(len(env.as_List())):
            
            for column in range(len(env.as_List()[line])):

                if self.sensor.current_State(env.as_List()[line][column]):
                    
                    print('Estado Atual: SUJO')
                    print('\nLocal: ' + str(line+1) + 'x' + str(column+1) + '\nAção: LIMPAR')
                    now = self.actuator.clean_Here(line, column, env)
                    env.update_Now(now)
                    
                else:
                    print('Estado Atual: LIMPO')
                    print('\nLocal: ' + str(line+1) + 'x' + str(column+1) + '\nAção: MOVER')
                    pass
                
        pass

    