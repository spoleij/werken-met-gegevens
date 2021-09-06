aantalPersonen = 4
prijsTicket = 7.45
tijdGameSeat = 45
verhoudingGameSeat = 5
prijsGameSeat = 0.37

totaalPrijs = ((aantalPersonen * prijsTicket) + (tijdGameSeat / verhoudingGameSeat * prijsGameSeat * aantalPersonen))

# zorg voor dit antwoord: ‘Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar 44.44 euro’

print ('Dit geweldige dagje-uit met ' +str(aantalPersonen) +' mensen in de Speelhal met ' + str(tijdGameSeat) + ' minuten VR kost je maar ' + str(round(totaalPrijs, 2)) + ' euro')