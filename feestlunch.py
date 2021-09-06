aantalCroissantjes = 17
prijsCroissantjes = 0.39
aantalStokbroden = 2
prijsStokbroden = 2.78
aantalKortingsbonnen = 3
prijsKortingsbonnen = 0.50

totaalPrijs = ((aantalCroissantjes * prijsCroissantjes) + (aantalStokbroden * prijsStokbroden) - (aantalKortingsbonnen * prijsKortingsbonnen))

#zorg voor dit antwoord: ‘De feestlunch kost je bij de bakker 10.69 euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!’

print ('De feestlunch kost je bij de bakker ' + str(totaalPrijs) + ' euro' + ' voor de ' + str(aantalCroissantjes) +' croissantjes en de ' + str(aantalStokbroden)
+ ' stokbroden als de ' + str(aantalKortingsbonnen) + ' kortingsbonnen nog geldig zijn')