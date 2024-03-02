print("Xəzinə adası oyununa xoş gəlmisiniz: ")
seçim=str(input("seçim edin sağ yoxsa sol:? "))
if seçim=="sağ":
    print("siz düzgün seçim etdiniz növbəti mərhələ ilə davam edirsiniz: ")
    seçim=(input("seçim edin üzmək yoxsa gözləmək:? "))
    if seçim=="gözləmək":
        print("siz düzgün seçim etdiniz və növbəti mərhələ ilə davam edirsiniz: ")
        seçim=(input("seçim edin qırmızı qara yoxsa sarı:? "))
        if seçim=="qırmızı":
           print("siz düzgün seçim etdiniz və növbəti mərhələ ilə davam edirsiniz: ")
    elif seçim=="sarı":
        print("siz düzgün seçim etmədiniz.Oyun sonlandırıldı: ")
    else:
        print("siz düzgün seçim etmədiniz.Oyun sona çatdı:")