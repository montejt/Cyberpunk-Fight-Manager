class TriggerSet:

    def __init__(self, callback):
        self.values = set()
        self.callback = callback
    
    def add(self, value):
        self.values.add(value)
        self.callback()

    def remove(self, value):
        self.values.remove(value)
        self.callback()

    def removeIfExists(self, value):
        if (value in self.values):
            self.values.remove(value)
            self.callback()

    def clear(self):
        self.values.clear()
        self.callback()

    def __iter__(self):
        for value in self.values:
            yield value

    def __str__(self) -> str:
        return str(self.values)