

student_data = {
    "id1": {
        "name": "Sara",
        "age": 12,
        "subject": ["english", "maths", "science"]
    },
    "id2": {
        "name": "James",
        "age": 14,
        "subject": ["english", "maths", "Commerce"]
    },
    "id3": {
        "name": "Sara",
        "age": 12,
        "subject": ["english", "maths", "science"]
    },
    "id4": {
        "name": "David",
        "age": 12,
        "subject": ["english", "maths", "Computer"]
    }
}
result = {}
for key,value in student_data.items():
        if value not in result.values():
                result[key] = value
print("the dictionary without duplicties:")
print(result)