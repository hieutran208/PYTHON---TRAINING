import json

data = {
    "id": "001",
    "name": "Hiếu",
    "age": 25,
    "skills": ["Python", "SQL"]
}

with open('exp.json',mode='w',encoding='utf-8') as file:
    json.dump(data, file, indent=4, ensure_ascii=False) # indent = 4: Xuống dòng và thụt vào 4 dấu cách (nếu không có thì kqua sẽ dưới dạng 1 dòng)
    json.dumps(data, indent=4, ensure_ascii=False) # json.dump là ghi vào file, còn json.dumps là chuyển thành chuỗi để in ra trực tiếp
    print(json.dumps(data, indent=4, ensure_ascii=False)) # ensure_ascii=False → giữ nguyên ký tự Unicode (thường dùng khi có tiếng Việt)
    # ensure_ascii=True => File JSON chỉ chứa ký tự ASCII. Tất cả kí tự Unicode sẽ bị chuyển thành dạng \uXXXX.