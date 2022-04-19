a = input("Masukan Nama Siswa  : ")
b = input("Masukan NIS Siswa   : ")
c = int(input("Masukan Nilai Siswa : "))
if c >= 80:
    d = 'A'
elif c >= 70:
    d = 'B'
elif c >= 60:
    d = 'C'
elif c >= 50:
    d = 'D'
else:
    d = 'E'
print("===================================")
print("              DATA SISWA        ")
print("===================================")
print("Nama Siswa  : ", a)
print("NIS Siswa   : ", b)
print("Grade       : ", d)
print("==================================")