print("Pizza Mizza restoranına xoş gəlmisiniz")
input("zəhmət olmasa menyumuzla tanış olun və sifarişinizi qeyd edin: ")
ölçü=input("Seşdiyiniz pizza hansı ölçüdə olsun? (15 sm,20 sm,25 sm): ")
növ=input("Pepperoni, marqarita, vegetarian və 4 fəsil pizza növlərindən birini seçin: ")
əlavə_bibər=input("pizzanız əlavə bibərli olsunmu? bəli xeyr? ")
qiymet=0
if ölçü=="15":
    qiymet +=18
elif ölçü=="20":
    qiymet +=22
else:
    qiymet +=26
    if əlavə_bibər=="bəli":
        if ölçü=="25":
            qiymet +=5

print(f"sizin yekun hesabınız: {qiymet}m.")
print("Bizi seçdiyiniz üçün təşəkkürlər!")



