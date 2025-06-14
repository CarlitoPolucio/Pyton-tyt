import os


def files_counter(_path: str) -> (int, int):
    count, weight = 0, 0
    for file in os.listdir(_path):
        file_path = os.path.join(_path, file)
        count += 1
        weight += os.path.getsize(file_path) / 1024
        if os.path.isfile(file_path):
            continue
        elif os.path.isdir(file_path):
            c, w = (files_counter(file_path))
            count += c
            weight += w
    return count, weight


if __name__ == '__main__':
    root_path = r"C:\Program Files (x86)"
    print(files_counter(root_path))