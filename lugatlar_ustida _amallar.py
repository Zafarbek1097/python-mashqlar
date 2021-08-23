# -*- coding: utf-8 -*-
"""
Created on Sun Jun  6 20:57:05 2021

@author: Пользователь
"""
#talaba = {
 #   'ism':'botir',
  #  'familiya':'olimov',
   # 't_yil':'1999',
    #'t_joyi':'surxondaryo',
    #'kurs':4,
    #'yosh':24,
    #'yonalishi':'telecom'
    #}

#print(talaba.items())

#for k, q in talaba.items():
 #   print(f"Kalit: {k} ")
  #  print(f"Qiymat: {q} \n")
  
 #___________________________________________________________________

#telefonlar = {
 #   'ali':'redmi',
  #  'vali':'samsung',
   # 'alisher':'x4',
    #'zafar':'A10',
    #'sardor':'S9',
    #'mahmud':'galaxy'
     #   } 
  
#for k,q in telefonlar.items():
 #   print(f"{k.title()}ning  telefoni  {q} ")
  
 #__________________________________________________________________________________
 
#mahsulotlar = {
    
     #'olma':20000,
     #'uzum':30000,
     #'zanjabil':1200,
     #'anor':23000,
     #'gilos':5000,
     #'anjir':7000,
    # 'malina':9000,
   #  'shaftoli':5400
     
  #   } 

#print(mahsulotlar.keys())

#for mahsulot  in  mahsulotlar.values():
 #   print(sorted(mahsulot))   
#________________________________________________________________________________    


#mahsulotlar = {
    
     #'olma':20000,
     #'uzum':30000,
     #'zanjabil':1200,
     #'anor':23000,
     #'gilos':5000,
    # 'anjir':7000,
   # 'malina':9000,
  # 'shaftoli':5400
     
 # } 

#bozorlik = []
#for n  in range(4):
 #   bozorlik.append(input(f"{n+1}-mahsulot nomini kiriting >> "))
#print(bozorlik)
    
#for mahsulot  in bozorlik:
#    if mahsulot in mahsulotlar:
 #       print(f"{mahsulot.title()}  {mahsulotlar[mahsulot]}  so'm ")
 
#+____________________________________+++________________+++____________________   
    
#mahsulotlar = {
    
  #   'olma':20000,
  #   'uzum':30000,
   #  'zanjabil':1200,
   #  'anor':23000,
   #  'gilos':5000,
  #   'anjir':7000,
  #  'malina':9000,
  # 'shaftoli':5400
     
 # }

#bozorlik = ['olma', 'uzum', 'salat', 'non', 'kampot']

#for buyum  in bozorlik:
#    if buyum not in mahsulotlar:
 #       print(f" Iltimos do'koningizga {buyum}  ham olib keling")

 
#___________________________________________________________________________________


#mahsulotlar = {
    
#     'olma':20000,
  #   'uzum':30000,
  #   'zanjabil':1200,
   #  'anor':23000,
  #   'gilos':5000,
  #   'anjir':7000,
   # 'malina':9000,
  # 'shaftoli':5400
     
#  }

#print('Do\'kondagi mahsulotlar')

#for m  in sorted(mahsulotlar):
#    print(m.title())

 #_____________________________________________________________________________________
    
#telefonlar = {
 #   'ali':'bredmi',
  #  'vali':'samsung',
   # 'alisher':'x4',
    #'zafar':'A10',
    #'sardor':'S9',
    #'mahmud':'galaxy'
     #   } 
  
#print('Foydalannuvchi quyidagi telefonlarni ishlatadi')

#for tel in set(telefonlar.values()):
 #   print(tel)
 
 
 #___AMALIYOT  MASHQLARI_______________________________________________________________________________

#izohli_lugat = {
    
#    'float':"haqiqiy sonlarni chiqarish",
 #   'integer':'butun son',
  #  'for': 'takrorlash operatiri',
   # 'if':' agar shartli aperatori',
    #'else':'aks holda shart operatori',
    #'input':'kiritish oqimi',
    #'print':'chop etish',
    #'boolen':'mantiqiy qiymat'
       
    #}

#for lugat in sorted(izohli_lugat):
 #   print(f" {lugat.title()}-{izohli_lugat[lugat]} \n")
  #



#______________--------davlatlar  poytaxti  lugati______________________________________


#davlatlar = {
 #   
  #  'uzbekistan': 'toshkent',
   # 'qozogiston': 'beshkek',
    #'rossiya': 'maskva',
    #'tojikiston':'dushanbe',
    #'AQSH': 'vashingto',
    #'kanada':'attava',
    #'italiya':'rim',
    #'germaniya':'berlin',
    #'xitoy':'pekin',
    #'fransiya': 'parij'
    #}
 
#print(davlatlar) 



#for davlat in sorted(davlatlar):
 #   print(davlat.upper())
    
#for davlat in davlatlar:
 #   print(davlatlar[davlat])
    
#______________________________________________________________________________________
    

davlatlar = {

  'uzbekistan': 'toshkent',
    'AQSH': 'vashingto',
   'qozogiston': 'beshkek',
    'rossiya': 'maskva',
    'tojikiston':'dushanbe',
    'kanada':'attava',
    'italiya':'rim',
    'germaniya':'berlin',
    'xitoy':'pekin',   
    'fransiya': 'parij'
    }
   
    

davlat = input(' Biror davlat nomini kiriting? >> ')
potaxt = davlatlar.get(davlat)
if poytaxt==None:
    print(" Bizda bu haqda ma'lumot yo'q ")  
else:        
    print(f" {davlat}ning  poytaxti {poytaxt[davlat]}")
       
country = input('Qaysi davlatning poytaxtini bilishni istaysiz?:').lower()
capital = davlatlar.get(country)
if capital==None:
    print('Kechirasiz, bizda bu haqida ma\'lumot yo\'q')    
else:
    print(f"{country.upper()}ning poytaxti {capital.title()} shahri")     
     
     #_________________________________________________________________________
  
#menyu = {
    
 #  'non': 3000,
  # 'osh':20000,
   # 'shorva':18000,
   # 'mastava':15000,
   # 'qatiq':5000,
   # 'somsa':6000,
   # 'manti':4000,
   # 'shashlik':35000,
   # "go'sht":80000,
   # 'xonim':25000,
    
    
   # }




#taom = []
#print("Uchta taom buyurtma bering? ")

#for n in range(3):
 #   taom.append(input(f"{n+1}-taom:-> "))
     
   
#print(taom) 

#for k in taom:
 #   if k in menyu:
  #      print(f"{k.title()} {menyu[k]} ming so'm ")
   # else:
   #     print(f"Kechirasiz bizda {k} yo'q")    


    
 
    
 
    
 
    
 
    
 
    
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  