#Bài 5 - Xử lý tuple
# 1. Tạo một tuple chứa các số từ 1 đến 5.
numbers_tuple = (1, 2, 3, 4, 5)
print("Tuple ban đầu:", numbers_tuple)
print(type(numbers_tuple))
# 2. Truy cập và in ra phần tử thứ ba trong tuple.
third_element = numbers_tuple[2]
print("Phần tử thứ ba trong tuple:", third_element)

# 3. Cắt tuple để lấy các phần tử từ phần tử thứ hai đến phần tử thứ tư.
sliced_tuple = numbers_tuple[1:4]
print("Tuple sau khi cắt (từ phần tử thứ hai đến thứ tư):", sliced_tuple)

# 4. Unpack tuple để lấy các giá trị riêng biệt.
a, b, c, d, e = numbers_tuple
print("Giá trị được unpack:", a, b, c, d, e)

# 5. Sử dụng vòng lặp để kiểm tra xem số 7 có tồn tại trong tuple không.
exists = 7 in numbers_tuple
print("Số 7 có tồn tại trong tuple không?", exists)

# 6. Tạo một tuple khác và nối với tuple ban đầu.
another_tuple = (6, 7, 8)
combined_tuple = numbers_tuple + another_tuple
print("Tuple sau khi nối:", combined_tuple)
exists = 7 in combined_tuple
print("Số 7 có tồn tại trong tuple không?", exists)

# 7. Sử dụng phương thức để đếm số lần xuất hiện của một phần tử trong tuple.
count_of_4 = numbers_tuple.count(4)
print("Số lần xuất hiện của số 4 trong tuple:", count_of_4)

# 8. Hãy tạo một tuple mới chỉ chứa các số chẵn từ tuple ban đầu.
even_numbers_tuple = tuple(x for x in combined_tuple if x % 2 == 0)
print("Tuple mới chỉ chứa các số chẵn:", even_numbers_tuple)