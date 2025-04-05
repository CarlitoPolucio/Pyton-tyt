def data_validation(__data_list: list) -> list:
    skip = []
    for i, ip in enumerate(__data_list):
        for num in ip[0].split("."):
            if num.isdigit() and int(num) in range(256):
                continue
            else:
                skip.append(i)
                break
    return __data_list



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
    print(data_validation(data))