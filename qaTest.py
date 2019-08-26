#Question A: Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8)

def overlap(x1, x2, x3, x4):
    if((x1>x2) or (x3>x4)):
        return "improper notation for line segments. The point x1 precede x2 on the x-axis"
    if (x1 <= x3 and x2 >= x3):
        return True
    elif (x1 >= x3 and x4 >= x1):
        return True
    else:
        return False
