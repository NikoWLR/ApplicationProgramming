# define list
instruction_list = []


# defining get last id
def get_last_id():
    if instruction_list:
        last_instruction = instruction_list[-1]
    else:
        return 1
    return last_instruction.id + 1


# Instruction class and properties
class Instruction:
    def __init__(self, name, description, steps, tools, cost, duration):
        self.id = get_last_id()
        self.name = name
        self.description = description
        self.steps = steps
        self.tools = tools
        self.cost = cost
        self.duration = duration
        self.publish = False  # instructions are initially drafts

    @property       # all your classes are belong to us (this belongs to the class now)
    def data(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'steps': self.steps,
            'tools': self.tools,
            'cost': self.cost,
            'duration': self.duration
        }
