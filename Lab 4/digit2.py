import sys

def digit(x, count=0):
    return count if x <= 0 else digit(x // 10, count + 1)

def digit_iterative(x):
    i = 1
    while True:
        if x < 10 ** i:
            break
        i += 1
    return i

def main():
    args = int(sys.argv[1])
    print('The number of digit(s) calculated by recursive is {} and by iterative is {}.'.format(digit(args), digit_iterative(args)))

if __name__ == '__main__':
    main()
