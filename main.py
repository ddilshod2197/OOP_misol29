class Oyin:
    def __init__(self, jamoa1, jamoa2, hisob="0:0"):
        self.jamoa1 = jamoa1
        self.jamoa2 = jamoa2
        self.hisob = hisob

class Stadion:
    def __init__(self, nomi):
        self.nomi = nomi
        self.oyinlar = []
    
    def oyin_qosh(self, oyin):
        self.oyinlar.append(oyin)
        print(f"✅ {oyin.jamoa1} vs {oyin.jamoa2} o‘yini qo‘shildi.")
    
    def oyinlar_royxati(self):
        print(f"\n🏟️  {self.nomi} stadionidagi o‘yinlar:")
        for o in self.oyinlar:
            print(f"• {o.jamoa1} vs {o.jamoa2} — Hisob: {o.hisob}")

# Test
stadion = Stadion("Milliy Stadion")
stadion.oyin_qosh(Oyin("Paxtakor", "Lokomotiv", "2:1"))
stadion.oyin_qosh(Oyin("Bunyodkor", "Nasaf", "0:0"))
stadion.oyinlar_royxati()
