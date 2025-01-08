import random    # Importing the random module to generate random numbers

userGuess = 0          # Initialize the user's guess value
computerGuess = 0      # Initialize the computer's guess value

# Function to ask for user input and generate a random computer guess
def guesses():
  global userGuess
  userGuess = int(input("There are 10 Students, how many do you guess passed? "))  # Get user's guess
  
  global computerGuess
  computerGuess = random.randint(1, 10)  # Generate a random number between 1 and 10 for the computer's guess
  
  print(f"Your Guess is {userGuess}")
  print(f"The Computer Guess is {computerGuess}")
  continueProgram = input("Continue the evaluation? (Yes/YES) ")  # Ask if the user wants to continue

# Function to increment the counter for students who passed
def counterPass():
  global pStudentCounter
  pStudentCounter += 1  # Increment the passed students counter

# Function to increment the counter for students who failed
def counterFail():
  global fStudentCounter
  fStudentCounter += 1  # Increment the failed students counter

# Function to check if a student has passed or failed and categorize them accordingly
def testGrade(name, grade, subject):
  global passStudents, failedStudents
  if grade >= 75:  # If the grade is 75 or higher, the student passes
    passStudents.append([name, grade, subject])  # Add to the passed students list
    counterPass()  # Increment the passed counter
  else:  # If the grade is below 75, the student fails
    failedStudents.append([name, grade, subject])  # Add to the failed students list
    counterFail()  # Increment the failed counter

# Function to compare the guesses of the user and computer
def guessedNear():
  global userGuess, computerGuess, pStudentCounter

  nearUGuess = abs(pStudentCounter - int(userGuess))  # Difference between actual passed count and user's guess
  nearCGuess = abs(pStudentCounter - int(computerGuess))  # Difference between actual passed count and computer's guess

  # Determine whose guess is closer to the actual value
  if nearUGuess < nearCGuess:
    print(f"User Guess is nearer! {nearUGuess}")
  elif nearUGuess == nearCGuess:
    print("User and Computer Guesses are the same")
  else:
    print(f"Computer Guess is nearer {nearCGuess}")

# Function to print the list of passed and failed students
def printList():
  print("----------- List of Students who have a Passing Mark --------------------")
  print(passStudents)  # Print passed students
  print(f"Total no. of Passed Students: {pStudentCounter}")
 
  print("------------ List of Students who have a Failing Mark ---------------------")
  print(failedStudents)  # Print failed students
  print(f"Total no. of Failed Students: {fStudentCounter}")

# Dictionary to store student information (name, grade, and subject)
studentList = {
  "studentOne" : {
  "studentName": "Ricardo P",
  "studentGrade": 85,
  "classSubject": "DSA"
  },
  "studentTwo": {
  "studentName": "Anagracia A",
  "studentGrade": 82,
  "classSubject": "DSA"
  },
  "studentThree": {
  "studentName": "Anastacia D",
  "studentGrade": 75,
  "classSubject": "DSA"
  },
  "studentFour": {
  "studentName": "Gregorio D",
  "studentGrade": 74,
  "classSubject": "DSA"
  },
  "studentFive" : {
  "studentName": "Alegro",
  "studentGrade": 95,
  "classSubject": "DSA"
  },
  "studentSix" :  {
  "studentName": "Maria Juana",
  "studentGrade": 90,
  "classSubject": "DSA"
  },
  "studentSeven" : {
  "studentName": "Shantal T",
  "studentGrade": 83,
  "classSubject": "OS"
  },
  "studentEight" :{
  "studentName": "Mariano J",
  "studentGrade": 91,
  "classSubject": "OS"
  },
  "studentNine" : {
  "studentName": "Josefa G",
  "studentGrade": 73,
  "classSubject": "OS"
  },
  "studentTen" : {
  "studentName": "Eliseo S",
  "studentGrade": 75,
  "classSubject": "OS"
  }
}

# Calculate the lengths of student names and store the class subjects
nameLengths = []
classmateDict = {}
for key, value in studentList.items():
  classmateDict[value["studentName"]] = value["classSubject"]  # Store student name and subject in a dictionary
  nameLengths.append(len(value["studentName"]))  # Add the length of each student name to the list

# Create a list of class numbers (1 to 10) and sort them in reverse order
classNumbers = [i for i in range(1, 11)]
classNumbers.sort(reverse=True)

# Main function that runs the quiz
def quizTwo(userName):
  print(f"Hello, {userName}! Welcome to the quiz.")
  
  guesses()  # Get user and computer guesses

  global passStudents, failedStudents, pStudentCounter, fStudentCounter

  sizeClass = len(studentList)
  passStudents = []  # List to store students who passed
  failedStudents = []  # List to store students who failed
  pStudentCounter = 0  # Counter for passed students
  fStudentCounter = 0  # Counter for failed students

  # Loop through each student and evaluate their grade
  for x, obj in studentList.items():
    testGrade(obj.get('studentName'), obj.get('studentGrade'), obj.get('classSubject'))

  printList()  # Print the result lists of students
  guessedNear()  # Compare the guesses of user and computer

# Ask for the user's name and start the quiz
userName = input("Enter your name: ")
quizTwo(userName)  # Call the quiz function with the user's name
