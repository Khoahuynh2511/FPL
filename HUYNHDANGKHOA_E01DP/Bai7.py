# 1. Tạo một dictionary đơn giản chứa thông tin về tên và tuổi của bạn.
person_info = {
    "tên": "Huỳnh Đăng Khoa",
    "tuổi": 20
}
print("Dictionary ban đầu:", person_info)

# 2. Truy xuất và in ra giá trị tuổi từ dictionary đã tạo.
print("Tuổi của bạn là:", person_info["tuổi"])

# 3. Thêm một thông tin về trường học.
person_info["trường học"] = "Đại học Công nghệ thông tin - ĐHQG"
print("Dictionary sau khi thêm trường học:", person_info)

# 4. Hãy cộng thêm một tuổi.
person_info["tuổi"] += 1
print("Dictionary sau khi cộng thêm một tuổi:", person_info)

# 5. Xóa tuổi.
del person_info["tuổi"]
print("Dictionary sau khi xóa tuổi:", person_info)

# 6. Sử dụng vòng lặp để in ra tất cả các key và value trong dictionary.
print("Các key và value trong dictionary:")
for key, value in person_info.items():
    print(f"{key}: {value}")

# 7. Sao chép nội dung của một dictionary sang một dictionary khác.
person_info_copy = person_info.copy()
print("Bản sao của dictionary:", person_info_copy)

# 8. Thêm thông tin về địa chỉ là một dictionary gồm tỉnh, huyện, xã.
person_info["địa chỉ"] = {
    "thành phố": "Thành phố Hồ Chí Minh",
    "quận": "Quận 6",
    "phường": "Phường 6"
}
print("Dictionary sau khi thêm địa chỉ:", person_info)

# 9. Hãy in ra thông tin về tỉnh.
print("Thông tin về tỉnh là:", person_info["địa chỉ"]["thành phố"])

# 10. Tạo một dictionary chứa bình phương của các số từ 1 đến 5.
squares = {x: x*x for x in range(1, 6)}
print("Dictionary chứa bình phương của các số từ 1 đến 5:", squares)
