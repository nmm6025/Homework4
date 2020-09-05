# Author: Nick McCuch nmm6025@psu.edu
grade1 = input("Enter your course 1 letter grade: ")
course1 = input("Enter your course 1 credit: ")
if grade1 == "A" or grade1 == "a":
  gradepoint1 = float(4.0)
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "A-" or grade1 == "a-":
  gradepoint1 = float(3.67)
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "B+" or grade1 == "b+":
  gradepoint1 = float(3.33)
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "B" or grade1 == "b":
  gradepoint1 = float(3.0)
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "B-" or grade1 == "b-":
  gradepoint1 = float(2.67)
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "C+" or grade1 == "c+":
  gradepoint1 = float(2.33)
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "C" or grade1 == "c":
  gradepoint1 = float(2.0)
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "D" or grade1 == "d":
  gradepoint1 = float(1.0)
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "F" or grade1 == "f":
  gradepoint1 = float(0.0)
  print(f"Grade point for course 1 is: {gradepoint1}")

else:  
  print(f"Grade point for course 1 is: {float(0.0)}")

grade2 = input("Enter your course 2 letter grade: ")
course2 = input("Enter your course 2 credit: ")
if grade2 == "A" or grade2 == "a":
  gradepoint2 = float(4.0)
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "A-" or grade2 == "a-":
  gradepoint2 = float(3.67)
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "B+" or grade2 == "b+":
  gradepoint2 = float(3.33)
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "B" or grade2 == "b":
  gradepoint2 = float(3.0)
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "B-" or grade2 == "b-":
  gradepoint2 = float(2.67)
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "C+" or grade2 == "c+":
  gradepoint2 = float(2.33)
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "C" or grade2 == "c":
  gradepoint2 = float(2.0)
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "D" or grade2 == "d":
  gradepoint2 = float(1.0)
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "F" or grade2 == "f":
  gradepoint2 = float(0.0)
  print(f"Grade point for course 2 is: {gradepoint2}")

else:  
  print(f"Grade point for course 2 is: {float(0.0)}")

grade3 = input("Enter your course 3 letter grade: ")
course3 = input("Enter your course 3 credit: ")
if grade3 == "A" or grade3 == "a":
  gradepoint3 = float(4.0)
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "A-" or grade3 == "a-":
  gradepoint3 = float(3.67)
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "B+" or grade3 == "b+":
  gradepoint3 = float(3.33)
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "B" or grade3 == "b":
  gradepoint3 = float(3.0)
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "B-" or grade3 == "b-":
  gradepoint3 = float(2.67)
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "C+" or grade3 == "c+":
  gradepoint3 = float(2.33)
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "C" or grade3 == "c":
  gradepoint3 = float(2.0)
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "D" or grade3 == "d":
  gradepoint3 = float(1.0)
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "F" or grade3 == "f":
  gradepoint3 = float(0.0)
  print(f"Grade point for course 3 is: {gradepoint3}")

else:  
  print(f"Grade point for course 3 is: {float(0.0)}")

GPA = ((float(course1) * float(gradepoint1) + float(course2) * float(gradepoint2)) + (float(course3) * float(gradepoint3)) / ((float(course1) + float(course2) + float(course3))))
print(f"Your GPA is: {GPA}") 