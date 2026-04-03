import re
text = "abc123xyz"
str = "The rain in Spain" 
search  = re.search(r"\s",str)
search_all  = re.findall(r"\s",str)
print(f'Vị trí khoảng trắng đầu tiên trong chuỗi str là: {search.start()}')
print(f'Vị trí khoảng trắng cuối cùng trong chuỗi str là: {search.end()}')
print(f'Các kí tự khoảng trắng trong chuỗi str là: {search.group()}')
print(f'Số lần xuất hiện khoảng trắng trong chuỗi str là: {len(search_all)}')
print(re.findall(r"b",text))
print(re.findall(r"[0-9]{3}",text))
print(re.sub("\s","9",str))