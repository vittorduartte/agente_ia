
class Actuator:

    def __init__(self):
        pass

    def clean_Here(self, line, column, env):
        output = env.as_List()
        output[line][column] = 0
        return output
