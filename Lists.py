my_list = [1, 2, 3, 4, 5]
print(my_list[3])

my_list.append("cat")
print(my_list)

my_list.remove("cat")
print(my_list)

my_list.insert(2, "cat")
print(my_list)

animals = ["cat", "dog", "mouse"]
print(animals)

insects = ["ant", "bat", "cockroach"]

# .extend can be used to append lists with other lists
animals.extend(insects)
print(animals)

