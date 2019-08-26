
import math
from qbTest import getMostRecent
from qaTest import overlap

def QATest():
    print(str(overlap(1,5,2,6)))
    print(str(overlap(1,5,6,8)))
    print(str(overlap(1,5,1,5)))
    print(str(overlap(1,5,1,8)))
    print(str(overlap(1,8,2,6)))
    print(str(overlap(2,5,1,3)))
    print(str(overlap(1,4,2,3)))
    print(str(overlap(4,1,5,2)))
    print(str(overlap(6,1,2,6)))
    print("complete.")

def QBTest():
    print(getMostRecent("1.1", "1.2"))
    print(getMostRecent("1.2", "1.1"))
    print(getMostRecent("1.1", "1.1"))
    print(getMostRecent("1.9.9.9.9", "2.0"))
    print(getMostRecent("3.4.5.6", "6.5.4.3"))
    print(getMostRecent("1.44", "1.4"))
    print(getMostRecent("1", "1.1.1"))
    print(getMostRecent("1", "1.0"))
    print(getMostRecent("1.1", "1.1"))
    print(getMostRecent("33.2345.34", "33.2345.35"))
    print(getMostRecent("5", "4"))
    print(getMostRecent("3.7", "7.3"))
    print(getMostRecent("1.999999999999", "2.0"))
    print("complete.")

print("Question A: Your goal for this question is to write a program that accepts two lines (x1,x2) and (x3,x4) on the x-axis and returns whether they overlap. As an example, (1,5) and (2,6) overlaps but not (1,5) and (6,8).")
QATest()
print("Question B: The goal of this question is to write a software library that accepts 2 version string as input and returns whether one is greater than, equal, or less than the other. As an example: “1.2” is greater than “1.1”. Please provide all test cases you could think of.")
QBTest()
