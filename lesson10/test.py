text = "127 килограмм говна вышло из жопы моей"
output = {text.count(sym): [val for val in text if text.count(val) == text.count(sym)] for sym in text}

print(output)