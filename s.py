# fname='abhinand'
# lname='narayanan'
# msg=f'{fname} [{lname}] is a coder'
# print(msg)

# weight=int(input("Enter the weight"))
# unit=input("Unit is in Kg or lbs")
# if unit.upper()=='L':
#     w=weight*.45
#     print(f'You are converted in {w} in kilos')
# else:
#     w=weight/.45
#     print(f' You are converted in to {w} Lbs')


# has_good_credit=True
# has_criminal_record=False
# if has_good_credit and not has_criminal_record:
#     print('Eligible for loan')


# name=input("Enter the name: ")
# if len(name)<3:
#     print("Name must be greater than 3 ")
# elif len(name)>50:
#     print("Name must be less than 50 ")
# else:
#     print("Name looks good!")

# n=9
# i=0
# while(i<=3):
#     if i==3:
#         print("You loss")
#         braek
#     m=int(input("Guess"))
#     if m==n:
#         print("you won")
#     i+=1

# num=[5,2,5,2,2]
# for i in range(0,len(num)-1):
#     print('*'*num[i])

# num=[34,16,48,56,6,5]
# largest=num[0]
# for i in range(len(num)-1):
#     if num[i]>largest:
#         largest=num[i]
    

# print(largest)

num=[4,3,2,4,5,6,6,5,4,1,9,1]
unique=[]
for i in range(0,len(num)-1):
    if num[i] not in unique:
        unique.append(num[i])
print(unique)

