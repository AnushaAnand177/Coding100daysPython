# from random import random
# functions like shuffle() and choice() belong to the random module itself, not the random() function.

import random

print("Let's play Who pays the bill!")

friends = ["Alice", "Bob", "Carol", "David", "Eve", "Fred", "Ginny", "Harriet", "Ileana", "Joseph", "Kincaid", "Larry"]

# Shuffle the list once
random.shuffle(friends)

# The first person in the shuffled list will pay the bill
bill_payer = friends[0]

# The second person in the shuffled list will not pay the bill for a week
non_payer = friends[1]

print("The bill will be paid by " + bill_payer + ".")
print("The person who will not pay the bill for a week is " + non_payer + ".")
