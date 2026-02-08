largest = None
smallest = None
while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
            #largest = num
            if largest is None:
                largest = num
                smallest = num
                #print("Maximum is", largest)
            elif num>largest:
                
                #smallest = largest
                largest = num
                #print("Maximum is", largest)#print(largest)
            elif num<largest:
                if num < smallest:
                    smallest = num
                else:
                    smallest = smallest
                #print("Minimum is", smallest)
        except ValueError:
            print("Invalid input")
            continue
        #print("Maximum is", num)
print("Maximum is", largest)
print("Minimum is", smallest)












# largest = None
# smallest = None

# while True:
#     num = input("Enter a number: ")

#     if num == "done":
#         break

#     else:

#         try:
#             num = int(num)
        
#             #largest = num
#             if largest is None:
#                 largest = num

#             elif num>largest:

#                 largest = num

#                 #print(largest)
#         except ValueError:
#             print("Invalid input")
#             continue

#     print("Maximum", largest)






# largest = None
# smallest = None
# while True:
#     num = input("Enter a number: ")
#     if num == "done":
#         break
#     else:
#         try:
#             num = int(num)
#             #largest = num
#             if largest is None:
#                 largest = num
#             elif num>largest:
#                 largest = num
#                 #print(largest)
#         except ValueError:
#             print("Invalid input")
#             continue
#     print("Maximum", largest)