"""
Program: Attendance Tracker
---------------------------------
- Calculate attendance %
- Identify students below 75%
- Flag consecutive absences
"""

def attendance_percentage(attendance_list):
    """Calculate attendance percentage."""
    total_days = len(attendance_list)
    present_days = attendance_list.count(1)
    return (present_days / total_days) * 100


def check_consecutive_absences(attendance_list):
    """Return True if 2 consecutive absences found."""
    for i in range(len(attendance_list) - 1):
        if attendance_list[i] == 0 and attendance_list[i + 1] == 0:
            return True
    return False


attendance = [1, 1, 0, 0, 1, 1, 0]

percentage = attendance_percentage(attendance)

print("Attendance %:", round(percentage, 2))
print("Below 75%:", percentage < 75)
print("Consecutive Absence:", check_consecutive_absences(attendance))