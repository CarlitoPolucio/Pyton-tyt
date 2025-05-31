import os


def competition(_path: str):
    with open(_path, mode="r") as first_tour:
        second_tour_members = []
        members_list = first_tour.readlines()
        for line in members_list[1:]:
            member_inf = line.split()
            if int(member_inf[2]) >= int(members_list[0]):
                second_tour_members.append(member_inf[0] + " " + member_inf[1][0] + " " + member_inf[2])
        second_tour_sort(second_tour_members)


def second_tour_sort(_member_inf: list):
    _member_inf.sort(key=lambda member: member[-2:], reverse=True)
    with open(os.getcwd() + r"\\second_tour", mode="w") as second_tour:
        second_tour.write(f"{str(len(_member_inf))} \n")
        [second_tour.write(f"{i + 1} {memb}\n") for i, memb in enumerate(_member_inf)]


if __name__ == '__main__':
   competition(r"E:\github\lesson13.files\first_tour.txt")

