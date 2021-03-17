#isi nama teman sebanyak 10 list
teman = ["Efa", "Erysa", "Tsania", "Gea", "Candrika", "Funny", "Ara", "Divana", "Hana", "Angela"]

#tampilkan list index nomor 4, 6, 7
print("teman[4]", teman[4])
print("teman[6]", teman[6])
print("teman[7]", teman[7])

#ganti nama teman yang berada pada list 3, 5, 9
teman[3] = "Issa"
teman[5] = "Rana"
teman[9] = "Rara" 
print(teman)

#tambahkan 2 nama temanmu
teman.append("Nadiya")
teman.append("Mira")
print(teman)

#tampilkan semua teman dengan pengulangan
['teman'] * 2
print(teman)

#tampilkan panjang list
len(teman)
print(len(teman))