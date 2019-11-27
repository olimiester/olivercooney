# def my_sum(a,b):
#     return a+b

# print(my_sum(5,5))

# def my_sum(my_integers):
#     result = 0
#     for x in my_integers:
#         result += x
#     return result

# list_of_integers = [1,2,3]
# print(my_sum(list_of_integers))

# def my_sum(*args):
#     result = 0
#     for x in args:
#         result += x
#     return result

# print(my_sum(1,2,3,4,5,6))

# my_list = [1,2,3]
# my_list[0] = 9
# print (my_list)

# my_tupple = (1,2,3)
# my_tupple[0] = 9
# print(my_tupple)

def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values()
        result += arg
    return result

print(concatenate(a="Django",b="Is",c="Great", e="!"))