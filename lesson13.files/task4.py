import os


def dir_name(input_path: str, _file: str):
    return [input_path + rf"\{_path}" for _path in os.listdir(input_path) if os.path.isdir(input_path) ]


if __name__ == '__main__':
    user_path = r"E:\github"
    user_file = "task1.py"
    print(dir_name(user_path, user_file))

    #dir_name(input_path + rf"\{_path}", _file)
    #if _path == _file and os.path.isfile(input_path + rf"\{_path}")
    #if not os.path.isfile(input_path + rf"\{_path}")