import random

max_number = random.randint(1, 100)
update_count = 0

for i in range(100):
    current_number = random.randint(1, 100)
    if current_number > max_number:
        update_count += 1
        max_number = current_number
        if i == 99:
            print(f"{current_number} <== Update")
        else:
            print(f"{current_number} <== Update")
    else:
        print(current_number)
print("Gia tri lon nhat:",max_number)
print("So lan cap nhat:",update_count)
