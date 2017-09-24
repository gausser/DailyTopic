# -*- coding utf-8 -*-

import time
tiangan = ['甲', '乙', '丙', '丁', '戊', '己', '庚', '辛', '壬', '癸']
dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
now = int(time.strftime("%Y"))

def Get_Tian_Zhi(year):
    s = tiangan[year % 10 - 3] + dizhi[year % 12 - 3]
    print s.decode('utf-8')

def Get_Year_By_TianZhi(tianzhi):
    tmp1 = tianzhi[0] + 3
    tmp2 = tianzhi[1] + 3
    list_year = []

    for i in range(100, 300):
        for j in range(100, 300):
            if (i * 10 + tmp1 == j * 12 + tmp2) and abs(j * 12 + tmp2 - now) <= 60:
                list_year.append(j * 12 + tmp2)

    return list_year
        
year = int(raw_input("Enter the year: "))    
Get_Tian_Zhi(year)

tiangan = int(raw_input("Enter the tiangan: "))
dizhi = int(raw_input("Enter the dizhi: "))
tianzhi = [tiangan, dizhi]
print Get_Year_By_TianZhi(tianzhi)