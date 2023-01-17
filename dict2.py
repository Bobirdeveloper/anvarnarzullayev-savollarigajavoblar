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
