def input_marks(student, subjects):
    marks_list = []
    for i in range(student):
        marks = []
        print("Enter marks for student", i + 1)
        for j in range(subjects):
            mark = int(input("Enter subject " + str(j + 1) + "'s marks: "))
            marks.append(mark)
        marks_list.append(marks)
    return marks_list

def calculate_average_marks(marks_list):
    averages = []
    for marks in marks_list:
        avg = sum(marks) / len(marks)
        averages.append(avg)
    return averages

def calculate_total_average(averages):
    total_avg = sum(averages) / len(averages)
    return total_avg

def compare_with_average(total_avg, predefined_avg):
    if total_avg > predefined_avg:
        print("The total average is higher than the predefined average.")
    elif total_avg < predefined_avg:
        print("The total average is lower than the predefined average.")
    else:
        print("The total average is equal to the predefined average.")

def main():
    try:
        student = int(input("Enter the number of students: "))
        subjects = int(input("Enter the number of subjects: "))
        if student < 0 or subjects < 0:
            print("Please enter positive numbers.")
            return

        marks_list = input_marks(student, subjects)
        averages = calculate_average_marks(marks_list)
        total_avg = calculate_total_average(averages)
        
        predefined_avg = 70  # Example predefined average
        
        print("\nAverage marks of each student:", averages)
        print("Total average of all students:", total_avg)
        
        compare_with_average(total_avg, predefined_avg)
    except ValueError:
        print("Please enter valid integers.")

if __name__ == "__main__":
    main()
