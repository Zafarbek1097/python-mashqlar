# -*- coding: utf-8 -*-
"""
Created on Thu Jul 15 14:31:13 2021

@author: Пользователь
"""

#print("Yaqin do'stlaringiz ro'yxatini tuzamiz")
#n=1
#while n<4:
 #   kirit=f" {n} - do'stingiz ismini kiriting->> "
  #  ism = input(kirit)
   # ismlar.append(ism)
   # chiqar = input("Yana ism qo'shasizmi? Ha/Yo'q->>")
   #if chiqar=="ha":
    #    n+=1
     #   continue
    #else:
     #   break


#print("Do'stlarim ro'yxati:")
#for dostlarim in ismlar:
 #   print(dostlarim.title())
#_______________________________________________________________________________

#print("Do'stlarimniing yoshini saqlayman:")

#dostlar = {}
#ishora = True

#while ishora:
 #   ism = input("Do'stingizni ismini kiriting->> ")
  #  yosh= input(f"{ism.title()}ning yoshini kiriting: ->>")
   # dostlar[ism]=int(yosh)
    
   # javob = input("Yana ma'lumot qo'shasizmi?  Ha/Yo'q? ->>")
    
   # if javob=="yo'q":
    #    ishora = False

        
#for ism, yosh in dostlar.items():
 #   print(f" Do'stingiz {ism.title()}  {yosh} yoshda ")
    
  #_________________ro'yxat elementlarini o'chirish________________________________________________________________


#cars = ['cobalt','matiz','tiko','nexia','ravon','gentra','malibu','cobalt','spark','cobalt']

#while 'cobalt'  in cars:
 #   cars.remove('cobalt')
    
    
  #____________________________o'quvchilarni baxolash _______________________________________

#oquvchilar = ['asin','turgun','muxi','yo\'ldosh','ro\'zi','sodiq']

#baholangan_oquvchilar = {}

#while oquvchilar:
 #   oquvchi = oquvchilar.pop()
  #  baho = int(input(f"{oquvchi.title()}ning bahosini kiriting?->> "))
  #  if baho<6:
  #      print(f"{oquvchi.title()} baholandi")
  #  else:
  #      print("Maximal 5 baxogacha qo'yish mumkin! ")
        
  #      break

    
#_____________________amaliy mashg'ulot______________________________________________________________________


#royxat = []

#qabul = True

#while qabul:
#    buyurtma = input("Buyurtmangizni kiriting:->> ")
 #   royxat.append(buyurtma)
  #  kirit = input("Yana biror mahsulat buyurtma qilasizmi?  Ha/Yo'q: ")
   # if kirit=="yo'q":
        
    #    break
    
#print("Siz buyurtma qilgan mahsulotlar ")

#for mahsulot in royxat:
 #   print(mahsulot)    
    
  #____________________________amaliy____________________________________________

#bozor = {}
#n=1
#while True:
 #   mahsulot = input(f"{n}- Mahsulot nomini kiriting?->> ")
  #  narh = input(f"{mahsulot.title()} narhini kiriting?->> ")
   # bozor[mahsulot] = int(narh)
    
   # yana = input("Yana mahsulot qo'shasizmi? Ha/Yo'q ->> ")
   # if yana=='ha':
    #   n+=1
     #  continue
    #else:
     #  break
   
#print("Siz buyurtma qilgan mahsulotlar") 

#for mahsulot, narh in bozor.items():
 #   print(f"{mahsulot.title()} narhi {narh} ming so'm")

  #________________________________solishtirish________________
  

#buyurtmalar = ['non','makaron','go\'sht','saryog\'']
#bozor = {'non':1600,
 #        'kartoshka':3000,
  #       'saryog\'':4000,
   #      'piyoz':2000,
    #     'mosh':10000}
    

#while buyurtmalar:
 #   buyurtma = buyurtmalar.pop()
  #  if buyurtma in bozor.keys():
   #     narh = bozor[buyurtma]
    #    print(f"{buyurtma.title()}ning narxi {narh} ming so'm ")
    #else:
     #   print(f"Bizda {buyurtma} yo'q ")    
            
     
        
import   random  
        
a=random.randrange(1,10)



print(a)
        
    
    
    
    
    
    
    
    
    
    
    
    