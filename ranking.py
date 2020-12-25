f = open("ranking.txt", "r")
student_report = {}
for line in f.readlines():

        roll_num = [i for i in line.split()[0]]
        marks = [tuple(int(i) for i in line.split()[1:])]
        student_marks = dict(zip(roll_num, marks))
        student_report.update(student_marks)
print(student_report)


