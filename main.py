from environment.environment import Environment as Ambiente
from agent.agent import Agent as Agente
from agent.actuator import Actuator as Atuador
from agent.sensor import Sensor as Sensor

Ambiente = Ambiente(6,6)
Agente = Agente(Sensor(), Atuador())

Agente.now_Alive(Ambiente)