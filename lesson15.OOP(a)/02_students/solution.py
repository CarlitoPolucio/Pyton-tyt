class Student:
    def __init__(self, name: str, group_number: int, average_score: float, faculty: str):
        self.name = name
        self.group_number = group_number
        self.average_score = average_score
        self.faculty = faculty


    def get_name(self):
        return self.name


def get_sort_stud_list(students: list) -> list:
    return [student.get_name() for student in sorted(students, key=lambda stud: stud.average_score)]


if __name__ == '__main__':
    stud1 = Student("Говнарь", 1, 4.4, "факультет залуп")
    stud2 = Student("Алёша", 2, 3.5, "факультет оценки говна")
    stud3 = Student("Семя", 3, 4.8, "факультет выдавливания говна из жопы")
    stud4 = Student("Нассал", 4, 2.2, "факультет прокачки кадыка")

    print(get_sort_stud_list([stud1, stud2, stud3, stud4]))

