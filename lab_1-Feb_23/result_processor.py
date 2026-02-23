"""
Program: Online Exam Result Processor
---------------------------------
- Remove lowest 2 scores
- Add grace marks (5) if score between 30-35
- Count students passed (>=40)
"""

def process_results(scores):
    scores.sort()
    scores = scores[2:]  # Remove lowest 2

    updated = [
        s + 5 if 30 <= s <= 35 else s
        for s in scores
    ]

    passed = len([s for s in updated if s >= 40])

    return updated, passed


exam_scores = [25, 32, 45, 55, 20, 33, 70]

updated_scores, pass_count = process_results(exam_scores)

print("Updated Scores:", updated_scores)
print("Students Passed:", pass_count)