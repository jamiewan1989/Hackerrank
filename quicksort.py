
def partition(ar):
    if len(ar)<1:
        return ar
    equal = ar[0]
    left = []
    right = []
    i=1
    while i<len(ar):
        if ar[i]>=equal:
            right.append(ar[i])
        else:
            left.append(ar[i])
        i+=1
    if len(left)>1:
        left = partition(left)
    if len(right)>1:
        right = partition(right)
    new_ar= left + [equal] + right
    for num in new_ar:
        print num,
    print ""
    return new_ar

partition(ar)
