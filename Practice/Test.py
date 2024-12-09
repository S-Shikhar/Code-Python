# a = int(input("enter the input:"))

# for i in range(1, a):
#     print(i)

# i = 0
# while i < a:
#     print(i)
#     i += 1


# for i in range(2,int(a/2)+1):
#     flag = True
#     if a % i ==0:
#         print("not prime")
#         flag = False
#         break

# if flag == True:
#     print("prime")


fruits = ["mango", "apple", "banana", "grapes"]

# print(len(fruits))
# print(fruits[0])
# print(fruits[1])
# a = fruits.index("banana")
# print(a)

# print(fruits.index("banana"))
fruits.append("orange")

# for i in range(len(fruits)):
#     fruits.append(input("enter the fruit:"))
print(fruits)

# fruits.remove("banana")
# fruits.pop(1)
fruits.insert(1, "mango")
fruits.sort()
fruits.reverse()
# fruits.clear()
print(fruits)
print(fruits.count("mango"))

num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

num = num[::-1]

# print(num)
# for i in "hello":
#     print(i)