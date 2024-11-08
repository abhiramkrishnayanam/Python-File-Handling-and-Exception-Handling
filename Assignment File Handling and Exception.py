# File and Exception Handling
# # Exercise 1: (score : 1) Write a Python program to read a file and display its contents
# file_1 = open("C:\\Users\\matra\\Desktop\\File handling\\abhi.txt","r")
# print(file_1.read())


# # Exercise 2: (score : 1) Write a Python program to copy the contents of one file to another file.
# from pathlib import Path
#
# source_file = Path("C:\\Users\\matra\\Desktop\\File handling\\abhi.txt")
# destination_file = Path("C:\\Users\\matra\\Desktop\\File handling\\Destination.txt")
#
# # Read contents from source and write to destination
# destination_file.write_text(source_file.read_text())
# source_file = open("C:\\Users\\matra\\Desktop\\File handling\\abhi.txt","r")
# destination_file = open("C:\\Users\\matra\\Desktop\\File handling\\Destination.txt","r")
# print(source_file.read())
# print(destination_file.read())

# # Exercise 3: (score : 2) Write a Python program to read the content of a file and count the total number
# # of words in that file.
# with open("C:\\Users\\matra\\Desktop\\File handling\\abhi.txt","r")  as abhi:
#     A=abhi.read()
#     print(A)
#     print(len(A.split()))

# # Exercise 4: (score : 1)
# # Write a Python program that prompts the user to input a string and converts it to an integer.
# # Use try-except blocks to handle any exceptions that might occur.
# try:
#     num=int(input("Enter an integer: "))
#     print(f"The number is {num}")
# except ValueError:
#     print("Invalid input. Please enter a valid integer.")

# # Exercise 5: (score : 1) Write a Python program that prompts the user to input a list of integers and raises an
# # exception if any of the integers in the list are negative.
#
# List=[]
# for i in range(11):
#     try:
#         L=int(input("Enter positive integers to the list : "))
#         if L<0:
#             raise ValueError
#         List.append(L)
#
#     except ValueError:
#         print("Enter valid positive integers!")
# print(f"The list is : {List}")

# # Exercise 6: (score : 2) Write a Python program that prompts the user to input a list of integers
# # and computes the average of those integers.Use try-except blocks to handle any exceptions that
# # might occur.use the finally close to print a message indicating that the program has finished
# # running.
# numbers=[]
# try:
#     users_input=input("Enter the numbers separated by spaces: ")
#     numbers=[int(x) for x in users_input.split()] # Convert the input string to a list of integers
#     if len(numbers)==0:
#         raise ValueError
#     avg=sum(numbers)/len(numbers)
#     print(f"The average of given numbers is : {avg}")
# except ValueError:
#     print("Error : The list cannot be empty.")
# except Exception as e:
#     print("Error ",e)
# finally:print("The program finished.")

# Exercise 7 : (score : 2) Write a Python program that prompts the user to input a filename and
# writes a string to that file.
# Use try-except blocks to handle any exceptions that might occur and print a welcome message if
# there is no exception occurred.

# try:
#     filename=input("Enter the file name want to create :")
#     content=input("Enter the content want to include in the file :")
#     with open("filename","w") as file:#opening the file to write
#         file.write(content)
#     print(f"Welcome, The content has been included in the file {filename} ")
# except Exception as e:
#     print("There is an error : ",e)