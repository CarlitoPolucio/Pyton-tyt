deposit = int(input("deposit: "))
rate = int(input("rate: "))
expectation = int(input("expectation: "))

if deposit <= 0 or rate < 0 or expectation < deposit:
    print("error")
    exit()

count = 0
rate = rate / 100 + 1

while deposit < expectation:
    deposit *= rate
    deposit //= 1
    count += 1
print(count)