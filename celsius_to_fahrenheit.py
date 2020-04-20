# 將攝氏轉換成華氏
temp_c = int(input('請輸入欲轉換的攝氏溫度： '))
temp_f = int((temp_c * (9 / 5)) + 32)
print("攝氏溫度 " + str(temp_c) + " 度，等於華氏溫度 " + str(temp_f) + " 度")