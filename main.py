import random, string

amount = int(input('Üretilecek kod sayısını gir: '))
value = 1
while value <= amount:
    code = "https://discord.gift/" + ('').join(random.choices(string.ascii_letters + string.digits, k=16))
    f = open('ghostcodes.txt', "a+")
    f.write(f'{code}\n')
    f.close()
    print(f'[ÜRETİLDİ] {code}')
    value += 1
