def suggest_workouts(goal, experience):
    if goal == "Lose Weight":
        return ["HIIT", "Jump Rope", "Running", "Burpees"]
    elif goal == "Gain Muscle":
        return ["Push-ups", "Deadlifts", "Squats", "Bench Press"]
    else:
        return ["Yoga", "Cycling", "Plank", "Walking"]
