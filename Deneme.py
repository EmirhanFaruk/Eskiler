
# Modification date: Sat Dec 28 20:17:56 2019

# Production date: Sun Sep  3 15:43:43 2023

input("Hakları Davut\'a aittir")

input("biraz hikaye...")
klavyeci2= 1905

#menü kısmı
def menu():
	klavyeci2 = int(input("1- Arama \n2- Mesaj \n0- Çıkış  \n: "))
	klavyeci = "wow"
	if klavyeci2 == 1:
		print(arama())
	elif klavyeci2 == 2:
		print(mesaj())
	elif klavyeci2 == 0:
		klavyeci = "hiçbişe"
	else:
		print("wth smh")
#---------------------------------------------------------------------------
#arama kısmı
def arama():
	arama = 17
	while arama != 4:
		arama = int(input("1- Annem \n2- Babam \n3- Kardeşim \n4- Çıkış \n: "))
		if arama == 1:
			print("merhaba anne")
			input("merhaba")
		elif arama == 2:
			print("merhaba baba")
		elif arama == 3:
			print("merhaba kardeşim")
	if arama == 4:
		print(menu())
#---------------------------------------------------------------------------
#mesaj kısmı
def mesaj():
	mesaj =17
	while mesaj != 4:
		mesaj =int(input("1- Annem \n2- Babam \n3- Kardeşim \n4- Çıkış \n: "))
		if mesaj == 1:
			print("Mesaj gönderildi: \"Merhaba anne.\"")
		elif mesaj == 2:
			print("Mesaj gönderildi: \"Merhaba baba.\"")
		elif mesaj == 3:
			print("Mesaj gönderildi: \"Merhaba kardeşim.\"")
	if mesaj == 4:
		print(menu())
#---------------------------------------------------------------------------
#telefonun menü kısmı
klavyeci = str(input("Menüyü açmak için menü yaz \n: "))
if klavyeci == "menü":
	print(menu())
#---------------------------------------------------------------------------
print("hikaye devamı")
input("daha fazla hikaye")
