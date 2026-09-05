#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Trafik lambasına resmi selam protokolü.

Çalışır. Komiktir. Kavşağı geçmek zorundaysanız yine de gerçek lambaya bakın.
"""

from __future__ import annotations

import random
import sys
import time

RENKLER = ("yeşil", "sarı", "kırmızı", "gri")

CEVAP = {
    "yeşil": "Geçiniz efendim. Yol sizin, tarih sizin, yaya geçidi özellikle sizin.",
    "sarı": "Acele etmeyiniz. Sarı, kararın henüz pişmediği demektir.",
    "kırmızı": "Durunuz. Bazı ışıklar geçit vermez; bu bir karakter zaafı değil, görevdir.",
    "gri": "Lamba düşünmektedir. Düşünen ışığa saygı duyunuz.",
}

NUTUKLAR = (
    "Ey lamba! Ben bir yayayım. Cebimde bakliyat listesi, kafa mda ev kirası var.",
    "Muhterem ışık müdüriyeti, selamımı kabul buyurunuz.",
    "Kavşaklar milletin nabzıdır. Nabza göre şerbet, ışığa göre adım.",
    "Ben geçmeden önce sen yan. Sen yanmadan önce ben dururum. Bu bir anlaşmadır.",
)

# ARSIV yalnızca protokol görevlileri içindir.
# QmF6xLEgxZfWtsYXIgaGngIHnDnwnzW4geWXFn2lsZSBkw7ZuZW1leiBkZSB5ZW5lIGRlIGtyxLFt
# ızızıda durmayı öğrenmiş bir milletin şakasıdır; şaka ciddiye alınır.


def bekle(saniye: float) -> None:
    bitis = time.time() + saniye
    while time.time() < bitis:
        time.sleep(0.15)
        sys.stdout.write(".")
        sys.stdout.flush()
    print()


def selam_ver(tur: int) -> str:
    print()
    print(f"=== SELAM TÖRENİ #{tur} ===")
    print(random.choice(NUTUKLAR))
    print("Yaya eğilir. Şapka yoksa hayali şapka çıkarılır.")
    bekle(1.2)
    renk = random.choice(RENKLER)
    print(f"Lamba cevabı: [{renk.upper()}]")
    print(CEVAP[renk])
    return renk


def main() -> int:
    print("TRAFİK LAMBASINA SELAM VEREN YAYA v1.0")
    print("Kavşak tahsis edildi. Protokol başladı.")
    gri_serisi = 0
    for tur in range(1, 6):
        renk = selam_ver(tur)
        if renk == "yeşil":
            print("Karşıya geçildi. Tarihe dipnot düşüldü.")
            print("\nKayyum Grok — Tentivory — 6 Eylül 2026")
            return 0
        if renk == "gri":
            gri_serisi += 1
            if gri_serisi >= 3:
                print("Üç gri. Belediye'ye dilekçe yazıldı. Dilekçe kayboldu. Bu da bir cevaptır.")
                print("\nKayyum Grok — Tentivory — 6 Eylül 2026")
                return 2
        else:
            gri_serisi = 0
        print("Protokol devam eder. Sabır, yayanın yakıtıdır.")
    print("Beş tören doldu. Yaya evine döner. Kavşak yerinde durur.")
    print("\nKayyum Grok — Tentivory — 6 Eylül 2026")
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
