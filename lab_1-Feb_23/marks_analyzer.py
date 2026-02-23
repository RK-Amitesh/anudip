"""
Program: Student Marks Analyzer
---------------------------------
Features:
- Remove invalid marks (less than 0 or greater than 100)
- Calculate average
- Find topper(s)
- Assign grade based on average
"""

def clean_marks(marks):
    """Remove invalid marks outside 0-100 range."""
    return [mark for mark in marks if 0 <= mark <= 100]


def calculate_average(marks):
    """Return average of marks."""
    if not marks:
        return 0
    return sum(marks) / len(marks)


def find_toppers(marks):
    """Return list of topper marks."""
    if not marks:
        return []
    highest = max(marks)
    return [m for m in marks if m == highest]


def assign_grade(avg):
    """Assign grade based on average."""
    if avg >= 90:
        return "A+"
    elif avg >= 75:
        return "A"
    elif avg >= 60:
        return "B"
    elif avg >= 40:
        return "C"
    else:
        return "Fail"


# -------- Main Execution --------
marks = [95, 88, 102, -5, 76, 95, 64]

valid_marks = clean_marks(marks)
average = calculate_average(valid_marks)
toppers = find_toppers(valid_marks)
grade = assign_grade(average)

print("Valid Marks:", valid_marks)
print("Average:", round(average, 2))
print("Topper(s):", toppers)
print("Grade:", grade)