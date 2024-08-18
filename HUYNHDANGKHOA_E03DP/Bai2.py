# Đếm tính từ
adjective_list = {
    "phẩm chất": [
        "tốt", "xấu", "thật thà", "giả dối", "tử tế", "độc ác", "hiền lành",
        "dễ chịu", "khó chịu", "nhẹ nhàng", "thô lỗ", "khiêm tốn", "kiêu căng",
        "cẩn thận", "ẩu", "lịch sự", "thô tục", "hào phóng", "keo kiệt", 
        "trung thực", "dối trá", "dũng cảm", "nhát gan", "quyết đoán", 
        "do dự", "nhân hậu", "ác nghiệt", "tận tâm", "vô tâm", "nhiệt tình", 
        "thờ ơ", "chu đáo", "lơ là", "tinh tế", "thô thiển", "tài năng", 
        "vụng về", "chăm chỉ", "lười biếng", "sáng tạo", "bảo thủ", "hoà đồng",
        "cô lập", "hướng ngoại", "hướng nội", "hoà nhã", "nóng nảy",
        "nhạy cảm", "khoan dung", "dè dặt", "quảng đại", "thận trọng",
        "bộc trực", "nghiêm túc", "hài hước"
    ],
    "cảm xúc": [
        "vui", "buồn", "giận", "bình tĩnh", "sợ hãi", "lo lắng", "hạnh phúc",
        "cô đơn", "phấn khích", "chán nản", "thất vọng", "hồi hộp", "tự tin",
        "rụt rè", "ngượng ngùng", "tức giận", "ngạc nhiên", "kích động", 
        "xúc động", "bối rối", "an tâm", "hoang mang", "hoảng sợ", "tức tối",
        "bình yên", "thanh thản", "ngây ngất", "phấn khởi", "mừng rỡ",
        "hài lòng", "bực tức", "cảm thông", "phẫn nộ", "hối hận", "nhẹ nhõm",
        "hoài nghi", "nghi ngờ", "tự hào","yêu"
    ],
    "trạng thái": [
        "mệt mỏi", "khoẻ mạnh", "ốm yếu", "đói", "no", "khát", "buồn ngủ",
        "tỉnh táo", "say", "lạnh", "nóng", "ấm", "mát", "đầy", "trống rỗng",
        "bẩn", "sạch", "sạch sẽ", "bẩn thỉu", "khô", "ướt", "mềm", "cứng",
        "trơn", "nhám", "mịn", "thô", "đau", "nhức", "ngứa", "tê", "hạnh phúc",
        "hân hoan", "bâng khuâng", "mơ màng", "sảng khoái", "lơ mơ", "bình phục",
        "mắc kẹt", "tự do", "bị trói buộc", "thăng hoa", "xuống tinh thần"
    ],
    "đặc điểm vật lý": [
        "cao", "thấp", "to", "nhỏ", "dài", "ngắn", "rộng", "hẹp", "nặng", 
        "nhẹ", "béo", "gầy", "tròn", "vuông", "bằng phẳng", "gồ ghề",
        "sáng", "tối", "mờ", "rõ ràng", "đục", "trong suốt", "mảnh mai",
        "vạm vỡ", "gọn gàng", "xuề xoà", "bảnh bao", "điển trai", "xấu xí",
        "mịn màng", "sần sùi", "dẻo dai"
    ],
    "màu sắc": [
        "đỏ", "xanh", "vàng", "trắng", "đen", "nâu", "hồng", "cam", "tím", 
        "xám", "xanh dương", "xanh lá", "kem", "bạc", "vàng chanh", "xanh lá mạ",
        "xanh ngọc", "đỏ rực", "tím than", "vàng nghệ", "xanh đậm", "trắng sứ",
        "đỏ đô", "cam cháy", "hồng phấn"
    ],
    "cảm giác": [
        "ngọt", "chua", "đắng", "mặn", "nhạt", "thơm", "hôi", "nồng", 
        "nhẹ", "nặng", "nhức", "ngứa", "mềm mại", "xù xì", "mượt mà", 
        "sần sùi", "lạnh lẽo", "ấm áp", "mát mẻ", "nhẹ nhàng", "nóng bỏng",
        "nghẹt thở"
    ],
    "thời gian": [
        "nhanh", "chậm", "sớm", "muộn", "thoáng qua", "kéo dài", "chớp nhoáng",
        "bất tận", "ngắn hạn", "dài hạn", "liên tục", "tạm thời", "đột ngột",
        "từ từ"
    ],
    "khác": [
        "dễ", "khó", "bền", "dễ vỡ", "giàu", "nghèo", "trẻ", "già", "mới", 
        "cũ", "tươi", "héo", "tuyệt vời", "tồi tệ", "xinh đẹp", "xấu xí", 
        "dễ thương", "đáng yêu", "khó ưa", "sành điệu", "lỗi thời", "phổ biến", 
        "hiếm", "đặc biệt", "bình thường", "quan trọng", "không quan trọng", 
        "chính xác", "sai", "đúng", "sai lệch", "thật", "giả", "rõ ràng", 
        "mơ hồ", "chắc chắn", "không chắc chắn", "dễ hiểu", "khó hiểu", 
        "dễ dàng", "phức tạp", "độc đáo", "khác thường", "hiếm có", 
        "lôi cuốn", "nhạt nhẽo", "thú vị", "trực quan"
    ]
}

# Hàm kiểm tra và đếm tính từ trong văn bản
def find_adjectives(text):
    words = text.lower().split()
    found_adjectives = []
    
    # Kiểm tra từng từ và cặp từ liên tiếp để nhận diện tính từ
    for i in range(len(words)):
        # Kiểm tra từ đơn
        if words[i] in [adj for sublist in adjective_list.values() for adj in sublist]:
            found_adjectives.append(words[i])
        
        # Kiểm tra từ ghép (cặp từ liên tiếp)
        if i < len(words) - 1:
            word_pair = words[i] + " " + words[i + 1]
            if word_pair in [adj for sublist in adjective_list.values() for adj in sublist]:
                found_adjectives.append(word_pair)
    
    return len(found_adjectives), found_adjectives

def main():
    print("Nhập hoặc dán văn bản của bạn (ấn Enter khi hoàn tất):")
    text = input().strip()
    
    count, adjectives = find_adjectives(text)
    print(f"Số lượng tính từ: {count}")
    print(f"Tính từ: {adjectives}")

if __name__ == "__main__":
    main()
