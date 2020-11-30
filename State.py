#State
class State(object):

    def __init__(self):
        print (f'Processing current state:', str(self))

    def on_event(self, event):
        pass

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        return self.__class__.__name__

#ConcreteStateA
class LockedState(State):

    def on_event(self, event):
        if event == 'pin_entered':
            return UnlockedState()

        return self

#ConcreteStateB
class UnlockedState(State):

    def on_event(self, event):
        if event == 'device_locked':
            return LockedState()

        return self

#Context
class Safebox(object):

    def __init__(self):
        self.state = LockedState()

    def on_event(self, event):
        self.state = self.state.on_event(event)

if __name__ == "__main__":

    device = Safebox()

    device.on_event('device_locked')
    device.on_event('pin_entered')  
    print(device.state)

    device.on_event('device_locked')
    print(device.state)

    device.on_event('device_locked')