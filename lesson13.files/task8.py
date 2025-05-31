import os


def files_counter(_path: str) -> dict:
    counter_dict = {"count": 0, "weight": 0}

    for file in os.listdir(_path):
        file_data = {"count": 1, "weight": os.path.getsize(_path + r"\\" + file) / 1024}
        counter_dict = {k: counter_dict.get(k) + file_data.get(k) for k in counter_dict}
        if os.path.isfile(_path + r"\\" + file):
            continue
        elif os.path.isdir(_path + r"\\" + file):
            file_data = (files_counter(_path + r"\\" + file))
            counter_dict = {k: counter_dict.get(k) + file_data.get(k) for k in counter_dict}
    return counter_dict


if __name__ == '__main__':
    root_path = r"C:\Program Files (x86)"
    print(files_counter(root_path))

