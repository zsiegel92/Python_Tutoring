import random
p1_score = 0
p2_score = 0
while input("(p1) Enter 'h' or 't'") == random.choice(['h','t']):
    print("Player 1 gets a point!")
    p1_score += 1

print("\nWRONG. Player 2's turn!\n")

while input("(p2) Enter 'h' or 't'") == random.choice(['h','t']):
    print("Player 2 gets a point!")
    p2_score += 1

print("\n\nPlayer 1's score is {}. Player 2's score is {}.\n\n".format(p1_score,p2_score))
if p1_score > p2_score:
    print("Player 1 wins!")
elif p2_score > p1_score:
    print("Player 2 wins!")
else:
    print("Tie!")
