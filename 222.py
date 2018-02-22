def main():
    pass
lee=[]
n=int(input("enter the element in array\n"))
for i in range(0,n):
	b=int(input())
	lee.append(b)
lee.sort()
print(lee[-1])
if __name__ == '__main__':
    main()
