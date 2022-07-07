# Kredit Oleh MisterAM

impor os,sys,waktu,permintaan

dari waktu impor tidur

a,m,h,k,b,u,bm,p,bn,o = [

'\033[90m',

'\033[31m',

'\033[32m',

'\033[33m',

'\033[94m',

'\033[35m',

'\033[36m',

'\033[37m',

'\033[41m',

'\033[0m'

]

#mengetik otomatis

def mengetik(z):

    untuk e dalam z + "\n":

      sys.stdout.write(e)

      sys.stdout.flush()

      waktu.tidur(0.05)

os.system('hapus')

print ('\033[36;1mBerlangganan yt ku ngab \033[37mClover \033[36mok! :v')

os.system('termux-open-url https://youtube.com/channel/UCMkyXfqqWm_uuMh2UBOHc8w')

tidur(5)

os.system('hapus')

print ('\033[36;1mSubs juga chanelnya \033[37;1myg ngasih source ngab :v')

os.system('xdg-open https://youtube.com/channel/UCRaVHUXQGVAH7Gof7kixIoQ')

tidur(3)

os.system('hapus')

# Ubah Terserah kalian

spanduk = """

\033[31;1m \033[31;1m ████╗ ██╗ ██╗

\033[31;1m \033[31;1m ═══╝██╔══██╗██║ ██║

\033[31;1m \033[31;1m ███████║██║ ██║

\033[37;1m \033[37;1m █╔══██║██║ ██║

\033[37;1m \033[37;1m █║███████╗███████╗

\033[37;1m \033[37;1m ═════╝╚══════╝

\033[33;1m╔═══════════════════════════════════════════ ═════╗

\033[33;1m║ \033[36;1m [•] Penulisan : Semanggi \033[33;1m

\033[33;1m║ \033[36;1m [•] gitHub : https:github.com/CloverID10 \033[33;1m

\033[33;1m║ \033[36;1m [•] Kredit : MisterAM \033[33;1m

\033[33;1m╚═══════════════════════════════════════════ ═════╝

\033[36;1m╔═══════════════════════════╗

\033[36;1m║\033[33;1m GUNAKAN DENGAB BIJAK YA\033[36;1m

\033[36;1m╚═══════════════════════════╝"""

tidur(1)

cetak (spanduk)

# Jagan di ubah sayang

cetak ("")

print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m PILIHAN Nomor \033[1;33m• \033[ 0m\033[1;30m]══════════════>")

cetak ("")

print ("\033[37m[\033[31m•\033[37m]\033[32m Contoh nomor\033[37m : \033[37m\033[33m8Xxx\033[33m")

nomor = input("\033[37m[\033[31m•\033[37m]\033[32m Nomor Target\033[32m \033[37m:\033[37m\033[33m ")

print ("\033[1;30m<════════════[\033[1;33;41m • \033[1;37m MASUKAN JUMLAH \033[1;33m• \033[ 0m\033[1;30m]══════════════>")

jumlah = int(input("\033[37m[\033[31m•\033[37m]\033[32mJumlah Spam\033[37m :\033[37m\033[33m "))

mengetik("[KALO SUDAH LIMIT TUNGUH BEBERAPA MENIT LAGI BARU ULANGI NGAB :V] ")

waktu.tidur(3)

# Jagan di ubah sayang ku

url = "https://id.jagreward.com/member/verify-mobile/"

ua = {'Host': "id.jagreward.com",'Connection': "keep-alive",'User-Agent': 'Mozilla/5.0 (Linux; Android 8.1.0; vivo 1724) AppleWebKit/537.36 ( KHTML, seperti Gecko) Chrome/77.0.3865.73 Mobile Safari/537.36'}

dat = {"metode": "PANGGILAN","kode negara": "id",}

# Jagan di ubah sayng

untuk i dalam kisaran (jumlah):

    kirim = request.post(url+nomor, header=ua, data=dat)

    print(" [â€¢] Status ~+> ",(send.json()["pesan"]))
