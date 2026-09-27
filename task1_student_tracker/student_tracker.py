def student_information():
    student_name = input("Enter Student's name: ").strip()
    student_rollno = input("Enter Student's Roll Number: ").strip()
    return student_name, student_rollno


def subject_marks():
    student_results = {}
    print("\nEnter subjects marks:")
    while True:
        subject_name = input("Enter subject name: ").strip().title()
        marks = float(input(f"Enter marks for {subject_name}: "))

        student_results[subject_name] = [marks]

        if len(student_results) >= 3:
            more = (
                input("Do you want to add another subject? (yes/no): ")
                .strip()
                .lower()
            )
            if more == "no":
                break
        else:
            print(
                f"Please enter at least {3 - len(student_results)} more subjects.\n"
            )

    return student_results


def calculating_performance(student_results):
    all_marks = [marks_list[0] for marks_list in student_results.values()]
    total_marks = sum(all_marks)
    average_score = total_marks / len(all_marks)

    if average_score >= 80:
        grade = "Grade A"
    elif average_score >= 70:
        grade = "Grade B"
    elif average_score >= 50:
        grade = "Grade C"
    else:
        grade = "Grade F (Fail)"

    return total_marks, average_score, grade


def checking_attendance():
    print("\nEnter attendance details:")
    total_classes = int(input("Enter total number of classes: "))
    classes_attended = int(input("Enter classes attended: "))

    attendance_percentage = (classes_attended / total_classes) * 100

    if attendance_percentage >= 75:
        status = "Eligible"
    else:
        status = "Not Eligible"

    return attendance_percentage, status


def report_card(
    student_name,
    student_rollno,
    student_results,
    total_marks,
    average_score,
    grade,
    attendance_percentage,
    status,
):
    print("\n" + "=" * 40)
    print("     Student Report Card     ")
    print("=" * 40)
    print(f"Name: {student_name}")
    print(f"Roll Number: {student_rollno}")
    print("-" * 40)

    for subject_name, marks_list in student_results.items():
        print(f"{subject_name:<25} | {marks_list[0]:<10.2f}")

    print("-" * 40)
    print(f"Total Marks: {total_marks:.2f}")
    print(f"Average Score: {average_score:.2f}%")
    print(f"Final Grade: {grade}")
    print(f"Attendance percentage: {attendance_percentage:.2f}%")
    print(f"Exam Eligibility: {status}")
    print("=" * 40)


def main():
    print("=== Student Grade and Attendance Tracker ===")

    student_name, student_rollno = student_information()
    student_results = subject_marks()

    total_marks, average_score, grade = calculating_performance(
        student_results
    )

    attendance_percentage, status = checking_attendance()

    report_card(
        student_name,
        student_rollno,
        student_results,
        total_marks,
        average_score,
        grade,
        attendance_percentage,
        status,
    )


if __name__ == "__main__":
    main()