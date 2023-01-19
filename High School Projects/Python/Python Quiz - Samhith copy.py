"""

# caluculate final marks provided with a grade letter ----- done
# provide final marks and letter for each class ----------- done
# total avg ----- ----------------------------------------- done
# loop through for x students  ---------------------------- done
# final output written in txt file ------------------------ done
# 4 sub 4 term marks and 4 exam marks  -------------------- done

Requirements

input validation------------------------------------------- done
endless input while loops --------------------------------- done
output to file -------------------------------------------- done

"""

import sys

userCount = 0

def credentials():

    global userCount
    userCount += 1
    
    name = str(raw_input("Please type your name: "))
    print("Greetings " + name + "!")

    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except Exception:
            print("Please enter your age in numbers only! ")

    while True:
        gender = str(raw_input("Please enter your gender (M/F) "))
        if gender == "m" or gender == "f" or gender == "M" or gender == "F":
            break
        
    if userCount >= 2:
        quizFile = open("Python Quiz - Samhith_Final Report.txt", "a")
    elif userCount == 1:
        quizFile = open("Python Quiz - Samhith_Final Report.txt", "w")

    if userCount == 1:
        quizFile.write("************ Final Report ************")
    elif userCount >= 2:
       quizFile.write("\n\n************ End of Record ***********")
       
    quizFile.write("\n\nStudent Name: " + name)
    quizFile.write("\nAge: " + str(age))
    quizFile.write("\nGender: " + gender)
    quizFile.close()
    
credentials()

       
def execution():

    quizFile = open("Python Quiz - Samhith_Final Report.txt", "a")
    
    courseOne = str(raw_input("Please enter your first course: "))
    courseTwo = str(raw_input("Please enter your second course: "))
    courseThree = str(raw_input("Please enter your third course: "))
    courseFour = str(raw_input("Please enter your fourth course: "))

    courses = {"course1": courseOne, "course2": courseTwo, "course3": courseThree, "course4": courseFour}

    while True:
        try:
            markOne = float(input("Please enter your mark for " + courseOne + ": "))
            if markOne in range(0, 101):
                break
        except Exception:
            print("Please enter a valid mark for your course!")
            
    while True:
        try:
            markTwo = float(input("Please enter your mark for " + courseTwo + ": "))
            if markTwo in range(0, 101):
                break
        except Exception:
            print("Please enter a valid mark for your course!")
      
    while True:
        try:
            markThree = float(input("Please enter your mark for " + courseThree + ": "))
            if markThree in range(0, 101):
                break
        except Exception:
            print("Please enter a valid mark for your course!")
        
    while True:
        try:
            markFour = float(input("Please enter your mark for " + courseFour + ": "))
            if markFour in range(0, 101):
                break
        except Exception:
            print("Please enter a valid mark for your course!")        

    termMarks = {courseOne: markOne, courseTwo: markTwo, courseThree: markThree, courseFour: markFour}

    while True:
        try:
            examMarkOne = float(input("Please enter your exam mark for " + courseOne + ": "))
            if examMarkOne in range(0, 101):
                break
        except Exception:
            print("Please enter a valid exam mark for your course!")

    while True:
        try:
            examMarkTwo = float(input("Please enter your exam mark for " + courseTwo + ": "))
            if examMarkTwo in range(0, 101):
                break
        except Exception:
            print("Please enter a valid exam mark for your course!")

    while True:
        try:
            examMarkThree = float(input("Please enter your exam mark for " + courseThree + ": "))
            if examMarkThree in range(0, 101):
                break
        except Exception:
            print("Please enter a valid exam mark for your course!")

    while True:
        try:
            examMarkFour = float(input("Please enter your exam mark for " + courseFour + ": "))
            if examMarkFour in range(0, 101):
                break
        except Exception:
            print("Please enter a valid exam mark for your course!")


    examMarks = {courseOne: examMarkOne, courseTwo: examMarkTwo, courseThree: examMarkThree, courseFour: examMarkFour}
    
    def calculateGrade(courseName, courseMark):
        if courseMark > 90:
            quizFile.write("\n" + courseName + ": " + str(courseMark) + "%, A+")
            
        elif courseMark in range(80, 90):
            quizFile.write("\n" + courseName + ": " + str(courseMark) + "%, A")
            
        elif courseMark in range(70, 80):
            quizFile.write("\n" + courseName + ": " + str(courseMark) + "%, B")
            
        elif courseMark in range(60, 70):
            quizFile.write("\n" + courseName + ": " + str(courseMark) + "%, C")
            
        elif courseMark in range(50, 60):
            quizFile.write("\n" + courseName + ": " + str(courseMark) + "%, D")
            
        elif courseMark < 49:
            quizFile.write("\n" + courseName + ": " + str(courseMark) + "%, F")
            
    

    courseOneAverage = markOne * 0.7 + examMarkOne * 0.3
    calculateGrade(courseName = courseOne, courseMark = courseOneAverage)
    
    courseTwoAverage = markTwo * 0.7 + examMarkTwo * 0.3
    calculateGrade(courseName = courseTwo, courseMark = courseTwoAverage)
 
    courseThreeAverage = markThree * 0.7 + examMarkThree * 0.3
    calculateGrade(courseName = courseThree, courseMark = courseThreeAverage)

    courseFourAverage = markFour * 0.7 + examMarkFour * 0.3
    calculateGrade(courseName = courseFour, courseMark = courseFourAverage)

    totalAverage = (courseOneAverage + courseTwoAverage + courseThreeAverage + courseFourAverage) / 4
    quizFile.write("\nTotal Student Average: " + str(totalAverage) + "%")    

    quizFile.close()

    quizFile = open("Python Quiz - Samhith_Final Report.txt", "r")
    print quizFile.read()

execution()


def runAgain():
    answer = str(raw_input('Run again? (y/n): '))
    if answer != 'y' or 'n':
        pass
    if answer == 'y':
        credentials()
        execution()
        runAgain()
    if answer == 'n':
        print("Goodbye!")
        quizFile = open("Python Quiz - Samhith_Final Report.txt", "a")
        quizFile.write("\n\n************ End of Report ***********")
        sys.exit()

runAgain()

