# print("Souharda")

# a = "Souharda"
# print(type(a))

# name = input("Enter your name: ")

# print(name)

# if(name == "Souharda"):
#     print("My name is Souharda")
# else:
#     print("My name is not Souharda")

# name = input("Name: ")
# if(name == "Souharda"):
# 	print("My name is Souharda")
# elif(name == "Souharda Shikhar Biswas"):
# 	print("My name is Souharda Shikhar Biswas")
# else:
# 	print("This is not my name")

def update_list():
	l1[1:3] = l2[:2]

l1 = [1, 2, 3, 4, 5]
l2 = [5, 6]

update_list()
print(l1)