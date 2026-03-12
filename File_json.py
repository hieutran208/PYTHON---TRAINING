import json

data = {
    "id": "001",
    "name": "Hieu",
    "age": 25,
    "skills": ["Python", "SQL"]
}

with open('exp.json',mode='w',encoding='utf-8') as file:
    json.dump(data,file,indent=4) # indent = 4: Xuống dòng và thụt vào 4 dấu cách (nếu không có thì kqua sẽ dưới dạng 1 dòng)
    json.dumps(data, indent=4) # json.dump là ghi vào file, còn json.dumps là chuyển thành chuỗi để in ra trực tiếp
    print(json.dumps(data, indent=4))
                                         