# a = [2,7,4,1,5,3]
a = [3,5,2,9,4,5,2,2,1,0]
for k in range(len(a)):
    for i in range(len(a)-1):
        if a[i]>a[i+1]:
            a[i],a[i+1]=a[i+1],a[i]

print(a)

#Pseudo Code
'''BubbleSort(A,n)
{
    for k <- 0 to n-1
    {
        for i <- 0 to n-2
        {
            if(A[i]>A[i+1])
                swap(A[i],A[i+1])
        }
    }
}
'''