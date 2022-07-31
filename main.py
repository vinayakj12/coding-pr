# def differenceofSum(n,m):
#   sum = 0
#   divsum = 0
#   for i in range(1,n+1):
#     if i%m==0:
#       sum +=i
#     else:
#       divsum +=i
#   return divsum-sum
      
  
# m,n = map(int,input().split())
# print(differenceofSum(n,m))

# method 2
# def diff_of_sum(n,m):
#   sum_ = n*(n+1)//2
#   temp = n // m
#   vs = 0
#   for i in range(1,temp+1):
#       vs = vs + m*i

#   sum_ = sum_ - 2*vs
#   return sum_
  
# n,m  = map(int, input().split())

# print(diff_of_sum(n,m))


# question 2 
# def LargeSmallSum(arr):
#   i=1
#   eve = []
#   odd = []
  
#   for i in range(len(arr)):
#     if i%2==0:
#       a = arr[i]
#       eve.append(a)
#     else:
#       a = arr[i]
#       odd.append(a)
#   m = sorted(eve)[-2]
#   n = sorted(odd)[-2]
#   return m + n

    
      

# arr =list(map(int,input().split()))
# ans = LargeSmallSum(arr)
# print(ans)



