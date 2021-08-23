# -*- coding: utf-8 -*-
"""
Created on Tue Jun 29 14:41:48 2021

@author: Пользователь
"""

#ism = input("Ismingiz nima? ")
#savol = (f"Salom, {ism.title()}, Yoshingiz nechida? ")

#yosh = int(input(savol))

#balandlik = float(input("Bo'yingiz nechi?> "))

#tyil = int(input("Tug'ilgan  yilingiznin kiriting?> "))

#n  =  input("O'zingiz haqingizda bilishni istaysizmi ? ")

#if n=='xa':
 #   print(f" Sizning ismingiz {ism.title()},\n Yoshingiz {yosh} da \n Bo'yingiz {balandlik} m\n Tug'ilgan yilingiz {tyil}")
#else:
 #   print("Malumot uchun rahmat! ")
  
#_____________while sikli bilan tanishamiz_______=++++++++++++++++++++++

#son= 1
#while son<=20:
 #   print(son, end=' ')
  #  son+=1

#_____________________________________________________________________________

#print("\nKiritgan soningizni kvadratini hisoblovchi dastur:")

#son = ("Istalgan sonni kiriting ")
#son += "\ndasturni to'xtatish uchun 'exit' deb yozing:  "

#qiymat = ' '
#while qiymat !='exit':
 #   qiymat = int(input(son))
  #  if qiymat != 'exit':
   #     print(float(qiymat**2))


#_____====++____________________+++++++++++++_______________________________




#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
#ishora = True
#while ishora:
 #   qiymat = float(input(savol))
  #  if qiymat=='exit':
   #     ishora=False
   # elif qiymat =='stop':
    #    ishora=False
    #else:    
     #   print(qiymat**2)
    
        
    

#+++++++++++++++++________BREAK OPERATORI ___________________________++++++++++++++++++++++++++++++++++=====


#print(" Kiritilgan sonning kvadratini hisoblovchi dastur ")
#kirit = "Istalgan son kiriting!"
#kirit +=" \n(daturdan chiqish uchun 'exit' deb yozing: ) ->> "

#while True:
 #   qiymat = int(input(kirit))
  #  if qiymat == 'exit':
   #     break
   # else:
    #    print(f"Siz kiritgan sonning kvadrati {qiymat**2} ga teng ")


#________________for funksiyasida  breakni qo'llaymiz_________________

#sonlar = list(range(1,20))

#for  son in sonlar:
 #   if son==10:
  #      break
   # print(f"\n{son}  ning kvadrati {son**2}  ga  teng, ")
    
    
 #_______________continue___bitta tashlab o'tib ketadi ____________________   
    
#print(" \n\nToq sonlar kvadratini hisoblaymiz:")    
#sonlar = list(range(1,30))

#for  son in sonlar:
 #   if son%2==0:
  #      continue
   # print(f"\n{son}  ning kvadrati {son**2}  ga  teng, ")


#_____________++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


#son = 0
#while son<10:
 #   son += 1
  #  if son%2!=0 or son%3==0:
   #     continue
   # else:
    #    print(son)

#_____________________++++++++++++++++++++++++++++_________________________________


#      xatoliklar bilan ishlash
#son = 0
#while son<10:
 #   son+=1
  #  if son%2!=0:
   #     continue
   # else:
    #    print(son)

#______________=======++++++++++++++++++++++++++++++++++++++++++++


#_________________________________amaliyot _____________==+++++++++++++++++++++

#print("\n\n Yoqtirgan kitoblaringizni saqlaydigan  dastur ")

#kitob = "Yoqtirgan kitobingizni kiriting:-> "
#kitob +=" \ndasturdan chiqish uchun 'stop' deb yozing " 
#saqla=''
#royxat=[] 
#while saqla!='stop':
#    saqla = input(kitob)
#    if saqla!='stop':
 #       False        
  #      royxat.append(saqla)
  #      print(royxat)

#______________amaliyot_______________________+++++++++++++++++++++++===============_________


#print("Muzeyga kirish chipta narxini aniqlaydigan dastur ")

#chipta = "Yoshingizni kiriting: "
#chipta += "  (dasturdan chiqish uchun 'exit' so'zini kiriting -> "
#narx=''
#while  narx!='exit':
 #   qiymat =int(input(chipta))
  #  if qiymat<7:
   #     pul=2000
   # elif   qiymat<18:
   #     pul=3000
   # elif  qiymat<65:
   #     pul=10000
   # elif narx=='quit':
   #     break
   # else:
   #     pul=15000
        
   # print(f"Sizga chipta narxi {pul} so'm ")   


#______________xatolikni tekshirish  _________________________________

savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat = int(input(savol))
    if qiymat<0:
        
        print("Siz manfiy son kiritdingiz ")
        continue
    elif qiymat=='Exit':
        break
    else:
        ildiz = float(qiymat**0.5)
        print(f"{qiymat} ning ildizi {ildiz} ga teng")







  
 