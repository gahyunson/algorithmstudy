# --- Directions
# Create an 'eventing' library out of the
# Events class.  The Events class should
# have methods 'on', 'trigger', and 'off'.

"""
What is a Callback?
A callback is 
- a function 
- is stored as data 
- designed to be called by another function
"""

class Events:
    def __init__(self) -> None:
        # Empty object
        # To register all the different events to Events Library
        self.events = {}

    # Register an event handler 
    # eventName - a string , 
    # a callback to invoke whenever that event is triggered
    def on(self, eventName, callback):
        if eventName in self.events:
            self.events[eventName].append(callback)
        else:
            self.events[eventName] = [callback]

    # Trigger all callbacks associated with a given eventName
    # associated : connected
    # Every callback in that array, we can immediately call it.
    def trigger(self, eventName):
        if eventName in self.events:
            for cb in self.events[eventName]:
                cb()
    
    # Remove all event handlers associated with the given eventName
    def off(self, eventName):
        del self.events[eventName]