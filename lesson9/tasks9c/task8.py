text = "вааагнорпаа"
vowel = ["ы", "а", "у", "о", "и", "э", "я", "ю", "е", "ё"]
vowel_list = [x for x in text if x in vowel]
print(vowel_list, len(vowel_list))