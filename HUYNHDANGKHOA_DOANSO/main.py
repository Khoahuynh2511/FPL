import random

def guess_number_game():
    secret_number = random.randint(1, 100)
    print("Một số từ 1 đến 100 đã được tạo ra, hãy đoán xem đó là số nào.")
    
    for attempt in range(1, 4):
        guess = int(input("Hãy nhập số dự đoán của bạn: "))
        
        if guess == secret_number:
            if attempt == 1:
                print("Chúc mừng, bạn đã đoán đúng ngay lần đầu tiên! Bạn được 100 điểm.")
            elif attempt == 2:
                print("Chúc mừng, bạn đã đoán đúng ở lần thứ hai! Bạn được 50 điểm.")
            elif attempt == 3:
                print("Chúc mừng, bạn đã đoán đúng ở lần thứ ba! Bạn được 30 điểm.")
            break
        else:
            if attempt < 3:
                if guess < secret_number:
                    print("Số của bạn nhỏ quá.")
                else:
                    print("Số của bạn lớn quá.")
            else:
                print("Game over. Số bí mật là:", secret_number)

guess_number_game()
