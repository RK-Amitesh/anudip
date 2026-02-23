"""
Program: Movie Rating System
---------------------------------
- Remove invalid ratings
- Find average rating
- Count 5-star ratings
- Sort ascending
"""

def process_ratings(ratings):
    valid = [r for r in ratings if 1 <= r <= 5]

    average = sum(valid) / len(valid) if valid else 0
    five_star_count = valid.count(5)

    valid.sort()

    return valid, round(average, 2), five_star_count


ratings = [5, 3, 6, 2, 5, 1, 0]

sorted_ratings, avg_rating, five_count = process_ratings(ratings)

print("Valid Ratings:", sorted_ratings)
print("Average Rating:", avg_rating)
print("5-Star Ratings:", five_count)