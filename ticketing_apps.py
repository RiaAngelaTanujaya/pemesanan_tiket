from os import system
import time

def checker(password_admin, password_user):
	if password_admin == password_user:
		return True
	else:
		print("Password salah")
		return None

def create_password(password_admin):
	return lambda x:checker(password_admin,x)

def display_ticket(kode):
	return database_transaksi.get(kode)

def checking_answer(ans):
	ans = ans.lower()
	if ans =="ya":
		return True
	elif ans == "y":
		return True
	else:
		return False

def print_header(snd):
	system("cls")
	print(snd)


def destination_option():
	print_header("""
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		PILIHAN DESTINASI
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		""")
	data_tujuan = """
	1.BALI
	2.JAKARTA
	3.PALEMBANG
	4.SURABAYA
	5.NTB
	"""
	print(data_tujuan)

	kota_tujuan = {
		1 : "BALI",
		2 : "JAKARTA",
		3 : "PALEMBANG",
		4 : "SURABAYA",
		5 : "NTB"
	}
	tujuan = int(input("Masukkan pilihanmu\t:"))
	while tujuan not in kota_tujuan:
		print("Pilihanmu Belum Tersedia...")
		tujuan = int(input("\nMasukkan pilihanmu\t:"))
	return kota_tujuan.get(tujuan)

def hometown():
	print("""
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~
		KOTA ASAL
	~~~~~~~~~~~~~~~~~~~~~~~~~~~~
	""")
	data_asal = """
	1.BALI
	2.JAKARTA
	3.PALEMBANG
	4.SURABAYA
	5.NTB
	"""
	print(data_asal)

	kota_asal = {
	 	1 : "BALI",
		2 : "JAKARTA",
		3 : "PALEMBANG",
		4 : "SURABAYA",
		5 : "NTB"
	}
	asal = int(input("Masukkan pilihanmu\t:"))
	while asal not in kota_asal:
		print("Pilihanmu Belum Tersedia...")
		asal = int(input("Masukkan pilihanmu\t:"))
	return kota_asal.get(asal)

def date():
	tanggal = int(input("Tanggal\t:"))
	while tanggal not in range(1,32):
		print("\nMasukkan kembali tanggal")
		tanggal = int(input("Tanggal(1-31)\t:"))

	bulan = int(input("Bulan\t:"))
	while bulan not in range(1,13):
		print("\nMasukkan kembali bulan")
		bulan = int(input("Bulan(1-12)\t:"))

	tahun = int(input("Tahun\t:"))
	while tahun not in range (2020,2021):
		print("Permintaan Belum Tersedia....")
		print("\nMasukkan tahun saat ini") 
		tahun = int(input("Tahun\t:"))
	return str(tanggal)+"-"+str(bulan)+"-"+str(tahun)

def number_of_passengers():
	penumpang = int(input("Banyak penumpang\t:"))
	while penumpang == 0:
		print("\nMasukkan kembali")
		penumpang = int(input("Banyak penumpang\t:"))
	return penumpang

def class_of_flight():
	kelas1 = "ekonomi"
	kelas2 = "bisnis"
	kelas = input("Kelas (ekonomi/bisnis)\t:")
	while kelas != kelas1 and kelas != kelas2:
		print("\nMasukkan kelas sesuai dengan pilihan yang ada")
		kelas = input("kelas\t:")
	return kelas
	
def airlines():
	print("~~~~~~~~~~~~~~~~\n PILIHAN MASKAPAI \n~~~~~~~~~~~~~~~~~")
	maskapai = """
	1.Garuda Indonesia
	2.Lion 
	3.Sriwijaya
	4.Batik
	5.Citilink
	"""
	print(maskapai)
	data_maskapai = {
		1:"Garuda Indonesia",
		2:"Lion",
		3:"Sriwijaya",
		4:"Batik",
		5:"Citilink"
	}
	pilihan = int(input("Masukkan pilihanmu\t:"))
	while pilihan not in data_maskapai:
		print("Pilihanmu Belum Tersedia...")
		pilihan = int(input("Masukkan pilihanmu\t:"))
	return data_maskapai.get(pilihan)

def rincian_harga(tujuan,asal,penumpang,kelas,maskapai):
	database_harga_asal = {
		"BALI": 200000,
		"JAKARTA": 150000,
		"PALEMBANG": 75000,
		"SURABAYA": 175000,
		"NTB":300000
		}
	database_harga_tujuan = {
		"BALI" : 250000,
		"JAKARTA": 100000,
		"PALEMBANG": 135000,
		"SURABAYA": 200000,
		"NTB": 300000
		}

	database_harga_kelas = {
		"ekonomi": 1,
		"bisnis" : 2.5
		}
	database_harga_maskapai = {
		"Garuda Indonesia": 50000,
		"Lion": 25000,
		"Sriwijaya": 35000,
		"Batik": 40000,
		"Citilink": 30000
		}

	harga = penumpang * (database_harga_tujuan.get(tujuan)+database_harga_asal.get(asal)+database_harga_maskapai.get(maskapai))*database_harga_kelas.get(kelas)
	return harga

def kesepakatan_penumpang():
	pilihan = input("Yakin dengan pilihan Anda (ya/tidak)\t:")
	if pilihan == "ya":
		print("Tunggu Sebentar...")
		time.sleep(2)
		input("Tekan 'Y' untuk melanjutkan proses pembayaran\t: ")
		return True
	else:
		time.sleep(2)
		return False

def data_penumpang(byk_penumpang):
	my_dict = {}
	for a in range (byk_penumpang):
		print_header("")
		nama =str(input("nama penumpang\t:"))
		telp = int(input("nomor telefon\t:+62"))
		email = input("alamat email\t:")
		nomor_ktp = int(input("no.ktp\t:"))	
		my_dict[nomor_ktp] = {"nama": nama,
		"telp": telp,
		"email":email,
		"nomor_ktp" : nomor_ktp}
	return my_dict

def menu1():
	a = destination_option()
	b = hometown()
	c = date()
	d = number_of_passengers()
	e = class_of_flight()
	f = airlines()
	print(a,b,c,d,e,f)
	g = rincian_harga(a,b,d,e,f)
	print(g)
	while not kesepakatan_penumpang():
		a = destination_option()
		b = hometown()
		c = date()
		d = number_of_passengers()
		e = class_of_flight()
		f = airlines()
		g = rincian_harga(a,b,d,e,f)
	info_pembeli = data_penumpang(d)
	my_dict = {"tujuan":a,
				"asal":b,
				"tanggal" :c,
				"penumpang":d,
				"kelas penerbangan":e,
				"maskapai":f,
				"harga":g,
				"data_pembeli": info_pembeli
		}
	return(my_dict,info_pembeli)

database_transaksi = {}
database_penumpang = {}

def menu_utama():
	system("cls")
	menu = """
	~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~
	 		PEMESANAN TIKET PESAWAT		
	~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~%~
	[1]BOOKING TIKET
	[2]TAMPILKAN TIKET
	
	"""
	print(menu)
	pilihan = int(input())
	if pilihan == 1:
		pesanan, pembeli = menu1()
		kode_booking = str(time.time())
		database_transaksi[kode_booking] = pesanan
		for penumpang in pembeli:
			nomor_ktp = pembeli[penumpang]["nomor_ktp"]
		database_penumpang[nomor_ktp] = pembeli[penumpang]
		return ("Pembelian Berhasil, Transaksi Tercatat.")
	elif pilihan == 2:
		kode_booking = input("Masukkan Kode Booking\t:")
		pesanan = display_ticket(kode_booking)
		if not pesanan:
			return "Kode Booking Belum Tercatat."
		return pesanan

def standby():
	print_header("")
	menu = """
	!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!
	[1] Pesan Tiket
	[2] Admin
	[3] Exit
	!~!~!~!~!~!~!~!~!~!~!~!~!~!~!~!
	"""
	print(menu)
	pilihan = int(input())
	if pilihan == 1:
		return menu_utama()
	elif pilihan == 2:
		password = input("Masukkan password\t:")
		if system_admin(password):
			menu2 = """
			@@~~@@~~@@~~@@~~@@~~@@~~@@
			[1] data transaksi
			[2] data penumpang
			@@~~@@~~@@~~@@~~@@~~@@~~@@
			"""
			print(menu2)
			pilihan2 = int(input("Masukkan pilihan\t:"))
			if pilihan2 == 1:
				return database_transaksi
			elif pilihan2 == 2:
				return database_penumpang
		else:
			return ""
	elif pilihan == 3:
		print("The program has stopped")
		return False

def program_on():
	while True:
		x = standby() 
		if x == False:
			break
		print(x)
		selesai = input("selesai? (Y) :")
		while selesai != "Y":
			selesai = input("selesai? (Y):")

system_admin = create_password(input("pilih password untuk system\t:"))
program_on()

