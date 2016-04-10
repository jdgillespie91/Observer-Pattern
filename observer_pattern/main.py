from abc import ABC, abstractmethod


class Subject(ABC):
    """ The Subject interface.

    In the Observer pattern, the Subject should define methods for attaching
    and detaching Observer objects from those that it is aware of. It should
    additionally define a method that notifies its observers.

    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def add_observer(self, observer):
        pass

    @abstractmethod
    def delete_observer(self, observer):
        pass

    @abstractmethod
    def notify_observers(self):
        pass


class Observer(ABC):
    """ The Observer interface.

    In the Observer pattern, the Observer should define a method that updates
    its state based on the notification it receives from the Subject. In
    addition, it should be aware of the subject it is observing.

    """
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def update(self):
        pass


class PoliceCar(Subject):
    """ The concrete subject.

    In this instance, the concrete subject is an emergency vehicle. Its role
    is to notify all observers whenever it activates or deactivates the siren.

    """
    def __init__(self):
        self._observers = []
        self.is_siren_on = False
        
    def add_observer(self, observer):
        self._observers.append(observer)
        observer.subject = self

    def delete_observer(self, observer):
        self._observers.remove(observer)
        observer.subject = None

    def notify_observers(self):
        for observer in self._observers:
            observer.update()

    def activate_siren(self):
        self.is_siren_on = True
        self.notify_observers()

    def deactivate_siren(self):
        self.is_siren_on = False
        self.notify_observers()


class NormalCar(Observer):
    """ The concrete observer.

    In this instance, the concrete observer is an ordinary (non-emergency) 
    vehicle. Its role is to stop driving whenever the subject's siren is on
    and start driving whenever it is off.

    """
    def __init__(self):
        self.subject = None
        self.is_driving = True

    def update(self):
        self.is_driving = not self.subject.is_siren_on

