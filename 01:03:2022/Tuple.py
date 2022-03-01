Tuple1 = ("Python")
print("\nTuple using String: ")
print(Tuple1)
 

list1 = [1, 2, 4, 5, 6]
print("\nTuple using List: ")
print(tuple(list1))
 

Tuple1 = tuple('Python')
print("\nTuple using function: ")
print(Tuple1)

Tuple1 = ('coding','python')
n = 3
print("\nTuple with a loop")
for i in range(int(n)):
    print(Tuple1)
    
print("\nFirst :")
print(Tuple1[0])

a, b = Tuple1
print("\nAccessing : ")
print(a)
print(b)
