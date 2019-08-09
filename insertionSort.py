a = [7,2,4,1,5,3]

for i in range(1,len(a)):
    value = a[i]
    hole = i
    while hole > 0 and a[hole-1] > value:
        a[hole] = a[hole-1]
        hole = hole-1
    a[hole] = value

print(a)

'''InsertionSort(A,n)
{
    for i <- 1 to n-1
    {
        value = A[i]
        hole = i
        while(hole>0 && A[hole-1] > value)
        {
            A[hole] = A[hole-1]
            hole = hole - 1
        }
        A[hole] = value
    }
}'''