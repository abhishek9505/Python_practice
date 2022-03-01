set1 = set([1, 2, 4, 4, 3, 3, 3, 6, 5])
print("\nSet with the use of Numbers: ")
print(set1)
  

set1 = set([1, 2, 3,'Python', 4, 'TS', 6, 'Python'])
print("\nSet with the use of Mixed Values")
print(set1)


set1 = set()
print("\nBlank Set: ")
print(set1)
  
  

set1.add(8)
set1.add(9)
set1.add((6,7))
print("\nSet after Addition of Three elements: ")
print(set1)
  

for i in range(1, 6):
    set1.add(i)
print("\nSet after Addition of elements from 1-5: ")
print(set1)
