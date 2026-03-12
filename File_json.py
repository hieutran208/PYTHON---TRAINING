import json

dict_data = {
 "user":[
    {"id":1,"name":"An"},
    {"id":2,"name":"Binh"}
 ],
 "skills":["Python","SQL"],
 "address":{
    "city":"Hanoi",
    "country":"Vietnam"
 }
}
# Ghi file .json
with open('exp.json',mode='w',encoding='utf-8') as file:
    json.dump(dict_data, file, indent=4, ensure_ascii=False) 
    json.dumps(dict_data, indent=4, ensure_ascii=False)
    print(json.dumps(dict_data, indent=4, ensure_ascii=False))
# Đọc file .json
with open('exp.json',mode='r',encoding='utf-8') as file: # encoding="utf-8" để tránh lỗi Unicode
    data = json.load(file)
    print(data)
    print(type(data)) 
    print(data["skills"]) # có thể dùng data.get("name") để truy cập dữ liệu
    print(data["address"]["city"]) # Đọc JSON lồng nhau
    print(data["skills"][0]) # Data có list bên trong Object
    for user in data["user"]: # data["user"] là một list => Truy cập vào các phần tử trong list
        print(f"ID: {user["id"]} Tên: {user["name"]}")