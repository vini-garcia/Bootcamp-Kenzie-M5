list1 = list(range(6, 21))

# print(list1[-1])

list1[1] = "Kenzie"
# print(list1)

# print(list1[2:5])

list1.append("Academy")
# print(list1)

list1.remove("Kenzie")
list1.remove("Academy")
# print(list1)

list2 = list1.copy()
list2.reverse()
# print(list1)
# print(list2)

lista_2 = sorted(list1, reverse=True)
# print(list1)
# print(lista_2)

# print(len(list1))
# print(len(list2))

list1.pop()
list2.pop()
# print(list1)
# print(list2)

list1.clear()
list2.clear()
# print(list1)
# print(list2)
