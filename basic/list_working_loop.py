# Looping through an entire list
witchs = ["newt", "credence", "lupin", "snape"]

for witch in witchs:
    print(witch)

print("-----")
# Looping with message
for witch in witchs:
    print(f"{witch.title()}, that was a great mantra!")
    print(f"I can't wait to see your next mantra, {witch.title()}. \n")

    print("Thank you, everyone. That was a great show!")
