#!/usr/bin/env python3

import sys
import os

class Config(object):
    def __init__(self,configfile):
        self.configfile = configfile
        self._config = {}

        try:
            if os.path.isfile(self.configfile):
                pass
            else:
                raise FileError
        except:
            print("FileError:not exist")
            sys.exit(0)

    def get_config(self):
        with open(self.configfile,'r') as file:
            for line in file:
               key,item = line.strip().split(' = ')
               try:
                   self._config[key] = float(item)
               except ValueError:
                   print("ValueError")
       # return self._config[connect]

c =Config('/home/shiyanlou/test.cfg')
print(c.get_config('JiShuH'))
sys.exit(0)

class Uerdata(Config):

    def __init__(self,userdatafile):
        self.userdatafile = userdatafile
        self.data = {}
        try:
            if os.path.isfile(self.userdatafile):
                pass
            else:
                raise FileError
        except:
            print("FileError:not exist")
            sys.exit(0)

    def get_data(self):
        with open(userdatafile,'r') as file:
            for line in file:
                key,item = line.split(',')
                try:
                    self.data[key] = int(item)
                except ValueError:
                    print("ValueError")
                    sys.exit(0)
        return self.data
   
    def calculator(self):
        for x,y in self._config.items():
            if not x == 'JiShuL' and not x == 'JiShuH':
                insurance +=y
        print(insurance)

        try:
            for user_id,salary in self.data.items():
                if salary < self._config['JiShuL']:
                    insurance = self._config['JiShuL'] * 
            salary = int(salary2)
            
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
            
            if ratal < 0:
                income = salary - insurance 
            else:
                tax = ratal * tax_rate - quick_deduction
                income = salary - insurance - tax
            print("{}:{:0.2f}".format(employ_id,income))
    except:
        print("Parameter Error")

if __name__ == '__main__':
    tax_calculate()
