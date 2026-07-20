# dosya işlemleri => file operations
# Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır.
# Kullanımı: open(dosya_adı, dosya_erişme_modu)
# dosya_erişme_modu => Dosyayı hangi amaçla açmak istediğimizi belirtir. (okuma, yazma, ekleme vb.)

# "w"  -> yazma (write, dosya varsa içeriğini siler, yoksa oluşturur)
# file = open("bolum-11/newfile.txt", "w", encoding="utf-8")
# file.write("Selim Şen")
# file.close()

# "a"  -> ekleme (append, mevcut içeriğin sonuna ekler)
file = open("bolum-11/newfile.txt", "a", encoding="utf-8")
file.write("Ahmet Şen\n")
file.close()

# "x"  -> oluşturma (dosya zaten varsa hata verir)
file = open("bolum-11/newfile2.txt", "x", encoding="utf-8")
# "r"  -> okuma (read, varsayılan)
