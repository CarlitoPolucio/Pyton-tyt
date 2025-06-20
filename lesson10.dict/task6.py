text = "127 килограмм говна вышло из жопы моей"
new_dict = {key: text.count(key) for key in text if key != " "}
print(dict(sorted(new_dict.items())), max(new_dict.values()))