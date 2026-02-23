"""
Program:Sports Tournament Points Table
---------------------------------
- Replace negative points with 0
- Sort leaderboard
- Find winner & runner-up
"""

def process_points(points):
    cleaned = [p if p >= 0 else 0 for p in points]

    sorted_points = sorted(cleaned, reverse=True)

    winner = sorted_points[0]
    runner_up = sorted_points[1]

    return sorted_points, winner, runner_up


team_points = [12, -3, 18, 9, 15]

leaderboard, winner, runner = process_points(team_points)

print("Leaderboard:", leaderboard)
print("Winner Points:", winner)
print("Runner-Up Points:", runner)