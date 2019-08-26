#Question A: Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8)

#----necessary functions----
#When the user runs the program, the program prompts them to enter the 4 values of the line coordinates. Assume user knows the lines are defined as (x1, x2) and (x3, x4)
x1 = input("enter the value of x1: ")
x2 = input("enter the value of x2: ")
x3 = input("enter the value of x3: ")
x4 = input("enter the value of x4: ")

def overlap(p1, p2, p3, p4):
    if((x1>x2) or (x3>x4)):
        return "improper notation for line segments. The point x1 precede x2 on the x-axis"
    if (x1 <= x3 and x2 >= x3):
        return True
    elif (x1 >= p3 and x4 >= p1):
        return True
    else:
        return False
#----the program----
#Print the result of the function. Note the function returns strings directly rather than boolean true or false in order to facilitate returning the result to the user.          
print(str(overlap(x1, x2, x3, x4)))