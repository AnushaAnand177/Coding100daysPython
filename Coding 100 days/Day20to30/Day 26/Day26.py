import json
data = {
    "name": "Lucy",
    "age": 30,
    "skills": ["Python", "Data Analysis", "Machine Learning"]
}

# Pretty print JSON
print(json.dumps(data, indent=4))

print(json.dumps(data, indent=4, sort_keys=True))





