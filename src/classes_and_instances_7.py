class Competition:
    participants = []

    def __init__(self, name, prize):
        self.name = name
        self.prize = prize


debate = Competition('Debate', 5000)

print(debate.participants)

Competition.participants.append('Anna')
Competition.participants.append('Alice')

print(debate.participants)

essay = Competition('Essay', 456)
print(essay.participants)

debate.participants.append('Lily')

print(debate.participants)
print(essay.participants)

