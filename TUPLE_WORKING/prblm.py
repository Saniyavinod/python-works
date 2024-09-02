numbers=[1,2,[3,(100,200,300),4],5,6]

tuple_first=numbers[2][1]

new_list=list(tuple_first)

new_list.append(500)



new_tuple=tuple(new_list)

print(new_tuple)

numbers[2][1]=new_tuple
print(numbers)