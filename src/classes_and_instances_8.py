class Competition:

    def __init__(self, name, prize):
        self.name = name
        self.prize = prize
        self.participants = []


debate = Competition('Debate', 5000)

print(debate.participants)
debate.participants.append('Anna')
print(debate.participants)
debate.participants.pop()
print(debate.participants)
print(debate.__dict__)


essay = Competition('Essay', 50000)

print(essay.participants)
essay.participants.append('Denys')
print(essay.participants)
print(essay.__dict__)

