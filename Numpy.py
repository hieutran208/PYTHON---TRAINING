import numpy as np
# Array 1 chiều
arr1 = np.array([1,2,3,4]) 
# Array 2 chiều
arr2 = np.array([
    [1,2,3],
    [4,5,6]
]) 
arr3 = np.zeros(5) # Tạo mảng có 5 phần tử  = 1: np.ones(5)
print(arr3) # Mảng có 5 phần tử có giá trị 0 => Output: [0. 0. 0. 0. 0.]
print(arr1[1]) # truy cập phần tử trong mảng => Output: 2
print(arr1[2:4]) # truy cập từ phần tử arr1[2] đến arr1[3] => Output: [3 4]
print(arr2.shape) # In ra kích thước mảng => Output: (2, 3)
print(arr2[0][2]) # truy cập phần tử trong mảng 2 chiều => Output: 3
print(arr2.ndim) # In ra số chiều của mảng => Output: 2

arr4 = np.array([1,2,3])
arr5 = np.array([4,5,6])
# Các thao tác cơ bản
print(arr5 + 10) # Cộng toàn bộ phần tử trong mảng với 10 => Output: [14 15 16]
print(arr4 * 2) # Nhân toàn bộ phần tử trong mảng lên 2 lần => Output: [2 4 6]
print(arr4 + arr5) # Cộng 2 mảng với nhau, tương tự phép - ,*, / => Output: [5 7 9]
# Các thao tác nâng cao
print(arr4 <= 2) # So sánh toàn mảng => Output: [ True True False]
print(np.sqrt(arr4)) # Lấy căn bậc 2 toàn mảng => Output: [1.   1.41421356 1.73205081]
print(np.sin(arr4)) # Lấy hàm lượng giác toàn mảng, tương tự với cos => Output: [0.84147098 0.90929743 0.14112001]
print(arr5[arr5 > 4]) # Lọc phần tử trong mảng theo điều kiện => Output: [5 6]
# Các hàm thống kê
print(arr5.mean()) # Trả ra giá trị TB các phần tử trong mảng => Output: 5.0
print(arr4.sum()) # Trả ra tổng các phần tử trong mảng => Output: 6
print(arr5.min()) # Tìm giá trị nhỏ nhất của mảng, tương tự là hàm arr.max() để tìm GTLN => Output: 4
print(arr4.std()) # Tính độ lệch chuẩn => Đo mức độ phân tán dữ liệu quanh giá trị TB (std nhỏ thì dữ liệu gần nhau, std lớn thì dữ liệu biến động lớn)
print(arr5.var()) # Tính phương sai (Phương sai là bình phương của độ lệch chuẩn)