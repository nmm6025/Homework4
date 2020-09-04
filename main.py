# Author: Nick McCuch nmm6025@psu.print
grade1 = input("Enter your course 1 letter grade: ")
course1 = input("Enter your course 1 credit: ")
if grade1 == "A" or grade1 == "a":
  gradepoint1 = 4.0
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "A-" or grade1 == "a-":
  gradepoint1 = 3.67
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "B+" or grade1 == "b+":
  gradepoint1 = 3.33
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "B" or grade1 == "b":
  gradepoint1 = 3.0
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "B-" or grade1 == "b-":
  gradepoint1 = 2.67
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "C+" or grade1 == "c+":
  gradepoint1 = 2.33
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "C" or grade1 == "c":
  gradepoint1 = 2.0
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "D" or grade1 == "d":
  gradepoint1 = 1.0
  print(f"Grade point for course 1 is: {gradepoint1}")
elif grade1 == "F" or grade1 == "f":
  gradepoint1 = 1.0
  print(f"Grade point for course 1 is: {gradepoint1}")

else:  
  print(f"Invalid unit({grade1})")

grade2 = input("Enter your course 2 letter grade: ")
course2 = input("Enter your course 2 credit: ")
if grade2 == "A" or grade2 == "a":
  gradepoint2 = 4.0
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "A-" or grade2 == "a-":
  gradepoint2 = 3.67
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "B+" or grade2 == "b+":
  gradepoint2 = 3.33
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "B" or grade2 == "b":
  gradepoint2 = 3.0
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "B-" or grade2 == "b-":
  gradepoint2 = 2.67
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "C+" or grade2 == "c+":
  gradepoint2 = 2.33
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "C" or grade2 == "c":
  gradepoint2 = 2.0
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "D" or grade2 == "d":
  gradepoint2 = 1.0
  print(f"Grade point for course 2 is: {gradepoint2}")
elif grade2 == "F" or grade2 == "f":
  gradepoint2 = 1.0
  print(f"Grade point for course 2 is: {gradepoint2}")

else:  
  print(f"Invalid unit({grade2})")

grade3 = input("Enter your course 3 letter grade: ")
course3 = input("Enter your course 3 credit: ")
if grade3 == "A" or grade3 == "a":
  gradepoint3 = 4.0
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "A-" or grade3 == "a-":
  gradepoint3 = 3.67
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "B+" or grade3 == "b+":
  gradepoint3 = 3.33
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "B" or grade3 == "b":
  gradepoint3 = 3.0
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "B-" or grade3 == "b-":
  gradepoint3 = 2.67
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "C+" or grade3 == "c+":
  gradepoint3 = 2.33
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "C" or grade3 == "c":
  gradepoint3 = 2.0
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "D" or grade3 == "d":
  gradepoint3 = 1.0
  print(f"Grade point for course 3 is: {gradepoint3}")
elif grade3 == "F" or grade3 == "f":
  gradepoint3 = 1.0
  print(f"Grade point for course 3 is: {gradepoint3}")

else:  
  print(f"Invalid unit({grade3})")

GPA = ((gradepoint1 * credit1 + gradepoint2 * credit2 + gradepoint3 * credit3) / (credit1 + credit2 + credit3))
print(f"Your GPA is: {GPA}")