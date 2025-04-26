def student(__stud_inf: dict) -> tuple[list, int]:
    interest_list = [val for interests in [__stud_inf[i]["interests"] for i in __stud_inf] for val in interests]
    surname_long = sum([len(__stud_inf[i]["surname"]) for i in __stud_inf])
    return interest_list, surname_long


if __name__ == '__main__':
    students = {
        1: {
            'name': 'Bob',
            'surname': 'Vazovski',
            'age': 23,
            'interests': ['biology, swimming']
        },
        2: {
            'name': 'Rob',
            'surname': 'Stepanov',
            'age': 24,
            'interests': ['math', 'computer games', 'running']
        },
        3: {
            'name': 'Alexander',
            'surname': 'Krug',
            'age': 22,
            'interests': ['languages', 'health food']
        }
    }

    print([[stud_id, students[stud_id]["age"]] for stud_id in students])
    print(student(students))