# coding: utf-8
# Your code here!
count = 0

def rec(number, is3use, is5use, is7use):
    if number > N:
        return 
    
    global count
    
    if is3use and is5use and is7use:
        count += 1
    
    rec(number*10+3, True, is5use, is7use)
    rec(number*10+5, is3use, True, is7use)
    rec(number*10+7, is3use, is5use, True)

def main():
    global N
    N = int(input())
    rec(0, False, False, False)
    print(count)
    

if __name__ == "__main__":
    main()