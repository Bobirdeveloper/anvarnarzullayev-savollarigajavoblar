# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir
# kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring.
python_words = {
    'integer': 'Butun son',
    'float': "O'nlik son",
    'boolean': "Mantiqiy qiymat",
    'for': "Biror amalni qayta-qayta bajarish tsikli",
    'if': 'Shartlarni tekshirish operatori'}
print("Lug'at elemetlari")
for a, b in python_words.items():
    print(f"Kalit=={a} qiymat=={b}")
# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida,
# alifbo ketma-ketligida konsolga chiqaring.
davlatlar = {
    "o'zbekiston": 'toshkent',
    'aqsh': 'washington d.c.',
    'rossiya': 'moskva',
    'tojikiston': 'dushanbe',
    "qirg'iziston": 'bishkek',
    'qozog\'iston': 'nursulton',
    'malayziya': 'kuala-lumpur',
    'singapur': 'sungapur',
    'italiya': 'rim'}
print("Davlat nomlari:")
for a in sorted(davlatlar.keys()):
    print(a)
print("Poytaxt nomlari:")
for a in sorted(davlatlar.values()):
    print(a)
