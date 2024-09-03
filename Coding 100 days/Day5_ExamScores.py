import random

students = ["Arun","John","Peter","Mary","Sam","Kim","Potter","Hank","Ricky","Micky","Quinn","Jen"]
scores = [95,85,85,80,75,70,65,60,55,50,45,40]

random.shuffle(students)

print("The top scorer is ", students[scores.index(max(scores))] + " with a score of ", max(scores))