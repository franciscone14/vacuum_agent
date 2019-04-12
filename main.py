# Importando bibliotecas do aima-python
from agents import (Agent, Thing, Environment)

# Classe que representa pouca sujeira
class LittleDirty(Thing):
    pass

# Classe que representa muita sujeira
class LotDirty(Thing):
    pass

# Agente
class RandomVacuumAgent4Places(Agent):
    location = "A"

    def move(self):
        if self.location == "A":
            self.location = "B"
        elif self.location == "B":
            self.location = "C"
        elif self.location == "C":
            self.location = "D"
        elif self.location == "D":
            self.location = "A"

    # Limpa se for pouca sujeira
    def clean(self, thing):
        if isinstance(thing, LittleDirty):
            return True
        return False

    # Lava se for muita sujeira
    def wash(self, thing):
        if isinstance(thing, LotDirty):
            return True
        return False

# Ambiente
class Rooms(Environment):

    def percept(self, agent):
        '''Retorna uma lista de coisas que estão no local do agente'''
        return self.list_things_at(agent.location)

    def execute_action(self, agent, action):
        if action == "move":
            print('Vacuum decided to {} at location: {}'.format(action, agent.location))
            agent.move()
        elif action == "clean":
            items = self.list_things_at(agent.location, tclass=LittleDirty)
            if len(items) != 0:
                if agent.clean(items[0]): # Have the agent cleaned the room ?
                    print("Vacuum decided to vacuum the room {}.".format(agent.location))
                    self.delete_thing(items[0]) # Delete it from the Room.
        elif action == "wash":
            items = self.list_things_at(agent.location, tclass=LotDirty)
            if len(items) != 0:
                if agent.wash(items[0]): # Have the agent cleaned the room ?
                    print("Vacuum decided to wash the room {}.".format(agent.location))
                    self.delete_thing(items[0]) # Delete it from the Room.

def program(percepts):
    '''Retorna a ação baseado no estado de sujeira da sala'''
    for p in percepts:
        if isinstance(p, LittleDirty):
            return 'clean'
        elif isinstance(p, LotDirty):
            return 'wash'
    return 'move'

rooms = Rooms()
ag = RandomVacuumAgent4Places(program)
rooms.add_thing(ag, "A")
rooms.add_thing(LittleDirty(), "A")
rooms.add_thing(LotDirty(), "C")
rooms.add_thing(LittleDirty(), "B")
rooms.add_thing(LotDirty(), "B")
rooms.add_thing(LittleDirty(), "A")
rooms.add_thing(LotDirty(), "D")

rooms.run(10)
