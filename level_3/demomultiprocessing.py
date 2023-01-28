import multiprocessing as mp
from time import perf_counter
import math

result1=[]
result2=[]
def cal_one(number):
    for i in number:
        result1.append(math.sqrt(i**3))
def cal_twe(number):
    for i in number:
        result1.append(math.sqrt(i**5))

if __name__=="__main__":
    numList=list(range(2500000))
    p1=mp.Process(target=cal_one,args=(numList,))
    p2=mp.Process(target=cal_twe,args=(numList,))
    start=perf_counter()
    p1.start()
    p2.start()
    end=perf_counter()
    print(f'{end-start} seconds taken')