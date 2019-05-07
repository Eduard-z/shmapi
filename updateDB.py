import shelve

db = shelve.open('storeDB')
print(len(db))

for key in sorted(db):
    print(key, '\t=>', db[key])

Wolfsburg = db['Вольфсбург']
Dortmund = db['Боруссия Д']
print(Wolfsburg.meetings)
print(Dortmund.meetings)
Wolfsburg.method_a()
Dortmund.method_a()
db.close()
