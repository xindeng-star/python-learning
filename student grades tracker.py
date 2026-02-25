#1. Add student
#2. View all students
#3. Get average grade
#4. Find student
#5. Exit

def add_student(grades):
    name=input('Enter student name:')
    grade=float(input('Enter grade:'))
    grades.update({name:grade})
    print('Student added\n')

def view_all_students(grades):
    for name in grades:
        print(f'{name}:{grades[name]}\n')

def average_grade(grades):
    avg=sum(grades.values())/len(grades)
    print(f'Average grade is: {avg:.2f}\n')

def find_student(grades):
    name=input('Enter student name:')
    for name in grades:
        print(f'{name}:{grades.values()}\n')


def main():
    grades={}
    while True:
        print('student grades tracker')
        print()
        print('1. add student')
        print()
        print('2. view all students')
        print()
        print('3. get average grade')
        print()
        print('4. find student')
        print()
        click=input('Click option:')
        print()
        if click=='1':
            add_student(grades)
        elif click=='2':
            view_all_students(grades)
        elif click=='3':
            average_grade(grades)
        elif click=='4':
            find_student(grades)
        else:
            print('False Runing\n')

main()
