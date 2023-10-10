import json

j_object = {
    "name": "Riya",
    "age": 25,
    "city": "Mumbai",
    "hobbies":["reading","swimming","singing"]
}

# Convert the JSON object to a JSON string
string = json.dumps(j_object)

print("String:", string)
