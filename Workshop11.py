# จงเขียนโปรแกรม Python คำนวณค่าโทรศัพท์ โดยรับชื่อผู้ใช้โทรศัพท์ เบอร์โทรศัพท์ และจำนวนนาทีที่ใช้
# โทรศัพท์ทางแป้นพิมพ์ 
# ทั้งนี้ ในการคิดค่าโทรศัพท์ มีหลักเกณฑ์ในการคิดคำนวณ ดังนี้ 
# นาทีที่ 1 - 15 คิดที นาทีละ 5 บาท 
# นาทีที่ 16 – 30 คิดที นาทีละ 3 บาท 
# นาทีที่ 31 เป็นต้นไปคิดที่นาทีละ 1.50 บาท                                       (อย่างน้อย 3 ฟังก์ชั่น)


def A(minutes):
    if minutes >= 1 and minutes <= 15:
        chargeminute = 5.0
    elif minutes <= 30:
        chargeminute = 3.0
    else:
        chargeminute = 1.5

    total = minutes * chargeminute
    return total

def B(name, phone_number, minutes, total):
    print("ชื่อ :", name)
    print("เบอร์ :", phone_number)
    print("เวลาโทร :", minutes)
    print("ค่าโทร :", total)
print("=================================")
print("======== คำนวณค่าโทรศัพท์ =========")
print("=================================")
name = input("ชื่อผู้ใช้โทรศัพท์ : ")
phone_number = input("เบอร์โทรศัพท์ : ")
minutes = int(input("นาทีที่โทรออก : "))

total = A(minutes)

B(name, phone_number, minutes, total)
print("=================================")