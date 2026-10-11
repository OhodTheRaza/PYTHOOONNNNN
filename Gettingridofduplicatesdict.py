student_data = {
    "id1" : {"name": "Sarah", "class": "V", "subject": "maths, science, english"},
    "id2" : {"name": "Zubair", "class": "V", "subject": "maths, science, english"},
    "id3" : {"name": "Sarah", "class": "V", "subject": "maths, science, english"},
    "id4" : {"name": "David", "class": "V", "subject": "maths, science, english"},
}
result = {}
seen_keys = []
for student_id, details in student_data.items():
    unique_key = (details["name"], details["class"], details["subject"])
    if unique_key not in seen_keys:
        seen_keys.append(unique_key)
        result[student_id] = details
for k, v in result.items():
    print(k, ":", v)
