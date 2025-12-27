import random

cowok = [
    "Kamu lagi ngapain?",
    "Capek banget hari ini.",
    "Aku kepikiran kamu tadi.",
    "Laper tapi males keluar.",
    "Cuacanya aneh ya hari ini.",
    "Kadang hidup tuh lucu.",
    "Aku pengen tidur lama.",
    "Kerjaan numpuk banget.",
    "Aku ngerasa hari ini panjang.",
    "Pernah nggak kamu ngerasa kosong?"
]

cewek = [
    "Lagi santai aja.",
    "Iya, aku juga capek.",
    "Kenapa kepikiran?",
    "Makan aja dulu.",
    "Iya, panas terus hujan.",
    "Hidup emang gitu.",
    "Tidur bentar enak sih.",
    "Sabar ya.",
    "Hari ini kerasa berat.",
    "Aku juga sering ngerasa gitu."
]

reaksi = [
    "Hehe.",
    "Hmm.",
    "Iya juga sih.",
    "Bener banget.",
    "Aku ngerti.",
    "Masuk akal.",
    "Kadang gitu ya.",
    "Entahlah.",
    "Aku mikir juga gitu.",
    "Yaudah jalani aja."
]

with open("percakapan_sejuta_baris.py", "w", encoding="utf-8") as f:
    for _ in range(1_000_000):
        siapa = random.choice(["cowok", "cewek", "reaksi"])

        if siapa == "cowok":
            kalimat = f'print("Cowok: {random.choice(cowok)}")\n'
        elif siapa == "cewek":
            kalimat = f'print("Cewek: {random.choice(cewek)}")\n'
        else:
            kalimat = f'print("{random.choice(reaksi)}")\n'

        f.write(kalimat)

print("Selesai. File percakapan_sejuta_baris.py berhasil dibuat.")
