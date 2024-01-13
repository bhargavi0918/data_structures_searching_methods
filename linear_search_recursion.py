def linear_search(list_a,target,length):
    if length == 0:
        return -1
    elif list_a[length-1] == target:
        return length-1
    else:
        return linear_search(list_a,target,length-1)



def main():
    list_a=list(map(int,input("Enter the list elements:").split(",")))   # sorting of list elements is not required since it is linear search
    target = int(input("Enter the target:"))
    length = len(list_a)
    print(linear_search(list_a,target,length))


main()
