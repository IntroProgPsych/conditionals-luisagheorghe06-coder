# You are tasked with creating a simple grading system for a class. 
# Write a Python program that takes a student's score as input
#  and calculates and prints its corresponding letter grade based on the following grading scale:

# 90 or above: A
# 80-89: B
# 70-79: C
# 60-69: D
# Below 60: F
def calculate_grade():
    try:
        score = float(input("Enter the student's score: "))
        
        
        if score >= 90:
            grade = "A"
        elif score >= 80:
            grade = "B"
        elif score >= 70:
            grade = "C"
        elif score >= 60:
            grade = "D"
        else:
            grade = "F"
            
        
        print(f"The student's grade is: {grade}")
        
    except ValueError:
        
        print("Error: Please enter a valid number.")


if __name__ == "__main__":
    calculate_grade()