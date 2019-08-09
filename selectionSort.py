a = [2,7,4,1,5,3]

for i in range(len(a)-1):
    iMin = i
    for j in range(i+1,len(a)):
        if a[j] < a[iMin]:
            iMin = j
    # temp = a[iMin]
    # a[iMin] = a[i]
    # a[i] = temp
    a[i], a[iMin]=a[iMin], a[i]

print(a)

#Pseudo Code

'''SelectionSort(A,n)
{
    for i <- 0 to n-2
    {
        iMin = i
        for j <- i to n-1
        {
            if(A[j]<A[iMin])
                iMin = j
        }
        temp = A[iMin]
        A[iMin] = A[i]
        A[i] = temp
    }
}
'''
