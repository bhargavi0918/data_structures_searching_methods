def binary_search_recur(list_a,target,low,high):
    if high >= low:
        mid = (high+low)//2

        if list_a[mid] == target:
            return mid
        elif list_a[mid] > target:
            binary_search_recur(list_a,target,low,mid-1)
        elif list_A[mid] < target:
            binary_search_recur(list_a,target,mid+1,high)
    else:
        return -1


def main():
    list_a = list(map(int,input("Enter the list numbers:").split( )))
    target = int(input("Enter the target number:"))
    list_a.sort()
    print(binary_search_recur(list_a,target,0,len(list_a)-1))

main()