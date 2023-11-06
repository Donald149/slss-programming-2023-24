# Semester Evaluator
# Author: Donald
# 1 November 2023

# Ask about courses
print("How many courses are you taking?")
course_amount = int(input().strip(",.?! "))

# Ask about rating
total_score = 0
print("How would you rate your courses out of 5?")
for _ in range(course_amount):
    course_score = int(input(f"Course {_ + 1}: "))
    total_score += course_score

average_score = total_score/course_amount

if average_score <= 1:
    comment = "Ouch. Good luck..."
elif average_score < 3:
    comment = "Not bad, I guess..."
elif average_score >= 3:
    comment = "Good for you!"
else:
    comment = "hmm..."

if total_score % course_amount == 0:
    average_score = int(average_score)
else:
    average_score = round(average_score, 2)

print(f"{average_score}? {comment}")