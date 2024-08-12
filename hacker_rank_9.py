#The provided code stub will read in a dictionary containing 
#key/value pairs of name:[marks] for a list of students. 
#Print the average of the marks array for the student name provided, showing 2 places after the decimal.

#Sample Input 0:
# 3
# Krishna 67 68 69
# Arjun 70 98 63
# Malika 52 56 60
# Malika

#Sample Output 0:
# 56.00

def calculate_average():
    num_students = int(input())
    student_marks = {}
    for _ in range(num_students):
        data = input().split()
        name = data[0]
        marks = list(map(float, data[1:]))
        student_marks[name] = marks
    query_name = input()
    if query_name in student_marks:
        average_marks = sum(student_marks[query_name]) / len(student_marks[query_name])
        print(f"{average_marks:.2f}")
    else:
        print("Student not found")

if __name__ == '__main__':
    calculate_average()