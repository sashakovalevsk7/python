#задача 1

# n = input("Введите трехзначное число: ")
# n = int(n)
 
# d1 = n % 10
# n = n // 10
# d2 = n % 10
# n = n // 10
 
# print("Сумма цифр числа:", n + d2 + d1)

#задача 2

# s = input("введите число: ")
# s = int(s)  
# x = s // 6
# k = (x+x)*2
# print (x,k,x)

#задача 3
a = int(input())


k6 = a%10
k5 = a//10%10
k4 = a//100%10
k3 = a//1000%10
k2 = a//10000%10    
k1 = a//100000%10
print((k1+k2+k3)==(k4+k5+k6))
