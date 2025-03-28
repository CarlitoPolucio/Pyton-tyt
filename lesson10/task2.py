def inf(__value: str) -> dict:
    keys_list = ["sd_name", "ft_name", "city", "college", "grades"]
    return {key: __value.split()[i] for i, key in enumerate(keys_list)}


if __name__ == '__main__':
    text = "Залупенко Степан Самара ПОЕБУГУ 5454345"
    print(inf(text))