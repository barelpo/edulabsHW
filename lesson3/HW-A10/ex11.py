import random
count = 0

while True:
    random_num = random.randint(1, 100)
    user_num = int(input("please insert number: "))
    print(f"num generated is: {random_num}")
    if user_num < random_num:
        print("you guessed too low")
    elif user_num > random_num:
        print("you guessed too high")
    else:
        print("you guessed exactly right")
        count += 1

    if input("continue/exit? ") == "continue":
        pass
    else:
        break

print(f"you guessed {count} times right")
