class TriggerInt:

    def __init__(self, value, callback):
        self.value = value
        self.callback = callback
    
    def set(self, value):
        self.value = value
        self.callback()

    def __str__(self) -> str:
        return str(self.value)