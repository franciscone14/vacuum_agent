from agents import (Agent, Thing, Environment)

class LittleDirty(Thing):
    pass

class LotDirty(Thing):
    pass

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

    def clean(self, thing):
        if isinstance(thing, LittleDirty):
            return True
        return False

    def wash(self, thing):
        if isinstance(thing, LotDirty):
            return True
        return False

class Rooms(Environment):

    def percept(self, agent):
        '''return a list of things that are in our agent's location'''
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
                    self.delete_thing(items[0]) #Delete it from the Room.
        elif action == "wash":
            items = self.list_things_at(agent.location, tclass=LotDirty)
            if len(items) != 0:
                if agent.wash(items[0]): # Have the agent cleaned the room ?
                    print("Vacuum decided to wash the room {}.".format(agent.location))
                    self.delete_thing(items[0]) #Delete it from the Room.

def program(percepts):
    '''Returns an action based on the dog's percepts'''
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

rooms.run(10)
