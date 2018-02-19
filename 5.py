def main():
    pass
    print("enter three numbers:")

a = int(input())
b = int(input())
c = int(input())

if a>b and a>c:
    print(a, " is largest")
elif b>a and b>c:
    print(b, " is largest")
else:
    print(c, " is largest")
if __name__ == '__main__':
    main()
