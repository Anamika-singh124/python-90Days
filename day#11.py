student = {
    "name": "anamika",
    "age" : 18,
    "course": "python"
}
print(student)
print(student["name"])
print(student.get("age"))
student["age"] = 19
print(student)
student["city"] = "prayagraj"
print(student)
student.pop("age")
print(student)
del student["course"]
print(student.keys())
print(student.values())
print(student.items())
for key,value in student.items():
    print(key,value)
student = {
    "student1":{
        "name": "anamika",
        "age": 18
    },
    "student2" :{
        "name": "riya",
        "age": 19
    }
}
print(student["student1"]["name"])