days = ["monday", "wednesday", "friday"]
print(days)
days.insert(1, "tuesday")
print(days)
days.insert(2, "thursday")
print(days)

# for loops can be used on lists to go through each element
for x in days:
    print(x)

# you can also print each item by referring to their index
fruit = ["apple", "banana", "cherry"]
for i in range(len(fruit)):
  print(fruit[i])

# while loops can be used to go throgh all index numbers
stocks = ["FB", "TSLA", "AAPL"]
i = 0
while i < len(stocks):
    print(stocks[i])
    i = i + 1
