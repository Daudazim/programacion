my_list = ['a', 'b', 'c']
another_list = ['hello', 55, 6.1]
result = (my_list [0])
print(result)

result = (len(my_list))
print(type (my_list))
print(result)
print(my_list + another_list)

my_list_3 = my_list + another_list
my_list_3[3] = 'dot'
print(my_list_3)

my_list_3.append('complicates')
print(my_list_3)

removed = my_list_3.pop(6)
print(my_list_3)
print(removed)

list = ['g', 'd', 'q', 'a', 'c']
list.sort()
print(list)
list.reverse()
print(list)