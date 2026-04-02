class Club:
    name = "UNDEFINED"
    sponsor = "UNDEFINED"
    startTimeHours = 0
    startTimeMins = 0
    endTimeHours = 0
    endTimeMins = 0
    interest = 0
    def __init__(self, name, sponsor, startTime1, startTime2, endTime1, endTime2):   
        self.name = name
        self.sponsor = sponsor
        self.startTimeHours = startTime1
        self.startTimeMins = startTime2
        self.endTimeHours = endTime1
        self.endTimeMins = endTime2

def interestQuery(club):
    if input("Are you interested in this club? y/n ") == "y":
        club.interest += 1


dndClub = Club("DND Club", "Chad Stewart", 15, 0, 17, 30)
debateClub = Club("Debate Club", "Kayla Vasilko", 16, 30, 18, 0)

print(dndClub.name, dndClub.sponsor, dndClub.startTimeHours, ":", dndClub.startTimeMins, dndClub.endTimeHours, ":", dndClub.endTimeMins, dndClub.interest)

selectedClub = dndClub

interestQuery(selectedClub)

print(dndClub.interest)

print(debateClub.name, debateClub.sponsor, debateClub.startTimeHours, ":", debateClub.startTimeMins, debateClub.endTimeHours, ":", debateClub.endTimeMins, debateClub.interest)

selectedClub = debateClub

interestQuery(selectedClub)

print(debateClub.interest)