"""
Progarm: Salary Processing System
---------------------------------
- Remove salaries below minimum wage
- Add 5% bonus for salary > 50000
- Sort descending
- Display top 3 salaries
"""

MIN_WAGE = 15000
BONUS_RATE = 0.05


def process_salaries(salaries):
    """Process employee salary list."""
    valid = [s for s in salaries if s >= MIN_WAGE]

    updated = [
        s + s * BONUS_RATE if s > 50000 else s
        for s in valid
    ]

    updated.sort(reverse=True)
    return updated[:3]


salary_list = [12000, 55000, 48000, 75000, 30000]

top_salaries = process_salaries(salary_list)

print("Top 3 Salaries:", top_salaries)