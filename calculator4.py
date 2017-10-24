#!/usr/bin/env python3

import sys
import os
from multiprocessing import Process, Queue, Lock

queue = Queue()
lock = Lock()

class Config(object):
    def __init__(self,configfile):
        self.configfile = configfile
        self._config = {}

   
    def get_config(self):
        try:
            if os.path.isfile(self.configfile):
                pass
#            else:
 #               raise FileError
        except:
            print("FileError:not exist")
            sys.exit(0)
       
        with open(self.configfile,'r') as file:
            for line in file:
                key,item = line.strip().split(' = ')
                try:
                    self._config[key] = float(item)
                except ValueError:
                     print("ValueError")
#        return self._config
#        print(self._config)  #ceshi
        queue.put(self._config)

class Userdata(Config):

    def __init__(self,userdatafile,configfile):
        self.userdatafile = userdatafile
        self.data = {}
        self.result = []
        Config.__init__(self,configfile)

           
    def get_data(self):
        try:
            if os.path.isfile(self.userdatafile):
                pass
#            else:
 #               raise FileError
        except:
            print("FileError:not exist")
            sys.exit(0)

        with open(self.userdatafile,'r') as file:
            for line in file:
                key,item = line.split(',')
                try:
                    self.data[key] = int(item)
                except ValueError:
                    print("ValueError")
                    sys.exit(0)
        return self.data

    def calculator(self):
       # c = Config(self.configfile)
#        self.get_config()
        print('start get queue') #ceshi
        config_dic = queue.get()  #get config 
        self.get_data()
#        print('hello') #ceshi
#        print(' data:',self.data.items())  #ceshi
       # print('data :',self._config.items())  #ceshi
        insurance_per = 0
        for x,y in config_dic.items():
            if not x == 'JiShuL' and not x == 'JiShuH':
        #        print(x) #ceshi
                insurance_per +=y
       # print('insurance_pe is :',insurance_per)  #ceshi

        try:
            print('ceshi') #ceshi   
            for employee_id,salary in sorted(self.data.items()):
                if salary < config_dic['JiShuL'] :
                    insurance = config_dic['JiShuL'] * insurance_per
                elif salary > config_dic['JiShuH']:
                    insurance = config_dic['JiShuH'] * insurance_per
                else:
                    insurance = salary * insurance_per
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
                    tax = 0 
                else:
                    tax = ratal * tax_rate - quick_deduction
                income = salary - insurance - tax
                               
                self.result.append(
                                   "{},{},{:.2f},{:.2f},{:0.2f}".format(
                                   employee_id,salary,insurance,tax,income)
                                  )
            with lock:
                queue.put(self.result)
#            return self.result 
        except:
            print("Parameter Error")
#        queue.put(self.result)
        print('calculae result end',self.result)  #ceshi
    def dumptofile(self,outputfile):
        reslut_queue = queue.get()
        print(reslut_queue) #ceshi
        with open(outputfile,'a') as file:
            for line in reslut_queue:
                file.write(line + '\n')


if __name__ == '__main__':
    pros = []
    args = sys.argv[1:]
    in_configfile = args[args.index('-c') +1]
    userdata = args[args.index('-d') +1]
    outfile = args[args.index('-o') +1]
    u = Userdata(userdata,in_configfile)
    pros.append(Process(target=u.get_config))
    pros.append(Process(target=u.calculator))
    pros.append(Process(target=u.dumptofile,args=(outfile,)))
    for p in pros:
        p.start()
