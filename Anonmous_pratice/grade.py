class Grade:
    def __init__(self):
        pass
    def valid_grade(self):
        
        while True:
            grade = int(input("Grade (0-20): "))
            if grade >= 0 and grade <= 20:
                print(f"Grade Saved : {grade}")
                return
            else:
                print("Invalid, try again")
hem = Grade()
hem.valid_grade()