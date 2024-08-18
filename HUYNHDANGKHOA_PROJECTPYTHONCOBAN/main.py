import pandas as pd

def read_scores_from_csv(file_path):
    
    df = pd.read_csv(file_path)
    
    toan_scores = df['Toán'].tolist() if 'Toán' in df.columns else []
    van_scores = df['Văn'].tolist() if 'Văn' in df.columns else []
    anh_scores = df['Anh'].tolist() if 'Anh' in df.columns else []
    
    return toan_scores, van_scores, anh_scores

def calculate_max(data):
    max_score = data[0]
    for score in data[1:]:
        if score > max_score:
            max_score = score
    return max_score

def calculate_min(data):
    min_score = data[0]
    for score in data[1:]:
        if score < min_score:
            min_score = score
    return min_score

def calculate_average(data):
    total = sum(data)
    return total / len(data)

def min_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

def calculate_median(data):
    min_sort(data)
    n = len(data)
    mid = n // 2
    if n % 2 == 0:
        return (data[mid - 1] + data[mid]) / 2.0
    else:
        return data[mid]

def main():
    filename = "test_05.csv"
    toan_scores, van_scores, anh_scores = read_scores_from_csv(filename)
    
    print("Toán:")
    print("Điểm cao nhất:", calculate_max(toan_scores))
    print("Điểm thấp nhất:", calculate_min(toan_scores))
    print("Điểm trung bình:", calculate_average(toan_scores))
    print("Điểm trung vị:", calculate_median(toan_scores))
    
    print("\nVăn:")
    print("Điểm cao nhất:", calculate_max(van_scores))
    print("Điểm thấp nhất:", calculate_min(van_scores))
    print("Điểm trung bình:", calculate_average(van_scores))
    print("Điểm trung vị:", calculate_median(van_scores))
    
    print("\nAnh:")
    print("Điểm cao nhất:", calculate_max(anh_scores))
    print("Điểm thấp nhất:", calculate_min(anh_scores))
    print("Điểm trung bình:", calculate_average(anh_scores))
    print("Điểm trung vị:", calculate_median(anh_scores))

if __name__ == "__main__":
    main()
