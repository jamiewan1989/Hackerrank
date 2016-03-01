#!/bin/python    
m = input()
ar = [int(i) for i in raw_input().strip().split()]
for j in range(1,m):
    key = ar[j]
    i = j-1
    while i >= 0 and (ar[i]>key):
        ar[i+1]=ar[i]
        i = i-1 
    ar[i+1]=key
    for num in ar:
        print num,
    print ""
                             
###insertionSort(ar)
