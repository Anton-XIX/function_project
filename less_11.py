# class Pet:
#     def __init__(self, name: str, height: int, weight: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     def change_weigth(self, weigth):
#         self.weight = weigth
#
#     def change_height(self, heigth):
#         self.height = heigth
#
#     def jump(self, heigth):
#         print(f'Jump {heigth} meteres')
#         print('aaaa')
#
#
# class Parrot(Pet):
#     def change_weigth(self, changes=None):  # *args, if args == ()
#         if changes == None:
#             self.weight += 0.05
#         else:
#             self.weight += changes
#
#     def change_height(self):
#         super().change_height(5)
#         print(self.height)
#
#     def jump(self, heigth):
#         if heigth > 0.05:
#             print('Parrot cant jump so high')
#         else:
#             super().jump(heigth)
#
#
# class DOG(Pet):
#     def change_height(self):
#         super().change_height()
#
#     def jump(self, heigth):
#         if heigth > 0.5:
#             print('Dog cant jump so high')
#         else:
#             super().jump(heigth)
#
#
# class Cat(Pet):
#     def change_height(self):
#         super().change_height()
#         print('aaaa')
#
#     def jump(self, heigth):
#         super()
#         if heigth > 2:
#             print('Cat cant jump so high')
#         else:
#             super().jump(heigth)
#
#
# p = Parrot('ads', 15, 10)
# d = DOG('Bar', 20, 20)
# c = Cat('Car', 2, 4)
#
#
#
#
# p.jump(15)
# d.jump(15)
# c.jump(15)
#
# p.jump(0.02)
# d.jump(0.3)
# c.jump(1.5)
##################################################################################################3
# class A:
#     def __init__(self,a):
#         self.a = a
#
# class B(A):
#     def __init__(self,a,b):
#         super().__init__(a)
#         self.b = b
#
# class C:
#     def set(self):
#
# b = B(1,2)
# print(b.a, b.b)
#########################################################################################################
# class Pet:
#     def __init__(self, name: str, height: int, weight: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#
#     def change_weigth(self, weigth):
#         self.weight = weigth
#
#     def change_height(self, heigth):
#         self.height = heigth
#
#     def jump(self, heigth):
#         print(f'Jump {heigth} meteres')
#         print('aaaa')
#
#     def voice(self):
#         pass
#
#
# class Parrot(Pet):
#     def __init__(self, name: str, height: int, weight: int, species):
#         super().__init__(name,height,weight)
#         self.species = species
#
#     def change_weigth(self, changes=None):  # *args, if args == ()
#         if changes == None:
#             self.weight += 0.05
#         else:
#             self.weight += changes
#
#     def change_height(self):
#         super().change_height(5)
#         print(self.height)
#
#     def jump(self, heigth):
#         if heigth > 0.05:
#             print('Parrot cant jump so high')
#         else:
#             super().jump(heigth)
#
#     def voice(self):
#         print('ARA!')
#
#
#
# class DOG(Pet):
#     def change_height(self):
#         super().change_height()
#
#     def jump(self, heigth):
#         if heigth > 0.5:
#             print('Dog cant jump so high')
#         else:
#             super().jump(heigth)
#
#     def voice(self):
#         print('Woof Woof!')
#
#
# class Cat(Pet):
#     def change_height(self):
#         super().change_height()
#         print('aaaa')
#
#     def jump(self, heigth):
#         super()
#         if heigth > 2:
#             print('Cat cant jump so high')
#         else:
#             super().jump(heigth)
#
#     def voice(self):
#         print('Meow!')
#
#
# def make_voice(animals):
#     for animal in animals:
#         animal.voice()
#
# p = Parrot('Igor', 23,23,23)
# d = DOG('Pes',20,20)
# c = Cat('Bars',3,4)
#
#
# other = list()
# make_voice([p, d, c])
#
#
# pets = [DOG('I',2,2) for i in range(5)]
# for i in range(4):
#     pets.append(Cat('a',2,2))
#
#
# for pet in pets:
#     other.append(pet)
# make_voice(other)
#
# print(dir(p))# spisok metodov i atributov

#####################################################################################

# class Car:
#     last_model = None
#
#     def __init__(self,model):
#         self.model = model
#         Car.last_model = model
#
# car1 = Car('A')
# print(Car.last_model)
# car2 = Car('B')
# print(Car.last_model)
# car3 = Car('C')
# print(Car.last_model)
# print(car1.last_model)
# print(car2.last_model)
#
################################################3

# class Pet:
#     __counter = 0
#
#     def __init__(self, name: str, height: int, weight: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         #Pet.__counter += 1
#
#     def change_weigth(self, weigth):
#         self.weight = weigth
#
#     def change_height(self, heigth):
#         self.height = heigth
#
#     def jump(self, heigth):
#         print(f'Jump {heigth} meteres')
#         print('aaaa')
#
#     def voice(self):
#         pass
#
# class Dog(Pet):
#     def __init__(self, name: str, height: int, weight: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         Pet.__counter +=1
#
#
# p = Pet('a',23,23)
# n = Pet('a',23,23)
# a = Pet('a',23,23)
# print(Pet._Pet__counter)
# ################################################################

# class Car:
#     __last_model = None
#
#     def __init__(self,model):
#         self.model = model
#         Car.__last_model = model
#
#     @classmethod
#     def get_last_mode(cls):
#         return cls.__last_model
#
# class B(Car):
#     pass
# car1 = Car('aa')
# car2 = B('asa')
# print(car2.get_last_mode())
# print(Car.get_last_mode())
###########################################################################
class Pet:
    __counter = 0

    def __init__(self, name: str, height: int, weight: int):
        self.name = name
        self.height = height
        self.weight = weight
        Pet.__counter += 1

    def change_weigth(self, weigth):
        self.weight = weigth

    def change_height(self, heigth):
        self.height = heigth

    def jump(self, heigth):
        print(f'Jump {heigth} meteres')
        print('aaaa')

    def voice(self):
        pass

    @classmethod
    def get_counter(cls):
        return cls.__counter


p = Pet('a',23,23)
n = Pet('a',23,23)
a = Pet('a',23,23)


print(Pet._Pet__counter)
print(Pet.get_counter())