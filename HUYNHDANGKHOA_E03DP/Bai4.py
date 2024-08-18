#Code mã đảo
def reverse_message(message):
    return message[::-1]

# Hiển thị bảng lựa chọn
print("Lựa chọn:")
print("1. Giải mã lời nhắn ngược")
print("2. Mã hóa lời nhắn thành ngược")

# Nhập lựa chọn của người dùng
choice = input("Vui lòng nhập lựa chọn (1/2): ").strip()

if choice == '1':
    # Nhập lời nhắn ngược từ người dùng
    encoded_message = input("Nhập lời nhắn ngược: ")
    decoded_message = reverse_message(encoded_message)
    print("Lời nhắn đã giải mã:", decoded_message)
elif choice == '2':
    # Nhập lời nhắn từ người dùng
    message = input("Nhập lời nhắn để mã hóa: ")
    encoded_message = reverse_message(message)
    print("Lời nhắn đã mã hóa:", encoded_message)
else:
    print("Lựa chọn không hợp lệ. Vui lòng chọn '1' hoặc '2'.")
