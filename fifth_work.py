import time
countdown = (int(input("Введите число: ")))
print("Внимание, обратный отсчёт")
while countdown > 0:
    print(countdown)
    countdown -= 1
    time.sleep(1)
print("Поехали!")
