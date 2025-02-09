def count_letters(user_input):
    digit = sum(1 for symbol in user_input if symbol.isdigit())
    letters = len(user_input)
    letters -= digit
    return f"digits are {digit}, letters are {letters}."

text = input("Enter the text: ")
num_of_digits = count_letters(text)
print(num_of_digits)