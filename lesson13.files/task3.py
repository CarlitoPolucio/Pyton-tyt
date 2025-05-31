import os.path


def path_definition(_path: str) ->  str | None | tuple[str, int]:
    if os.path.exists(_path):
        if os.path.isdir(_path):
            return "the path points to dir"
        elif os.path.isfile(_path):
            return "the path points to file", os.path.getsize(_path)
        else:
            return "the path points to link"
    return


if __name__ == '__main__':
    user_path =  r"C:\Users\doubl\OneDrive\Рабочий стол\Stalker2.exe"
    print(path_definition(user_path))