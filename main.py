from ambiente import environment as env
from agente import agente as agt

ambiente = env.Environment(4,4).generate_Environment()

agente = agt.Agente( ambiente, 
agt.Sensor(ambiente),
agt.Actuator(ambiente) )

result = agente.in_activity()
