record = {"name":"creta",
          "company":"hyundai",
          "price":"19L",
          "milage":"18km"}
print(record)
print(record["name"])
for i in record:
    print(i)

print(record.get("company"))

record["color"]="red"
print(record)
record["color"]="white"
print(record)
del record["milage"]
print(record)
record.pop("color")
print(record)
dict = {}
dict = record.copy()
print(dict)
print(record.keys())
print(record.values())
for i in record.values():
    print(i)
    