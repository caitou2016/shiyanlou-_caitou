#!/usr/bin/env python3

import sys

try:
    salary = int(sys.argv[1])
    insurance = salary * 0.165
    ratal = salary - insurance - 3500

    if ratal <= 1500:
        tax_rate = 0.03
        quick_deduction = 0
    elif ratal <= 4500:
        tax_rate = 0.1
        quick_deduction = 105
    elif ratal <= 9000:
        tax_rate = 0.2
        quick_deduction = 555
    elif ratal <= 35000:
        tax_rate = 0.25
        quick_deduction = 1005
    elif ratal <= 55000:
        tax_rate = 0.3
        quick_deduction = 5505
    elif ratal <= 80000:
        tax_rate = 0.35
        quick_deduction = 5505
    else:
        tax_rate = 0.45
        quick_deduction = 13505

    if ratal < 0 :
        print("no tax")
    else:
        tax = ratal * tax_rate - quick_deduction
        income = salary - insurance - tax
        print("{:0.2f}".format(income))
except:
    print("Parameter Error")
