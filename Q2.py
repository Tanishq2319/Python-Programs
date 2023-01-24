#Q2  divisible by 3 and 5
def divisible(num1,num2):
    for i in range(num1,num2):
        if(i%3==0 or i%5==0):
            print(i)

divisible(1,101)

