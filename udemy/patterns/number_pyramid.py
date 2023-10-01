n=int(input("Enter the limit: \n"))
# for i in range(1, n + 1):
#         for j in range(1, i + 1):
#             print("2", end=" ")
#         print()

num = 65
 
#     # outer loop to handle number of rows
# for i in range(0, n):
#     num = num + 1   
#             # not re assigning num
#             # num = 1
        
#             # inner loop to handle number of columns
#             # values changing acc. to outer loop
#     for j in range(0, i+1):
            
#                 # printing number
#         print(chr(num), end=" ")
            
#                 # incrementing number at each column
        
        
#             # ending line after each row
#     print("")


for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(1,i+1):
        print(chr(num),end=" ")
        num += 1
    num = 65
    print()
 