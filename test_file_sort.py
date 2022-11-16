from compute import *

def tester():
    l=[["1,4,2,6,8,5,","1,2,4,5,6,8,"],["3,1,1,0,5,7,6,","0,1,1,3,5,6,7,"],["1,2,3,4,5,","1,2,3,4,5,"],["6,1,3,5,","1,3,5,6,"]]
    for testcase in l:
        try:
            print(testcase[1])
            print(sort_fun(testcase[0]))
            if(sort_fun(testcase[0]) == testcase[1]):
                print("the test case passed")
        except:
            print("the test case failed")
            
if __name__ == "__main__":
    tester()