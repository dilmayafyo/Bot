students = [['Ильяс',5],
            ['Арыстан',4],
            ['Касым',5],
            ['Владистав',4],
            ['Искандер',5],
            ['Рахат',3],
            ['Виктор',2]]


def getListStudents():
    return students

def getStudentByIndex(a):
    if a > len(students) or a < 1:
        return "Ошибка. Такого студента нет!"
    else:
        return students[a-1]

def getAverStudMark():
    aver = 0
    for student in students:
        aver += student[1]
    return aver / len(students)
