animals_name=["cat","dog","fish"]
animals_ages=[4,7,5]
mix=["amina",27,56.78]
print(animals_name)
print(animals_ages)
# creating an empty list
lst = []
 
# number of elements as input
n = int(input("Enter number of elements : "))
 
# iterating till the range
for i in range(0, n):
    print("Enter the number at index ",i,"  ")
    element = input()
 
    lst.append(element) # adding the element
     
print("user created list is : ",lst)
