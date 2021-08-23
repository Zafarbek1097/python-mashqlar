# -*- coding: utf-8 -*-
"""
Created on Sat May 29 20:07:25 2021

@author: Пользователь
"""

#yosh = int(input(" Yoshingiz nechida? "))
#if yosh<=6:
 #   print("Sizga 1000 so'm ")
#elif yosh<=10:
 #   print(" Sizga 2000 so'm ")
#elif yosh<=16:
 #   print("Sizga 5000 so'm ")
#else:
 #   print("Kattalarga 10000 so'm ")    
 
 #________________________________________________________________________
    
#yosh = int(input(" Yoshingiz nechida? "))
#if yosh<=6:
 #  a=1000
#elif yosh<=10:
 #  a=2000
#elif yosh<=16:
 #   a=5000
#else:
 #  a=10000 
#print(f"Sizga kirish {a}  so'm")   

#______________________________________________________________________

#kun = input(" Bugun kun nima? ")
#if kun.lower() == "shanba"  or  kun.lower() == "yakshanba":
 #   print(" Bugun dam olish kuni  toqqa boramiz ")
#else:
 #   print("bugun ish kuni ")  
#______________________________________________________________________________

#kun = input('Bugun qaysi kun? >>>')
#harorat = int(input(' Havo harorti  qanday?>>> ')) 
#if (kun.lower()=="yakshanba"   or  kun.lower()=="shanba")  and  harorat>=30:
#    print(" Bugun dam olish kuni cho'milishga boramiz ")
#elif    (kun.lower()=='yakshanba'   or  kun.lower()=="shanba")  and  harorat<30:
#    print(" Uyda dam olamiz ")
#else:
 #   print("Bugun dam olish kuni emas")
 
 #______________________________________________________________________________________
 
#narh = 15000
#choy = True
#salat = True
#salat=False 


#if  choy  and salat:
 #   narh = narh+10000
#elif    choy or salat:
 #   narh = narh+5000
#print(f" Jami narx = {narh}")    

#____________________________________________________________________________
#ovqat = 15000
#choy = True
#non = False
#salat = True
#cola = True
#fanta = False
#qatiq = True
#assorti = True


#if choy:
 #   print("Choy oldi")
  #  ovqat=ovqat+2000
#if non:
 #   print("Non oldi")
  #  ovqat = ovqat+3000
#if salat:
 #   print("Salat oldi")
  #  ovqat = ovqat+5000
#if cola:
 #   print("Cola oldi")
  #  ovqat = ovqat+9000
#if fanta:
 #   print("fanta oldi")
  #  ovqat = ovqat +7500
#if qatiq:
 #   print("Qatiq oldi")
  #  ovqat= ovqat+6000
#if assorti:
 #   print('assorti oldi')
  #  ovqat = ovqat+7000
#print(f"Jami xisob {ovqat} ming so'm  ")    
    
    
 # ro'yxat ichini tekshirish bunda in operatoridan foydalanamiz____________________

#menu = ['manti','osh',' shorva','shashlik','kabob']
#ovqat = input("Ovqat nomini kiriting  >>")

#if ovqat.lower() in menu:
   # print(" Buyurtmangiz qabul qilindi")
#else:
 #   print("Bunday ovqat yo'q")
#print(menu)    
   
#__________+______________________________________________________________________

#menu = ['osh','somsa','manti','chuchvara', 'xalim','shashlik']
#buyurtmalar = ['osh', 'shorva','kabob','manti','shashlik','jiz']

#for taom in buyurtmalar:
 #   if taom in menu:
  #      print(f"Menuda {taom} bor ")
   # else:
    #    print(f"Menuda  {taom} yoq ")




#________________________________________________________________________________

# MASALALAR ISHLASH

#son = int(input("Juft son kiriting>> "))

#if  son%2==0:
 #   print(" Rahmat! ")
#else:
 #   print(" Bu son jift emas! ")
 # __________________________________________________________  
  

#yosh = int(input(" Yoshingiz nechida?  >>"))

#if yosh<4 or yosh>60:
 #   narx="tekin"
#elif yosh<=18:
 #   narx = 10000
#elif yosh>18:
 #   narx=20000
#print(f"Sizga  kirish  {narx}  ")    
    
     
#__________________________________________________________________________

#x=float(input("Birinchi sonni kiriting? >>"))
#y= float(input("Ikkinchi conni kiriting? >>"))

#if x>y:
 #   print(f"{x}>{y}")
#elif y>x:
 #   print(f" {y}>{x}") 
#else:
 #   print(f"{x}={y}")    

#_________________________________________________________________________________

#mahsulotlar = ['olma','anor','uzum','shaftoli','qovun','tarvuz','orik','gilos','anjir','olcha']
#savat = []

#for meva in range(5):
 #   savat.append(input(f"Savatga {meva+1}- mahsulotni qo'shing? >> "))
#print("Savatchadagi mahsulotlar ro'yxati \n")

#for tavar  in savat:
 #    if tavar in mahsulotlar:
  #      print(f" Do'konimizda {tavar} bor")
   #  else:
    #    print(f" Do'konimizda {tavar} yo'q") 
    
    
 #   __________________________________________________________
#mahsulotlar =  ['olma','anor','uzum','shaftoli','qovun','tarvuz','orik','gilos','anjir','olcha'] 
    
#savat = []
#for n  in range(5):
 #   savat.append(input(f" Savatga {n+1}-mahsulotni kiriting?>>"))


#bor_mahsulot = []
#mavjud_emas = []

#for mahsulot in savat:
 #   if mahsulot in mahsulotlar:
  #      bor_mahsulot.append(mahsulot)
   # else:
    #    mavjud_emas.append(mahsulot)
#________________________________________________________________________ 


#mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']

#savat=[]
#for n in range(5):
#    savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#if savat:
 #   for mahsulot in savat:
  #      if mahsulot in mahsulotlar:
   #         print(f"Do'konimizda {mahsulot} bor")
    #    else:
     #       print(f"Do'konimizda {mahsulot} yo'q")
#else: 
 #   print("Savatingiz bo'sh")            
#____________________________________________________________________________    

##mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz',
#               'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
#savat = []
#for n in range(5):
 #   savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

#bor_mahsulotlar = []
#mavjud_emas = []
#for mahsulot in savat:
 #   if mahsulot in mahsulotlar:
  #      bor_mahsulotlar.append(mahsulot)
   # else:
    #    mavjud_emas.append(mahsulot)

#if mavjud_emas:
 # print("Do'konimizda quyidagi mahsulotlar yo'q:")
#for mahsulot in mavjud_emas:
 # print(mahsulot)
#else:
 # print("Siz so'ragan barcha mahsulotlar do'konimizda bor")
  
#________________MASALA_________________________________________________________

#foydalanuvchilar = []
#for  n in  range(5):
 #   foydalanuvchilar.append(input(f"{n+1}- loginni kiriting? >> "))
#print(foydalanuvchilar)  
  
#login = input("Yangi login kiriting? >> ")    

#if  login in foydalanuvchilar:
 #   print("Login band yangi login tanlang! >>")
#else:
 #   print(f"Xush kelibsiz {login.title()}")    


#_______________________________________________________________________________

son = int(input("Istalgan butun son kiriting?>>"))

sonlar = list(range(1,11))
print(sonlar)
for butun in sonlar:
    if son%butun == 0:
        print(f"{son} soni {butun} ga qoldiqsiz bo'linadi ")

  
    












    