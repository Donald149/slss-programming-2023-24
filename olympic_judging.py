# Olympic Judging
# Author: Donald
# 1 November 2023

judges = 5

# Ask for judge scores
print("Judges please give a score.")

total_score = 0

for _ in range(judges):
    added_score = float(input(f"Judge {_ + 1}: ").strip(",!?"))
    total_score += added_score

# calc average score
average_score = total_score / judges

print(f"Your Olympic score is {average_score:.1f}")