num = int(input("Enter the number: "))

count = 0
while num > 0:
    end = num % 10
    num //= 10
    end2 = num % 10
    num //= 10
    if end == 5:
        print("Got 5. Operation has been stopped")
        break
    count += end + end2
print(f"count is {count}")


# Исправление
# num = int(input("Enter the number: "))
#
# count = 0
# while num > 0:
#     end = num % 10
#     num //= 10
#     if end == 5:
#         print("Got 5. Operation has been stopped")
#         break
#     count += end
# print(f"count is {count}")

