# --- Directions
# Create an 'eventing' library out of the
# Events class.  The Events class should
# have methods 'on', 'trigger', and 'off'.

class Events:
    def __init__(self) -> None:
        self.events = {}

    def on(self, eventName, callback):
        if eventName in self.events:
            self.events[eventName].append(callback)
        else:
            self.events[eventName] = [callback]

    def trigger(self, eventName):
        if eventName in self.events:
            for cb in self.events[eventName]:
                cb()
    
    def off(self, eventName):
        del self.events[eventName]