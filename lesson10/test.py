text = "127 килограмм говна вышло из жопы моей"
new_dict = {key: text.count(key) for key in text if key != " "}
answer = {key: value for key, value in zip(new_dict.values(), new_dict.keys())}
print(new_dict.values())
print(new_dict.keys())