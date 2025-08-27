# def factorial_hashvum(num):
#     fact=1
#     while(num!=0):
#         fact=fact*num
#         num-=1
#     print(fact)
    
# factorial_hashvum(5)


# def mijin_hashvum(num):
#     sum=0
#     count=0
#     for el in num:
#         sum=el+sum
#         count+=1
#         mijin=sum/count
#     print(mijin)
    
# mijin_hashvum([5,2,8])


# try:
	
# 	num1 = int(input("Mutqagreq tiv1 = "))
# 	num2 = int(input("Mutqagreq tiv2 = "))
# 	res = num1 / num2
# except ZeroDivisionError:
# 	print("0-i vra bajanel chi kareli")
# except ValueError:
# 	print("Mutqagrvacy tiv chi")
# else:
# 	print(f"{num1}/{num2} = {res}")




# user_input=input("Enter a data= ")
# try:
#     temp= int(user_input)
#     print(f"{user_input} is int")

# except ValueError:
#     try:
#          temp=float(user_input)
#          print(f"{user_input} is float")
#     except ValueError:     
#         temp= user_input.lower()
        
#         if(temp =="false" or temp=="true"):        
#             print(f"{user_input} is boolean")
#         else:      
#             print("user_input is string ")