'''
Created on Feb 10, 2019

@author: ITAUser

ALGORTHM:
1) Make a .json text file that will store our assignments
2) IMport our .json file into our code
3) Create user input for finding assignments
4) Find the users assignments in our data
    -If the users input is in our data
    -The users input isn't in our data
'''

import json

answer = ""

while(answer != 'no'):
    with open("assignments_1.json", "r") as f_r:
        data = json.load(f_r)
        print("\n\nWe have assignments of the following dueDates:")
        for i in data:
            print("\n" + i)
            
            ans = input("1. Find dueDate \n2. Add dueDate \n\n")
            if ans == '1':
                assignment = input("Enter the assignment:")
                
                print("The dueDate for {} is {}".format(assignment,data.get(assignment, "not in our database")))
            elif(ans == '2'):
                n = int(input("How many assignments do you want to add?"))
                i = 0
                while i < n:
                    print("\n Add assignment",i+1)
                    new_name = input("Enter the assignment:")
                    
                    new_dueDate = input("Enter the dueDate (dd/mm/yyyy):")
                    data[new_name] = new_dueDate
                    with open("assignments_1.json", "w")as f_w:
                        json.dump(data, f_w)
                        print ("assignment added!")
                    i+=1
            else:
                print("\nInvalid Choice!")
            answer = input("\nDo you want to use this again?(yes/no)")