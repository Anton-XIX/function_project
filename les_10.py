# class Dog:
#     def __init__(self, name: str, height: int, weight: int, age: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#
#     def bark(self):
#         print('Woof Woof!')
#
#     def run(self):
#         print('Run!')
#
#     def jump(self):
#         print('Jump!')
#
#     def change_height(self, height: int):
#         self.height = height
#
#     def change_name(self, name: str):
#         self.name = name
#
#
# dog = Dog('Bob', 150, 20, 7)
#
# dog.change_name('Barsik')
# dog.change_height(160)
# dog.bark()
# dog.jump()
# dog.run()
# print(f'Name - {dog.name}\nHeight - {dog.height}\nWeight - {dog.weight}\nAge - {dog.age}\n')
########################################################################################################################


# class Dog:
#     def __init__(self, name: str, height: int, weight: int, age: int, master: str, addres: str = 'Minsk'):
#         self.__name = name  # private
#         self._height = height  # protected
#         self.weight = weight  # public
#         self.age = age
#         self.__master = master
#         self.__addres = addres
#
#     def get_master(self):
#         return self.__master
#
#     def set_master(self, master):
#         self.__master = master
#
#     def get_addres(self):
#             return self.__addres
#
#     def set_addres(self, addsres):
#             self.__address = addsres
#
# '''
# comment
# comment
# '''
#
# dog = Dog('Bob', 150, 20, 7, 'Pavel')
# # print((dog.__name)) #error
# print(dog._Dog__name)  # zaguglit'
# print(dog._height)
# print(dog.weight)
# print(dog.get_master())
# dog.set_master('Igor')
# print(dog.get_master())
# print(dog.get_addres())

##################################################################################################################

# class Dog:
#     def __init__(self,master: str, addres: str = 'Minsk'):
#         self.__master = master
#         self.__addres = addres
#
#     @property
#     def master(self):
#         return self.__master
#
#     @master.setter
#     def master(self, master):
#         if len(master) < 5:
#             self.__master = master
#
#
# dog = Dog('Pavel', 'Minsk')
# dog.master = 'My'
# print(dog.master)
#

################################################################################################################3
# class Dog:
#     def __init__(self, name: str, height: int, weight: int, age: int, master: str, addres: str = 'Minsk'):
#         self.__name = name  # private
#         self.__height = height  # protected
#         self.__weight = weight  # public
#         self.__age = age
#         self.__master = master
#         self.__addres = addres
#
#     @property
#     def master(self):
#         return self.__master
#
#     @master.setter
#     def master(self, master):
#         if len(master) < 5:
#             self.__master = master
#
#     @property
#     def name(self):
#         return self.__name
#
#     @name.setter
#     def name(self, name):
#         self.__name = name
#
#     @property
#     def age(self):
#         return self.__age
#
#     @age.setter
#     def age(self, age):
#         self.__age = age
#
#     @property
#     def weight(self):
#         return self.__weight
#
#     @weight.setter
#     def weight(self, weight):
#         self.__weight = weight
#
#     @property
#     def height(self):
#         return self.__height
#
#     @height.setter
#     def height(self, height):
#         self.__height = height
#
#     @property
#     def address(self):
#         return self.__addres
#
#     @address.setter
#     def address(self, addres):
#         self.__addres = addres
#
#
# dog = Dog('Barsik', 150, 50, 20, 'Pavel', 'Gomel')
# dog.name = 'Sobaka'
# print(dog.name, dog.height, dog.address, dog.age, dog.master, dog.weight)

#####################################################################################################################
# class Dog:
#     def __init__(self, name: str, height: int, weight: int, age: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#
#     def bark(self):
#         print('Woof Woof!')
#
#     def run(self):
#         print('Run!')
#
#     def jump(self):
#         print('Jump!')
#
#     def sleep(self):
#         print('Sleep!')
#
#     def birthday(self):
#         self.age += 1
#
#
# class Cat:
#     def __init__(self, name: str, height: int, weight: int, age: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#
#     def meow(self):
#         print('Meow Meow!')
#
#     def run(self):
#         print('Run!')
#
#     def jump(self):
#         print('Jump!')
#
#     def sleep(self):
#         print('Sleep!')
#
#     def birthday(self):
#         self.age += 1
#
#
# class Parrot:
#     def __init__(self, name: str, height: int, weight: int, age: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         self.age = age
#
#     def fly(self):
#         print('Flyyyy!')
#
#     def run(self):
#         print('Run!')
#
#     def jump(self):
#         print('Jump!')
#
#     def sleep(self):
#         print('Sleep!')
#
#     def birthday(self):
#         self.age += 1
#
#
# dog = Dog('Bob', 150, 20, 7)
# cat = Cat('John', 70, 5, 3)
# parrot = Parrot('Igor', 70, 5, 3)
#
# print(dog.age, cat.age, parrot.age)
# dog.birthday()
# cat.birthday()
# parrot.birthday()
# print(dog.age, cat.age, parrot.age)
##########################################################

class Pet:
    def __init__(self, name: str, height: int, weight: int, age: int):

        self.name = name
        self.height = height
        self.weight = weight
        self.age = age

    def run(self):
        print('Run!')

    def jump(self):
        print('Jump!')

    def sleep(self):
        print('Sleep!')

    def birthday(self):
        self.age += 1



class Dog(Pet):

    def bark(self):
        print('Woof Woof!')


class Cat(Pet):
    def meow(self):
        print('Meooow')

class Parrot(Pet):
    def fly(self):
        print('Flyyy')



dog = Dog('Bob', 150, 20, 7)
cat = Cat('John', 70, 5, 3)
parrot = Parrot('Igor', 70, 5, 3)


print(dog.name)