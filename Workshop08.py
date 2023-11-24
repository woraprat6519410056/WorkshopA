# จงเขียนโปรแกรม Python ของโปรแกรมตรวจสอบค่า PH ของน้ำปะปาจากจังหวัดต่างๆ โดยรับชื่อจังหวัด 
# และค่า PH ทางแป้นพิมพ์ และแสดงผลทางหน้าจอ โดยหากค่า PH เป็น 7-8 แสดงข้อความ "Result is Normal" 
#หากค่า PH มากกว่า 8 ให้แสดงข้อความ "Result is Acid" หากค่า PH น้อยกว่า 7 ให้แสดงข้อความ "Result is Alkali" (อย่างน้อย 3 ฟังก์ชั่น)

def F(P, Hp):
    if Hp >= 7 and Hp <= 8:
        R = "Result is Normal"
    elif Hp > 8:
        R = "Result is Acid"
    else:
        R = "Result is Alkali"

    print(f"Province: {P}")
    print(f"pH Value: {Hp}")
    print(f"Result: {R}")

print("=================================")
print("========= ตรวจสอบค่า PH ==========")
print("=================================")
name = input("ใส่ชื่อจังหวัด : ")
Hp = float(input("ค่า pH : "))

F(name, Hp)
print("=================================")
