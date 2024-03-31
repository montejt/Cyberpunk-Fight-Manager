"""
    The InitiativeList holds an ordered list of names and their corresponding initiative number,
    ordered by desc initiative

    Format: [(name, initiative),...]
"""
class InitiativeList:
    def __init__(self):
        self.initiatives = []

    def add(self, name: str, initiative: int):
    
        for i, (currName, currInitiative) in enumerate(self.initiatives):
            if initiative >= currInitiative:
                self.initiatives.insert(i, (name, initiative))
                break
        else:
            # Never broke from loop, so list is either empty or our initiative is smaller than all others,
            # so place at end
            self.initiatives.append((name, initiative))

        print("{name} placed in initiative at {initiative}")

    def get_initiative(self, name):

        for foundName, initiative in ((n, i) for n, i in self.initiatives if n == name):
            return initiative
        else:
            print("Could not find {} within the initiative".format(name))

    def remove(self, name):

        for foundName, initiative in ((c, i) for c, i in self.initiatives if c == name):
            self.initiatives.remove((foundName, initiative))
            print("{foundName} removed from initiative")
            break
        else:
            print("Could not find {name} within the initiative")

    def clear(self):
        self.initiatives = []
        print("Initiative cleared")

    def print(self):
        print(str(self))

    def __str__(self):
        string = "-----Initiative-----\n"
        for name, initiative in self.initiatives:
            string += name + " : " + str(initiative) + "\n"
        return string
