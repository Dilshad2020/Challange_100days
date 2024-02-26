print("Salam,icazə almaq sisteminə xoş gəlmisiniz.")
ad=input("Zəhmət olmasa adınızı qeyd edin: ")
soyad=input("Zəhmət olmasa soyadınızı qeyd edin: ")
fakulte=input("Zəhmət olmasa fakültənizi qeyd edin: ")
qrup_n=input("Zəhmət olmasa qrup nömrənizi  qeyd edin: ")
kurs=input("Zəhmət olmasa neçənci kurs olduğunuzu qeyd edin: ")
icaze_gunu=input("Tarixi qeyd edin: ")
icaze_muddeti=input("Müddəti qeyd edin (saat və ya gün): ")
icaze_sebebi=input("Səbəbinizi qeyd edin: ")

 # xahiş edirəmki coğrafiya fakültəsinin 970-ci qrupunun 3-cü kurs tələbəsi Tamerlan Xəlliliyə
 # öz şəxsi işiylə bağlı olaraq 3 saatlıq icazə verəsiniz.
print(f"""           ƏRİZƏ         
Xahiş edirəm ki,{fakulte} fakültəsinin {qrup_n}-ci qrupunun {kurs}-cü kurs tələbəsi {ad} {soyad}-yə
{icaze_sebebi} {icaze_muddeti} icazə verəsiniz.""")

print(f"Ərizəniz uğurla {icaze_gunu} tarixi üçün  qeydə alındı ")
