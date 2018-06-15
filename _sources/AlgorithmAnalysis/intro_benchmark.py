import time

def summation(n):
    start = time.time()

    total = 0

    for i in range(1,n+1):
        total += i

    end = time.time()

    return total, end-start

def summation1(n):
    start = time.time()
    total = n*(n+1)/2
    end = time.time()

    return total, end-start



def main():
    for i in range(5):
        print("Sum is %d required %20.8f seconds "%summation1(100000000000))


if __name__ == '__main__':
    main()
