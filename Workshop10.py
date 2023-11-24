# จงเขียนโปรแกรม Python ของโปรแกรมแสดงข้อความต้อนรับนักศึกษา โดยรับชั้นปีทางแป้นพิมพ์แล้วแสดง
# ข้อความต้อนรับ ดังนี้
# กรณีป้อน 1 แสดงข้อความ "Welcome Freshman"
# กรณีป้อน 2 แสดงข้อความ "Welcome Sophomore"
# กรณีป้อน 3 แสดงข้อความ "Welcome Junior"
# กรณีป้อน 4 แสดงข้อความ "Welcome Senior                                  (อย่างน้อย 3 ฟังก์ชั่น)

def A(year):
    if year == 1:
        return "Welcome Freshman"
    elif year == 2:
        return "Welcome Sophomore"
    elif year == 3:
        return "Welcome Junior"
    elif year == 4:
        return "Welcome Senior"
    else:
        return "กรุณาใส่ชั้นปีที่กำหนดไว้"
print("=================================")
print("====== ข้อความต้อนรับนักศึกษา =======")
print("=================================")
year = input("ใส่ชั้นปีของคุณ 1-4 : ")

if year.isdigit():
    year = int(year)
    if 1 <= year <= 4:
        welcome_text = A(year)
        print(welcome_text)
    else:
        print("กรุณาใส่ชั้นปีที่กำหนดไว้.")
print("=================================")