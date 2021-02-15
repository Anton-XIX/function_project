# class Car:
#     __last_model = None
#
#     def __init__(self, model):
#         self.model = model
#         Car.__last_model = model
#
#     @staticmethod
#     def is_model_ok(model):
#         return len(model) > 3
#
#
# a = Car('sflls')
# print(Car.is_model_ok(a.model))
# print(Car.is_model_ok('abc'))
#####################################################################################################
#
# class Pet:
#     def __init__(self, a):
#         self.a = a
#
#     @staticmethod
#     def reverse_sring(a):
#         return a[::-1], list(reversed(a))
#
#
# print(Pet.reverse_sring('ABCDE'))

##########################################################################################################

# class A:
#     def hi(self):
#         print('A')
#
# class B(A):
#     def hi(self):
#         print('B')
#
#
# class C(A):
#     def hi(self):
#         print('C')
#
# class D(B,C):
#     pass
#
#
# d = D()
# d.hi()
############################################################################################
# class Pet:
#     __counter = 0
#
#     def __init__(self, name: str, height: int, weight: int):
#         self.name = name
#         self.height = height
#         self.weight = weight
#         # Pet.__counter += 1
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
# class Donkey(Pet):
#     def voice(self):
#         print('AAAAAAAAA')
#
#
# class Horse(Pet):
#     def voice(self):
#         print('IGOGOGO')
#
#
# class Mule(Donkey, Horse):
#     pass
#
#
# m = Mule('aaaaa', 228, 999)
# m.voice()
# print(Mule.mro())

##########################################################################################################################


#
# try:
#     a = int(input('a:\n'))
#     b = int(input('b:\n'))
#     result = a/b
#
# except ZeroDivisionError as err:
#     print(f'b is zero - {err}!!!')
# except Exception as err:
#     print(f'Something wrong - {err}!!!!!')
# else:
#     print('No error')
#     print(result)
# finally:
#     print('FINALLY')

# if b == 10:
#         raise ZeroDivisionError('b is 10')

#################################################################
# class MyExc(Exception):
#     def __init__(self, mes = 'aaaaa'):
#         super().__init__(mes)
# raise MyExc
###############################################################################################
# class MyErr(Exception):
#     def __init__(self, mess='Zero cost'):
#         super().__init__(mess)
#
#
# class Book:
#     def __init__(self, pages, year, author, cost):
#         try:
#             self.pages = pages
#             self.year = year
#             self.author = author
#             self.cost = cost
#
#             if type(pages) != int:
#                 raise TypeError('Pages is not int')
#             if type(year) != int:
#                 raise TypeError('Year is not int')
#             if type(author) != str:
#                 raise TypeError('Author is not str')
#             if type(cost) != int:
#                 raise TypeError('Cost is not int')
#             if year > 2021:
#                 raise ValueError('Error year')
#
#             if cost == 0:
#                 raise MyErr
#
#         except TypeError as te:
#             print(te)
#
#         except ValueError as ve:
#             print(ve)
#
#         except MyErr as err:
#             print(f'cost is not valid - {err}')
#         else:
#             print('Data is correct')
#
#
# a = Book('str', 2022, 'Author', 10)
# b = Book(12, 'str', 'author', 10)
# c = Book(12, 2000, 45, 10)
# d = Book(12, 200, 'author', [])
# e = Book(12, 3000, 'author', 10)
# f = Book(12, 2000, 'author', 0)
# h = Book(12,2000,'d',222)
############################################################################################################
# from abc import ABC, abstractmethod
#
# class A(ABC):
#     @abstractmethod
#     def do_smth(self, z=12):
#         print('I am parent')
#
# class B(A):
#     def do_smth(self,z = 15):
#         print('I am child')
#
# A.do_smth(12)
# b = B()
################################################################################################################