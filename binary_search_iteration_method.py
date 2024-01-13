def binary_search(list_a,target,low,high):
    

    while low <= high:
        mid = (high+low)//2 
        
        if list_a[mid] < target: #this step to set the iterative value to target number by increasing the mid value if mid is less than target value
            low = mid+1
        
        elif list_a[mid] > target: # this step is to set the iterative value to target number by decreasing the mid value if mid value is greater than target value
            high = mid-1 
        
        elif list_a[mid] == target:
            return mid
    return -1

def main():
    list_a=list(map(int,input("Enter the list elements:").split()))
    target = int(input("Enter the target number:"))
    list_a.sort()
    print(binary_search(list_a,target,list_a[0],len(list_a)-1))

main()