fruits = {"orange", "apple", "banana"}

#print(fruits[0]) indexlenemez

for x in fruits:
    print(x)

fruits.add("cherry")
fruits.update(["mango","grape","apple"])

fruits.remove("mango")
print(fruits)

fruits.discard("apple")
print(fruits)

fruits.pop()
print(fruits)

fruits.clear()
print(fruits)

# myList = [1,2,5,4,4,2,1]
# print(myList)
# print(set(myList))