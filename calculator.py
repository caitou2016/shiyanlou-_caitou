#!/usr/bin/env python3

import sys

try:
    salary = int(sys.argv[1])

    income = salary - 3500

    if income <= 1500:
        tax_rate = 0.03
        quick_deduction = 0
    elif income <= 4500:
        tax_rate = 0.1
        quick_deduction = 105
    elif income <= 9000:
        tax_rate = 0.2
        quick_deduction = 555
    elif income <= 35000:
        tax_rate = 0.25
        quick_deduction = 1005
    elif income <= 55000:
        tax_rate = 0.3
        quick_deduction = 5505
    elif income <= 80000:
        tax_rate = 0.35
        quick_deduction = 5505
    else:
        tax_rate = 0.45
        quick_deduction = 13505

    if income < 0 :
        print("no tax")
    else:
        tax = income * tax_rate - quick_deduction
        print("{:0.2f}".format(tax))
except:
    print("Parameter Error")
