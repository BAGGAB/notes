# from abc import ABC, abstractmethod

# class Observable:
#     def __init__(self):
#         self._observers = []

#     def register_observer(self, observer):
#         self._observers.append(observer)

#     def unregister_observer(self, observer):
#         self._observers.remove(observer)

#     def notify_observers(self, *args, **kwargs):
#         for obs in self._observers:
#             obs.process_event(self, *args, **kwargs)



# class HumanCompositions(ABC):
#     @abstractmethod
#     def process_event(self, observable, *args, **kwargs):
#         '''Notify'''



# class Observer:
#     notify_to: HumanCompositions
#     observable: Observable
#     def __init__(self, observable,person1):
#         self.observable = observable
#         observable.register_observer(self)
#         self.notify_to = person1

#     def process_event(self, observable, *args, **kwargs):
#         self.notify_to.process_event(self, observable, *args, **kwargs)
    
#     def delete(self):
#         self.observable.unregister_observer(self)

#     def __del__(self):
#         print('Destructor called, Employee deleted.')





# class Live(Observer):
#     def process_event(self, observable, *args, **kwargs):
#         print("Live Got", args, kwargs, "From", observable)
#         super().process_event(self, observable, *args, **kwargs)


# class Job(Observer):
#     def process_event(self, observable, *args, **kwargs):
#         print("Work Got", args, kwargs, "From", observable)
#         super().process_event(self, observable, *args, **kwargs)


# class Hobby(Observer):
#     def process_event(self, observable, *args, **kwargs):
#         print("Hobby Got", args, kwargs, "From", observable)
#         super().process_event(self, observable, *args, **kwargs)




# class Human(HumanCompositions):
#     observers =  []
#     def __init__(self):
#         print('Class Human Created')
#         # observable.register_observer(self)
#         # self.observables =  [Observer]

#     def addComposition(self, observable: Observable):
#         self.observers.append(observable)

#     def process_event(self, observable, *args, **kwargs):
#         print("Human Got", args, kwargs, "From", observable)

#     def __del__(self):
#         for observer in range(len(self.observers)):
#             self.observers[0].delete()
#             self.observers.remove(self.observers[0])
#         print('Destructor called, HumanCompositions deleted.')



# if __name__ == '__main__':
#     Life_Observable = Observable()
#     Work_Observable = Observable()
#     Work1_Observable = Observable()
#     Hobby_Observable = Observable()

#     person1 = Human()
#     person1.addComposition(Live(Life_Observable,person1))
#     person1.addComposition(Job(Work_Observable,person1))
#     person1.addComposition(Job(Work1_Observable,person1))
#     person1.addComposition(Hobby(Hobby_Observable,person1))
#     # Life.notify_observers("test", kw="python")
#     Work1_Observable.notify_observers("Hire", kw="python")
#     print('Before Delete')
#     person2 = Human()
#     del person2
#     # Life_Observable.unregister_observer(person1)
#     # person1.delete()
#     del person1
#     # print(person1)
#     print('After Delete')
#     input("Your name: ")
#     # Hobby_Observer.notify_observers("Get Hobby", kw="python")