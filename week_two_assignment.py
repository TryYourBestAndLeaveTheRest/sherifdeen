my_list =[]

for append_value in range(10,41,10):
    my_list.append(append_value)

my_list.insert(1,15)

to_extend = [num*10 for num in range(5,8)]
my_list.extend(to_extend)

del my_list[-1]

my_list.sort()

print(my_list.index(30))
