teamPedro = input()
teamJimena = input()
winningTeams = input()
pointsPedro = 0
pointsJimena = 0
joinList = ''
for character in winningTeams:
    if teamPedro.find(character) != -1: pointsPedro += 1         
    if teamJimena.find(character) != -1: pointsJimena += 1
    if pointsJimena > pointsPedro: joinList += 'J'
    elif pointsPedro > pointsJimena:joinList += 'P'
    else:joinList += 'E'
print(joinList)
