from points_module import batting_points, bowling_points

players = [
    {"name": "Virat Kohli", "runs": 83, "balls": 70, "fours": 8, "sixes": 2},
    {"name": "du Plessis", "runs": 94, "balls": 80, "fours": 10, "sixes": 3},
    {"name": "Bhuvneshwar Kumar", "wickets": 1, "overs": 10, "runs_given": 60},
    {"name": "Yuzvendra Chahal", "wickets": 2, "overs": 10, "runs_given": 45},
    {"name": "Kuldeep Yadav", "wickets": 4, "overs": 10, "runs_given": 35}
]

results = []

for player in players:
    if "runs" in player:
        score = batting_points(player["runs"], player["balls"], player["fours"], player["sixes"])
        results.append({"name": player["name"], "batscore": int(score)})
    else:
        score = bowling_points(player["wickets"], player["overs"], player["runs_given"])
        results.append({"name": player["name"], "bowlscore": int(score)})

# Print all players
for r in results:
    print(r)

# Find best player
best = max(results, key=lambda x: list(x.values())[1])
print("\nTop Player:", best)