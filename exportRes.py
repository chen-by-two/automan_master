import sys,os
def kk ():

    total = 0
    failed = -1
    with open("allure-report/data/behaviors.csv") as k:
        lines = k.readlines()
        total = lines.__len__()-1
        for line in lines:
            tmp = line.split(",")
            if tmp[5] != "\"1\"":
                failed +=1
    os.environ["total_num"] = total
    os.environ["failed_num"] = failed
    return total,failed
if __name__ == '__main__':
    kk()
