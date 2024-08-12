#Given the names and grades for each student in a class of n students,
#store them in a nested list and print the name(s) of any student(s) having the second lowest grade.
#Note: If there are multiple students with the second lowest grade,
#order their names alphabetically and print each name on a new line.

#Sample Input 0:
# 5
# Harry
# 37.21
# Berry
# 37.21
# Tina
# 37.2
# Akriti
# 41
# Harsh
# 39

#Sample Output 0:
# Berry
# Harry

def find_second_lowest_students():
    students = []
    num_students = int(input())
    for _ in range(num_students):
        name = input()
        grade = float(input())
        students.append([name, grade])
    unique_grades = sorted(set(student[1] for student in students))
    second_lowest_grade = unique_grades[1]
    second_lowest_students = [student[0] for student in students if student[1] == second_lowest_grade]
    second_lowest_students.sort()
    for student in second_lowest_students:
        print(student)

if __name__ == '__main__':
    find_second_lowest_students()