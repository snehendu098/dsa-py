# how to find the next
# what will be the last and the last second
def fib(n):
    print("Starting Fibonacci:")
    last = 1
    second_last = 0
    for i in range(n):
        print(last)
        next = last + second_last
        second_last = last
        last = next
        i += 1


fib(5)
