"""
    Projekt IVS 2019

    Tým: /(o_o)/

    Autoři:
        - Martin Krbila
	- Jirka Hába
	- Artsiom Luhin
	- Nikolaj Vorobiev
"""

##
#   @file parse.py
#   @author Martin Krbila
#   @date 22.3.2019
#
#   @brief Standard deviation
#
#   This script computes standard deviation of numbers from stdin.

from parse import Parser
import fileinput

###############################
#
#   Entry point
#
if __name__ == "__main__":
    sumq=0.0
    sums=0.0
    n=0
    for line in fileinput.input():
        nums=[ float(i) for i in line.strip().split(" ")]
        n+=len(nums)
        for i in nums:
            sumq+=i*i
            sums+=i
        #print(nums)
    expr1="(1/%d*%f)" % (n,sums)
    expr2="sqrt(1/(%d-1)*(%f-%d*%s^2))" % (n,sumq,n,expr1)
    #print(expr1)
    #print(expr2)
    print(Parser().parse(expr2))
