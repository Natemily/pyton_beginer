# объявление функции
def is_prime(num):
    count = 0
    for i in range(1, num + 1):
        if num != 1 and num % i == 0:
            count += 1
    if count == 2:
        return True
    else:
        return False
            

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))