# -*- coding: utf-8 -*-

#Calculator.py kodu

# Basit Hesap Makinesi (tekrar işlem, ^ ve sqrt, geçmiş)
# Python 3.x

import math

HISTORY = []  # işlem geçmişi

def toplama(a, b):        return a + b
def cikarma(a, b):        return a - b
def carpma(a, b):         return a * b
def bolme(a, b):
    if b == 0:
        raise ZeroDivisionError("0'a bölme tanımsızdır.")
    return a / b
def us_al(a, b):          return a ** b
def karekok(a):
    if a < 0:
        raise ValueError("Negatif sayının karekökü reel sayı değildir.")
    return math.sqrt(a)

def format_islem_str(op, *args):
    """Geçmiş listesi için okunaklı işlem metni üretir."""
    if op == "sqrt":
        return f"√({args[0]})"
    symbol = {"+" : "+", "-" : "-", "*" : "*", "/" : "/", "^": "^"}.get(op, op)
    return f"{args[0]} {symbol} {args[1]}"

def hesapla(op):
    """Kullanıcı girdilerini alır, sonucu döndürür ve geçmişe yazar."""
    if op == "sqrt":
        a = float(input("Sayıyı gir: "))
        sonuc = karekok(a)
        HISTORY.append(f"{format_islem_str(op, a)} = {sonuc}")
        return sonuc

    # İkili işlemler
    a = float(input("Birinci sayıyı gir: "))
    b = float(input("İkinci sayıyı gir: "))

    if op == "+":   sonuc = toplama(a, b)
    elif op == "-": sonuc = cikarma(a, b)
    elif op == "*": sonuc = carpma(a, b)
    elif op == "/": sonuc = bolme(a, b)
    elif op == "^": sonuc = us_al(a, b)
    else:
        raise ValueError("Geçersiz işlem.")

    HISTORY.append(f"{format_islem_str(op, a, b)} = {sonuc}")
    return sonuc

def menuyu_yazdir():
    print("\n=== Basit Hesap Makinesi ===")
    print("İşlemler:")
    print("  +  toplama")
    print("  -  çıkarma")
    print("  *  çarpma")
    print("  /  bölme")
    print("  ^  üs alma (a^b)")
    print("  sqrt  karekök (√a)")
    print("Komutlar:")
    print("  h  geçmişi göster")
    print("  q  çıkış")

def gecmisi_goster():
    if not HISTORY:
        print("Geçmiş boş.")
        return
    print("\n--- İşlem Geçmişi ---")
    for i, kayit in enumerate(HISTORY, 1):
        print(f"{i}. {kayit}")
    print("----------------------")

def main():
    while True:
        menuyu_yazdir()
        secim = input("Seçiminiz (+, -, *, /, ^, sqrt, h, q): ").strip().lower()

        if secim == "q":
            print("Program sonlandırıldı. Görüşmek üzere!")
            break
        if secim == "h":
            gecmisi_goster()
            continue

        try:
            sonuc = hesapla(secim)
            print("Sonuç:", sonuc)
        except ZeroDivisionError as zde:
            print("Hata:", zde)
        except ValueError as ve:
            print("Hata:", ve)
        except Exception as e:
            print("Beklenmeyen hata:", e)

        # (1) Tekrar işlem sorusu
        devam = input("Devam etmek ister misiniz? (E/H): ").strip().lower()
        if devam == "h":
            print("Program sonlandırıldı. Görüşmek üzere!")
            break

if __name__ == "__main__":
    main()







    
