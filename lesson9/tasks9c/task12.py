text = "abchabcdhabc"
left = text.index("h")
right = text.rindex("h")
print(text[:left] + text[left:right + 1][::-1] + text[right + 1:])

