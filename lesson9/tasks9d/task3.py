def path_check(__path: str) -> bool:
    if __path[-3:] == "txt" and __path[0] == "C":
        return True
    return False


if __name__ == '__main__':
    path = "C:/user/docs/folder/new_file.txt"
    print(path_check(path))