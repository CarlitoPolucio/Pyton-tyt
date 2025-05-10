import os

main_dir = os.getcwd() + "\\"
with open(main_dir + "scripts.txt", mode="a") as file:
    for py in os.listdir():
        if py.endswith("py"):
            with open(main_dir + py, mode="r") as script:
                file.write(f"{script.read()}\n")
                file.write(f"{"!"* 40}\n")