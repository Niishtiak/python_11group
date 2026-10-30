import random

secret_number = random.randint(1, 100)
print("Я загадал число от 1 до 100. Попробуй угадать!")

while True:
    guess = int(input("Введите вашу догадку: "))
    
    if guess < secret_number:
        print("Больше")
    elif guess > secret_number:
        print("Меньше")
    else:
        print("Поздравляю! Вы угадали число!")
        break