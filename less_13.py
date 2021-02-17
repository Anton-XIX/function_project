from time import sleep
from random import randint
import sys
import argparse

# mylist = [1,2,3]
# for i in mylist:
#     print(i)
#
# mylist2 = [x * x for x in range(3)]
# for i in mylist2:
#     print(i)
#########################################################
# mygenerator = (x * x for x in range(3))
# for i in mygenerator:
#     print(i)
#

###############################################################################
# def create_generator():
#     mylist = range(3)
#     for i in mylist:
#         yield i * i
#
#
# mygen = create_generator()
# print(mygen)
# for i in mygen:
#     print(i)
################################################################################################
# def my_animal_gen():
#     yield 'korova'
#     for animal in ['kot', 'dog', 'medved']:
#         yield animal
#     yield 'kit'
#
#
# mygen = my_animal_gen()
# print(next(mygen))
#
# print('---------------[][][][][]][][][[]--------------------')
# for animal in mygen:
#     print(animal)
#

##############################################################################################
# def gen(x, y, z):
#     while True:
#         yield randint(x, y)
#         x += z
#         y += z
#
#
# g = gen(1, 10, 10)
# for i in g:
#     print(i)
#     sleep(0.02)
######################################################################################################
print(sys.argv)
parser = argparse.ArgumentParser()
parser.add_argument('-fn', '--first-name',required=True)
parser.add_argument('-ln', '--last-name',required=True)
parser.add_argument('echo')
args = parser.parse_args()
print(args)
print('First Name:', args.first_name)
print('last', args.last_name)
print('a', args.echo)

#DJANGO###DJANGO##DJANGO##DJANGO##DJANGO###DJANGO###DJANGO####DJANGO####DJANGO
