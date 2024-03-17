"""
    The InitiativeQueue functions as a simple auto ordered list (ordered by the initiative).

    Form: [(name, initiative),...]
"""
class InitiativeQueue:
    def __init__(self):
        self.queue = []

    def add(self, nc, ni):
        for i, (cc, ci) in enumerate(self.queue):
            if ni == ci:
                print("Tie at value: " + str(ni))
                print(str(self))
                break
            elif ni > ci:
                self.queue.insert(i, (nc, ni))
                print("\"" + nc + "\" placed in initiative queue")
                break
        else:
            # Never broke from loop, so queue is either empty or our initiative is smaller than all others,
            # so place at end
            self.queue.append((nc, ni))
            print("\"" + nc + "\" placed in initiative queue")

    def get_initiative(self, name):
        for char, initiative in ((c, i) for c, i in self.queue if c == name):
            # We found the character! Return their initative
            print("Initiative of {}: {}".format(name, initiative))
            return initiative
        else:
            # No Character found, give an error
            print("\"" + name + "\" is not in the initiative queue")

    def remove(self, name):
        for char, initiative in ((c, i) for c, i in self.queue if c == name):
            # We found the character! Remove them!
            self.queue.remove((char, initiative))
            print("{} removed from queue!".format(name))
            break
        else:
            # No Character found, give an error
            print("\"" + name + "\" is not in the initiative queue")

    def clear(self):
        self.queue = []
        print("Queue cleared!")

    def print(self):
        print(str(self))

    def __str__(self):
        string = "-----Initiative Queue-----\n"
        for char, initiative in self.queue:
            string += char + " : " + str(initiative) + "\n"
        return string
