
# Modification date: Fri Jan 10 22:41:30 2020

# Production date: Sun Sep  3 15:43:43 2023

print("Tüm hakları bana aittir. Olaylar ve kişiler gerçek değildir.")
emirhaberi = []
durum = []
#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def ara():
    print("lol")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def telefonarama():
    print("\n\n")
    r = 0
    while r != 4:
        if durum[0] == 1:
            break
        else:
            print("Kimi arayacaksın?(telefondaki - li konuimalar karşı kişi, + lı konuşmalar sana ait.)")
            r = int(input(" 1- Kardeşim \n 2- Nibba Emir \n 0- Çık \n: "))
            if r == 1:
                input("Çalıyor...")
                input("Cevap yok.")
                print("-----------------------------------------------------------------------------\n\n")
            elif r == 2:
                input("+Alo?")
                input("-Efendim kanka.")
                input("+Kanka acil yardımın lazım. Kardeşim evden kaçtı ve baya uzaklaşmış. Erzak falan ne bulursan çantana koyup getirebilir misin? Benim için de getir.")
                input("-Ne demek knk birkaç dakikaya oradayım.")
                input("Arama bitti.")
                print("-----------------------------------------------------------------------------\n\n")
                return 1
            if r == 0:
                print(telefon())
                break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def telefongps():
    print("\n\n")
    g = 0
    while g != 4:
        if durum == 1:
            break
        else:
            print("Kimin gps'sine bakacaksın?")
            g = int(input(" 1- Kardeşim \n 2- Nibba Emir \n 0- Çık\n: "))
            if g == 1:
                input(".....Ormanda.")
                print("-----------------------------------------------------------------------------\n\n")
            elif g == 2:
                input(".....Evinde.")
                print("-----------------------------------------------------------------------------\n\n")
            if g == 0:
                print(telefon())
                break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

input("\n    Arkadaşlarınla geçirdiğin harkika bir günün akşamındasın.")
telefonn = "\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\nAramak, kişi bulmak, mesaj atmak gibi işlevleri yerine getirir. Aramak için telefonarama, kişi bulmak için telefongps yazabilirsin.\n---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------\n"
input("\n    Elindeki telefonla Nibba Emir ile sohbet ederken, salondan bağırışmalar duyuyorsun.")
input("\n    Hemen telefonu bırakıp salona koştun.")
input("\n    Ama olaya biraz geç kalmıştın. Kardeşin, sertçe kapıyı kapatıp dışarı çıkmıştı.")
input("\n Olay, babanla kardeşin arasındaydı. Babası, kardeşinin hayali arkadaşlarına kendisinden daha çok saygı göstermesini doğru bulmamıştı. Kardeşin ise, böyle birşey ile karşılaşınca hazmedememiş, iyice sinirlenip kapıyı çarpıp çıkmıştı.")
input("\n    Sen zaten kardeşinin bu \"Hayali arkadaş\" olaylarından haberdardın. Kendisi sık sık onunla konuşurdu. Ama henüz kendi gözlerinle varlığını görememiştin.")
input("\n Baban sinirli bir şekilde \"Git şu kardeşini çabuk bul gel! Ormanlık alan kaybulcak falan şimdi. Bir sorun daha istemiyorum. \"")
input("\n    Babanın sinirini üstüne çekmemek için hemen yanına telefonu alıp dışarı çıktın. Kardeşinin sinyali nasıl olduysa çok uzakta gözüküyor.")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def çıkış():
    print("Çıkılıyor...")

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
def telefon():
    a = b
    while a == "telefon()" or "telefon" or "telefonarama" or "telefongps" or "çık":
        a = input("Bir telefon fonksiyonu girebilirsin, örnek olarak telefon yazarsan tanımı görürsün. Çıkmak için çık yaz.\n\n: ")
        if a == "telefon":
            print(telefonn)
            print(telefon())
        elif a == "telefonarama":
            print(telefonarama())
            print(telefon())
        elif a == "telefongps":
            print(telefongps())
            print(telefon())
        elif a == "çık":
            print(çıkış())
            durum.insert(0,1)
            break

#---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
b = str(input("\n***Telefonunu telefon() yazarak inceleyebilir veya kullanabilirsin."))
if b == "telefon()":
    print(telefon())




if emirhaberi == 1:
    input("\nOrmana doğru baktın. Çok karanlık gözüküyor.")
    input("\nKardeşin aklına geldi. ")
    input("\nO da bu kadar korkmuş muydu?")
    input("\nYoksa \"Hayali arkadaşı\"yla mı birlikteydi?")
    input("\n   \"Resul!\"")
    input("\nWtf?")
    input("\nArkana baktığında elinde ve sırtında çanta ile sana koştuğunu görüyorsun.")
    input("\n\"Korkuttun beni. Hem sen nasıl o kadar hızlı geldin?\"")
    input("\n   \"Beni boşver knk hadi kardeşini bulalım.\"")
elif emirhaberi == 0:
    input("\nOrmana doğru baktın. Çok karanlık gözüküyor.")
    input("\nKardeşin aklına geldi. ")
    input("\nO da bu kadar korkmuş muydu?")
    input("\nYoksa \"Hayali arkadaşı\"yla mı birlikteydi?")

input("\nDaha fazla vakit kaybetmemek için yola çıktın.")

input("Şimdilik bu kadar dostum. Dahası gelecek. Şimdilik burada kestim çünkü buraya kadar gelmek bile çok zordu. Hikaye, kod ile ilgili görüş ve soruların olursa bana söyle.")