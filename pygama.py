#Napiši snake-game v pygamu
#koda od prej ti lahko sliži za inspiracijo (npr dolzina kace s kvadratki -> to pride prav)

#za projekt naredite github repozitorij, in spremembe sproti comitatje addajte in pushajte
#na koncu morajo biti v repozitoriju vsaj 3 vecji commiti

#okiren plan

#I. Naredi ogrodje -> while zanka, canvas, eventi za exit itd


#II. Naredi kvadrat -> ta kvadrat bo v prihodnisti ratala kača, zaenkrat naj bo samo kvadrat
#	naredi logiko da ta kvadrat lahko zavija levo desno z kliki na gumne na tipkovnici
#	naredi logiko, da se nakej izpiše, ko se ta kvadrat dotakne stene
#	naredi logiko, da se ta kvadrat premika po nekem "gridu" -> hint nastavi clock.tick na nekaj malega,
#		vsak frame premakni kaco za nekaj pixlov, ta premik predstavlja sirino vsake celice


#III. Kvdrat spremeni v seznam kvadratov, ki predstavljajo kaco


#IV. Naredi logiko, da se nekaj izpiše, ce se kace zabije sama vase


#V. Naredi nek nov kvadrat ki predstavlja hrano
#	-> naredi da se vsakic ko ga kaca poje z glavo prestavi na nakljucno mesto in kaca zrasta


#od tu naprej je treba samo še štet score, kej izpiovat na ekrat, dt kk gumb za game over pa restart itd... neke olepšave




#1. dodatna naloga:
#naredi branch "izgled"
#v tem brancu naredi logiko, da ko igra tece, lahko pritisnes gumb "space" kar celotni kaci nastavi nakljucno barvo

#2. dodatna naloga:
#naredi branch "multiplayer"
#v tem branchu naredi logiko, da sta na zacetku igre 2 kaci, ena se upravlja z wasd, druga z gumbi s puscicami
#ce se aca zabije vase, v drugo kaco ali v steno, izgubi

#3. dodatna naloga
#naredi megre obeh branchov


