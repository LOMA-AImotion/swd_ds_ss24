try:
    netto_preis = float(input("Preis in netto?"))
except ValueError as ve:
    print(ve)
else:
    print("Alles gut")
finally:
    print("Jetzt noch aufräumen")
