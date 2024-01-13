list_a = list(map(int,input("Enter the list numbers:").split(" ")))   #time complexity = O(n) ,sorting of list is not required
target = int(input("Enter the number:"))
for i in range(len(list_a)):
    if list_a[i] == target:
        print(i)