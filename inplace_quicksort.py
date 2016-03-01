def switch_pos(ar): ###find out the position of the first available in number greater than pivot need to switch with
    for n in ar:
        if n>=ar[-1]:
            pos = ar.index(n)
            break
    return pos  



def inplace_partition(ar):
    pivot = ar[len(ar)-1]
    for num in ar:
        if num<=pivot and ar.index(num)>switch_pos(ar):    ##if the number is behind the larger number and smaller than the pivot
            temp = ar[switch_pos(ar)]     # put larger number into a temp
            temp_pos = ar.index(num)      # record the position of the current number
            ar[switch_pos(ar)]=num         ## put smaller number into previous place
            ar[temp_pos]=temp             ## put the larger number into the temp_pos
    return ar

def quicksort(ar):
    if len(ar)<2:
        return ar
    left = []
    right = []
    pivot = ar[-1]
    print ar
    ar = inplace_partition(ar);
    left = ar[:(ar.index(pivot))]
    right = ar[(ar.index(pivot)+1):]
    new_ar= quicksort(left) +[pivot]+ quicksort(right)
    print new_ar
    return new_ar
    
ar = [1,3,9,8,2,7,5]    
print quicksort(ar)  
    
