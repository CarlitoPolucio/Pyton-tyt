from math import floor

def poz_float_check(user_input):
    try:
        float(user_input)
    except ValueError:
        return False
    if user_input <= 0:
        return False
    else:
        return True


speed = float(input("Enter internet speed (mb/s): "))
file_size = float((input("Enter size of the file (mb): ")))

download = 0
percent = 0
time = 0

if poz_float_check(speed) and poz_float_check(file_size):
    while percent < 100:
        download += speed
        time += 1
        percent = floor((download / file_size) * 100)
        if percent > 100:
            percent = 100
            download = file_size
        print(f"{time} sec passed. {download} mb from {file_size} mb downloaded. ({percent}%)")
else:
    print("Error")

