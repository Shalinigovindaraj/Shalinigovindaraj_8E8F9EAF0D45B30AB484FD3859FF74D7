# 1 implement a recursive function to calculate the factorial of a given number 
def fact_rac(n):
  if n==0 or n==1:
    return 1
  else:
    return n*fact_rec(n-1)

number =6
res=fact_rac(number)
print("the factorial of {} is {}.". format (number,res))
      
# leapyear 

def isleapyear(year):
  if(year % 4==0 and year % 100!=0) or yaer % 400==0:
    return True 
else:
    return false 
year =2012
if(yaer):
  print('{} is a leap year.'. format(year))
else:
  print('{} is not a leap year.'. format ( year))