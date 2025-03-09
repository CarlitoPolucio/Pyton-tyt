def change(user_str):
    output = user_str.replace(":",";")
    count = output.count(";")
    return count, output


user_string = "111:1234::234:123::"
print(change(user_string))

