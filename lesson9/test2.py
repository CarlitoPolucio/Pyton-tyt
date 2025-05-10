SPECIAL_SYMBOLS = "@№$%^&*()"


def ip_is_valid(__ip: str) -> bool:
    parts = __ip.split(".")
    if len(parts) != 4:
        return False
    for part in parts:
        if not part.isdigit() or not (0 <= int(part) <= 255):
            return False
    return True


def file_name_is_valid(__name: str) -> bool:
    return (__name.endswith(".txt") or __name.endswith(".docx")) and __name[0] not in SPECIAL_SYMBOLS


if __name__ == '__main__':
    data = [
        ["128.16.35.a4", ["file_21.txt @data_report.txt notes2024.txt"]],
        ["34.56.42,5", ["file.txt analysis_results.ttx notes2000.txt"]],
        ["128.0.0.255", ["file_1.txt document_2024.docx notes2022.txt"]],
        ["240.127.56.340", ["file_432.txt ^budget_summary.txt notes2021.txt"]],
        ["192.168.1.10", ["file_432.txt  important_info.txt notes1900.txt"]],
        ["192.c8.1.10", ["file_432.xt  &meeting_notes.docx notes1995.txt"]],
        ["10.20.30.40", ["file_432.txt  analysis_results.txt notes1998.txt"]],
    ]

    print([i for i in data if ip_is_valid(i[0]) and all(file_name_is_valid(j) for j in i[1])])




