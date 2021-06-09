import os
import time
import argparse
from typing import MutableSequence
from matplotlib import pyplot as plt 


def attack(times,m):
    cnt = 0
    for i in range(times):
        a = os.system('python RC4_attack.py -m %d -k wep_passw0rd! >>log'%m)
        if a==0:
            # print('ok')
            cnt+=1
  
    succ_rate = round(cnt/times,2)
    print("success rate:%.3lf"%(cnt/times))
    print('------------------------------')
    return succ_rate
    
parser  = argparse.ArgumentParser(description="repeating crack, count the success rate and display it")
parser.add_argument('-t',type = int, default=100,help="times to attack")
args = parser.parse_args()

times = args.t


li = [100*i for i in range(1,11)]
succ_rate = []

time_start=time.time()

for m in li:
    print("Message volume:%d"%m)
    succ_rate.append(attack(times,m))
time_end=time.time()
cost = time_end - time_start
print('time cost',time_end-time_start,'s')
plt.title("RC4 attack") 
plt.xlabel("Message volume") 
plt.ylabel("Success rate") 
plt.plot(li,succ_rate) 
fp = open("shieve","w")
print((li,succ_rate),file=fp)
print(cost,file=fp)
fp.close()
for a, b in zip(li, succ_rate):
    plt.text(a, b, b, ha='center', va='bottom', fontsize=20)

plt.show()