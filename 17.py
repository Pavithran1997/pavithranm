def main():
   
 num = int(input("Enter a number: "))
 sum = 0
 temp = num
 while temp > 0:
   digit = temp % 10
   sum += digit ** 3
   temp //= 10
 if num == sum:
   print("Yes It's a armstrong")
 else:
   print("Not a armstrong")

if __name__ == '__main__':
    main()
