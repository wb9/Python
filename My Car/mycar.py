# wpisywanie danych
# json
# 1.06 - 99.99 zł 147053
# 7.06 - ilość km - 147256, prędkość średnia - 31km/h, czas podróży 6:22, zasięg 230km, odległość przejechana 203.4 km,
# zużycie średnie 7.3l/100km, cena za paliwo 5.05 zł/l
# 10.06 - zatankowane za 100.04 zł
# 14.06 - ilość km - 147382, prędkość średnia - 25km/h, czas podróży 12:56, zasięg 342km, odległość przejechana 329.6 km,
# zużycie średnie 8.5l/100km,
# 19.06 - zatankowane za 100.10 zł - 20.64l - 4.85 zł/l
# 21.06 - ilość km - 147589, prędkość średnia - 27km/h, czas podróży 19:39, zasięg 479km, odległość przejechana 536.5 km,
# zużycie średnie 8l/100km,
# 28.06 - ilość km - 147670, prędkość średnia - 26km/h, czas podróży 23:41, zasięg 264km, odległość przejechana 617.5 km,
# zużycie średnie 8.1l/100km,
# 5.07 - zatankowane za 100.01 zł - 20.62l - 4.85 zł/l
# 5.07 - ilość km - 147762, prędkość średnia - 24km/h, czas podróży 28:38, zasięg 50km, odległość przejechana 709.9 km,
# zużycie średnie 8.4l/100km,


# ile kosztuje mnie kilometr, ile dzień
# średni czas podróży
# średnie spalanie


day = int(input("Który dziś dzień czerwca? "))
km = int(input("Ile kilometrów przejechałem? "))
hours = float(input("Ile godzin spędziłem w samochodzie? "))
money = float(input("Ile wydałem na paliwo? "))

how_many_km_per_day = str(km/day)
how_many_hours_per_day = str(hours/day)
money_per_km = str(money/km)
money_per_day = str(km/day)

money = str(money)
day = str(day)





average_speed = 4

print("Dziennie przejeżdżam " + how_many_km_per_day + " kilometrów dziennie.")
print("Dziennie spędzam w samochodzie " + how_many_hours_per_day + " godzin.")
print("Wydałem " + money + " zł na paliwo w ciągu " + day + " dni, tj. " + money_per_km + " zł na kilometr, " + money_per_day + " na dzień.")

