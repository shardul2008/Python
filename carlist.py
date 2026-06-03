cars = ["creta","elantra","punch","safari","venue"]
for car in cars:
    print(car)

cars = [{"name":"Creata", "company":"hyundai", "milage":18},
        {"name":"elantra","company":"hyundai","milage":15},
        {"name":"punch","company":"tata","milage":19},
        {"name":"swift","company":"suzuki","milage":20} 
        ]

for car in cars:
    print(car["name"] +" - "+ str(car["milage"])) 