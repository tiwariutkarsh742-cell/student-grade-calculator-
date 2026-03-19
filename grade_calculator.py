# Student Grade Calculator

def calculate_grade(marks):
    if marks >= 90:
        return "A", "Excellent work! Keep shining! 🌟"
    elif marks >= 80:
        return "B", "Very Good! Keep it up! 👍"
    elif marks >= 70:
        return "C", "Good effort! You can do even better! 💪"
    elif marks >= 60:
        return "D", "Keep trying! Improvement is possible! 📈"
    else:
        return "F", "Don't give up! Work harder and you'll succeed! 🔥"


def get_valid_marks():
    while True:
        try:
            marks = int(input("Enter marks (0-100): "))
            if 0 <= marks <= 100:
                return marks
            else:
                print("❌ Invalid input! Marks must be between 0 and 100.")
        except ValueError:
            print("❌ Please enter a valid number.")


def main():
    print("📊 STUDENT GRADE CALCULATOR\n")

    name = input("Enter student name: ").upper()
    marks = get_valid_marks()

    grade, message = calculate_grade(marks)

    print("\n📊 RESULT FOR", name + ":")
    print(f"Marks: {marks}/100")
    print(f"Grade: {grade}")
    print(f"Message: {message}")


# Run the program
if __name__ == "__main__":
    main() 