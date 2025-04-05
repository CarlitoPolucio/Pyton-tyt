text = "127 килограмм говна вышло из жопы моей"
new_dict = {key: text.count(key) for key in text if key != " "}
output = {}
values = {_ for _ in new_dict.values()}
letters = []

print(new_dict.keys())