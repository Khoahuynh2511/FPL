#Rùa và Thỏ***
# Chuỗi chứa thông tin về các chi phí
chuoi_thong_tin = '''
    Thỏ đưa Rùa 1 ly trà sữa vừa mới order có giá một ly là: 45.000 vnd.
    Sau đó vì Rùa đói nên Thỏ tiếp tục order bịch bánh tráng trộn có giá là: 20.000 vnd cho Rùa.
    Và tiền ship: 15.000 vnd.
'''

# Tách các số tiền từ chuỗi
gia_cac_mon = []
for phan in chuoi_thong_tin.split('vnd'):
    # Tìm vị trí của số tiền (số có dấu chấm)
    phan = phan.strip()  # Loại bỏ khoảng trắng thừa
    if ':' in phan:
        phan = phan.split(':')[-1].strip()
    if '.' in phan:
        try:
            gia = int(phan.replace('.', ''))
            gia_cac_mon.append(gia)
        except ValueError:
            continue

# Tính tổng tiền cần trả
tong_tien = sum(gia_cac_mon)

# In kết quả
print(f"Tổng số tiền bạn Rùa cần trả cho bạn Thỏ là: {tong_tien} VND")
