import os
txt_file_path = os.path.join(os.path.dirname(__file__), 'readme.txt')
# explizit mit close()-Befehl
datei = open(txt_file_path, "r", encoding="utf-8")
zeilen = datei.read()
print(zeilen)
datei.close()

# abgesichert durch with-Statement
with open(txt_file_path, "r", encoding="utf-8") as datei:
    zeilen = datei.read()
    # wird auch geschlossen, wenn ein Error geworfen !

print(zeilen)

