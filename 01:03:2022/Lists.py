List = []
print("Blank List: ")
print(List)
 

List = [10, 20, 14]
print("\nList of numbers: ")
print(List)
 

List = ["Jenkins", "Git", "Python"]
print("\nList Items: ")
print(List[0])
print(List[2])
 


List = [10, 20, 14]
print("\nLength of the List")
print(len(List))

List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)
 

for i in range(1, 4):
    List.append(i)
print("\nList after Addition of elements from 1-3: ")
print(List)
 

List.append((5, 6))
print("\nList after Addition of a Tuple: ")
print(List)

List.remove((5,6))
print("\nList after Removing elements: ")
print(List)
