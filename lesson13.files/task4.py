import os


def dir_name(input_path: str, search_file: str) -> None:
     for file in os.listdir(input_path):
         full_path = os.path.join(input_path, file)
         if file == search_file and os.path.isfile(full_path):
             print(full_path)
         elif os.path.isdir(full_path):
             dir_name(full_path, search_file)


if __name__ == '__main__':
    user_path = r"E:\github"
    user_file = "task1.py"
    print(dir_name(user_path, user_file))

