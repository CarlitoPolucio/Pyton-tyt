deposit = int(input("deposit: "))
rate = int(input("rate: "))
expectation = int(input("expectation: "))

if deposit <= 0 or rate < 0 or expectation < deposit:
    print("error")

count = 0
rate = rate / 100 + 1

while deposit > 0:
    deposit *= rate
    deposit //= 1
    count += 1
    if deposit >= expectation:
        print(count)
        break
