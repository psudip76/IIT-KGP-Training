##Assignment-1-Write a Python program that computes the following alternating factorial series for a given integer input ip
##function to find factorial of a number
def findfact(n):
  if n<0 :
    return("factorial not supported for negative numbers")
  fact=1
  for i in range(1,n+1):
    fact=fact*i
  return (fact)

##code to check input value is less than or equal to zero
ip=int(input("enter a number"))
if ip<0:
  print("the value of the sum is ",999)
elif ip==0:
  print("the value of the sum is",0)
else:
  #code to calculate the sum defined in the problem
  total_sum = 0.0 # Initialize total_sum
  for k in range(1,ip+1): #loop k till ip
   value= ((-1)**k)*(findfact(k)*k)/(findfact(k)+k**2) #calculate sum
   total_sum = total_sum + value # running total
  print("Final value of value is", round(total_sum,2))
