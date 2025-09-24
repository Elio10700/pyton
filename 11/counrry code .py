# get the country code

country_code = {
    "India": "0091",
    "Nepal": "0977",
    "Qatar": "0974"
}

print("The country code for India : ", country_code.get("India", "not found"))
print("The country code for Japan : ", country_code.get("Japan", "not found"))
