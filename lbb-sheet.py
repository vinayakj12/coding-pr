def minAndmax_short(a):
    a.sort()
    print(f'min:{a[0]} and max:{a[-1]}')
    
def minAndmax_long(a):
    max = -sys.maxsize
    min = sys.maxsize
    
    n = len(a)

    if n & 1:
        n -= 1


    for i in range(0,n,2):
        
        if a[i]>a[i+1]:
            maximum = a[i]
            minimum = a[i+1]
        else:
            maximum = a[i+1]
            minimum = a[i]
        
        if maximum > max:
            max = maximum

        if minimum < min:
            min = minimum

    if len(a) & 1:
        if a[n] > max: max = a[n]
        if a[n] < min: min = a[n]

    print('max is {} and min is {}'.format(max,min))


def reverse(a):
    n = len(a)
    start = 0
    end = n-1
    while start < end:
        a[start],a[end] = a[end],a[start]
        start += 1
        end -= 1
    
    print(a)


def binarySearch(a,key):
    start = 0
    end = len(a) - 1
    mid = start + (end - start)//2
    while(start<=end):

        if(a[mid] == key):
            print(mid)
            break

        if(key > a[mid]):
            start = mid + 1
        else:
            end = mid -1 

        mid = start + (end - start)//2

    print("-1") 

if __name__ == '__main__':
    import sys

    # number of elements
    n = int(input("Enter number of elements : "))

# Below line read inputs from user using map() function
    a = list(map(int,input("\nEnter the numbers : ").split()))[:n]

    print("\nList is - ", a)

    # minAndmax_short(a)
    # minAndmax_long(a)
    # reverse(a)
    # binarySearch(a,5)