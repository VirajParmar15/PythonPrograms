def input_marks(student,subject):
    marks_list=[]
    for i in range(student):
        marks=[]
        total = 0
        print("enter the marks for student",i + 1)
        for j in range(subject):
            mark = int(input("enter subject" + str(j+1) + 's marks:'))
            marks.append(mark)
            markstotal += marks[j]
        marks_list.append(marks)
    total += marks_list.marks[i]
    avg =  round(total / subject)
    above = 0
    return marks_list
    






        


