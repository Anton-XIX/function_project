# def dec(func):
#     def do():
#         print('Hello world')
#         result = func()
#         return result
#     return do
#
# def my_func():
#     print('Hi\n')
#     pass
#
# my_new_func = dec(my_func)
# # my_new_func()
# ###########################################################
# @dec   # декоратор основная запись
# def my_func():
#     print('Hi\n')
#     pass
# #my_func()
#######################################################################################################
# from datetime import datetime
#
#
# def elapsed_time(func):
#     def get_time():
#         time = datetime.now()
#         return time
#
#     return get_time
#
#
# @elapsed_time  # декоратор основная запись
# def my_func():
#     print('Hi\n')
#
#
# print(my_func())
##################################################################################################################



# def get_even(func):
#     def evens():
#         return func(),[x for x in func() if x % 2 ==0], list(filter(lambda x: x % 2 ==0, func()))
#     return evens
#
#
# @get_even
# def create_list():
#     return [x for x in range(1,10)]
#
#
# print(create_list())
##############################################################################################################
# my_file = open('test.txt')
# print(my_file.readline())
# my_file.close()


# my_file = open('test.txt')
# counter = 0
# while True:
#
#     counter += 1
#     line = my_file.readline()
#     if not line:
#         break
#     if counter == 5 or counter == 1:
#         print(line)
#     if counter < 5:
#         print(line)
#
#
#
#
# my_file.close()
# my_file = open('test.txt')
# print(my_file.readlines())


#######################################################
# with open('test.txt') as my_file:  #гарантированно закроет файл
#     for line in my_file.readlines():
#         print(line)
#
#
# b = open('test.txt')
# print(b.read()[8])
#
#
# with open('test.txt', 'w') as my_file:
#     my_file.write('qwerty') # rewrite

# with open('test.txt', 'a') as my_file:  #add lines
#     my_file.writelines(['qwerty\n', 'sdsdsdsd']) # takes one argument thats why used []


# with open('test.txt', 'w') as my_file:  #add new list of lines
#     my_file.writelines(['qwerty\n', 'sdsdsdsd']) # takes one argument thats why used []


# with open('test_2.txt','a') as my_file:
#     for x in range(0,3):
#         my_file.write(+input('Type any string\n')+'\n')
###############################################################
# 10.04
with open('test_2.txt') as my_file:
    data = my_file.readlines()


with open('new_file','w') as new_file:
    for x in data:
        for i in x:
            if i =='0':
                i = '1'
            elif i == '1':
                i = '0'
            new_file.write(i)
        #new_file.write('\n')

#
###############################
#10.05
# data_1 = []
# data_2 = []
#
# with open('test.txt') as my_file:
#     data = my_file.readlines()
#     for x in range(1,len(data)-1):
#         if x % 2 != 0:
#             data_1.append(data)[x]
#         elif x % 2 == 0:
#             data_2.append(data)[x]
#
# with open('even.txt','w') as my_file:
#     for x in data_2:
#         my_file.write(x)
#
#
# with open('not_even.txt','w') as my_file:
#     for x in data_1:
#         my_file.write(x)
#
