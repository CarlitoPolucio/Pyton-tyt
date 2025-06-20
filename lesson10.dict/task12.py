text = "127 килограмм говна вышло из жопы моей"
new_dict = {key: text.count(key) for key in text if key != " "}
output = {}
values = {_ for _ in new_dict.values()}

for val in values:
    letters = []
    for key, value in new_dict.items():
        if value == val:
            letters += key
    output[val] = letters

print(output)







