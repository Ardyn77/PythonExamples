from random import randint

# def get_random_int(count, start, end):
#     list = []
#     print("the get_random_int function starts")
#     for i in range(count):
#         list.append((randint(start,end)))
#     print("function ends")
#     return list  


# print(get_random_int(10, 0,100))
def get_random_ints(count, begin, end):
    print("get_random_ints start")
    for x in range(0, count):
        yield randint(begin, end)
    print("get_random_ints end")
 
 
nums_generator = get_random_ints(10, 0, 100)
print(type(nums_generator))
for i in nums_generator:
    print(i)