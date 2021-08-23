# -*- coding: utf-8 -*-
"""
Created on Tue Jul 27 09:48:34 2021

@author: Пользователь
"""

#def toliq_ism_yasa(ism,familiya):
 #   """toliq ism qaytaruvchi funksiya"""
  #  toliq_ism = (f" {ism.title()} {familiya.title()}")
   # return toliq_ism
    
#qaytaruvchi = toliq_ism_yasa('zafar','nurmatov')
#print(f"Assalomu alaykum {qaytaruvchi}")
#______________________________________________________________________________________

#def toliq_ismyasa(ism,familiya,otasining_ismi=''):
 #   """otasining ismi bor yo'qligini tekshiradigan qaytaruvchi funksiya"""
 #   if otasining_ismi:
 #       toliq_ism = f"{ism} {familiya} {otasining_ismi}"
 #   else:
 #      toliq_ism = f"{ism} {familiya}"
 #   return toliq_ism.title()    

#qiymat = toliq_ismyasa('zafar','nurmatov',"mo'minovich")
#print(f"Darsga kelmagan talabaning ismi {qiymat}")

#______________________________________________________________________________________

#def avto_malumot(kompaniya, model, rangi, karobka, yili, narhi=None):
 #   """Avtomobillar malumotini lug'atini qaytaradigan  qaytaruvchi funksiya"""
  #  avto = {'kompaniya':kompaniya,
   #         'model':model,
    #        'rangi':rangi,
     #       'karobka':karobka,
      #      'yili':yili,
       #     'narhi':narhi
        #    }
   # return avto

#avtomabil1 = avto_malumot('GM','lacetti','qora','avtomat','2019-yil',)
#avtomabil2 = avto_malumot('GM','gentra','qora','ruchnoy','2020-yil',12000)
#avtolar = [avtomabil1,avtomabil2]
#
#print("Onlayn bozordagi mavjud moshinalar:")

#for n in avtolar:
 #   if n['narhi']:
  #      narh = n['narhi']
   # else:
    #    narh = "Noma'lum"
    #print(f"{n['model']} {n['rangi']} {n['yili']}  Narhi: {narh}")    
      
#_________+++++++++++++++++____________________________________________________________

#    funksiyadan ro'yxat qaytaramiz   

#def  oraliq(min,max,qadam):
 #   sonlar = []
  #  while min<max:
   #     sonlar.append(min)
    #    min+=qadam
    #return sonlar

#print(oraliq(1,10,3))
#print(oraliq(20,100,5))    

#_________________________________________________________________________________

#       avtolar ro'yxatini shakllantiramiz


#def avto_malumot(kampaniya, model, rangi, karobka, yili, narh=None):
 #   """Avtomobillar malumotini lug'atini qaytaradigan  qaytaruvchi funksiya"""
  #  avto = {'kompaniya':kampaniya,
   #         'model':model,
    #        'rangi':rangi,
    #        'karobka':karobka,
    #        'yili':yili,
    #        'narh':narh
    #        }
    #return avto
    

#print("Saytimizdagi avtolar ro'yxatini shakllantiramiz")

#avtolar = []

#while True:
 #   print("\nQuyidagi malumotlarni kiriting: ", end='')
  #  kampaniya = input("Kampaniya nomini kiriting: ")
   # model = input("Modelni kiriting: ")
   # rangi = input("Moshina rangini kiriting: ")
   # karobka = input("Karobkasi qanday? ")
   # yili = input("Yilini kiriting: ")
   # narh = input("Narhini kiriting: ")
    
    
    
   # avtolar.append(avto_malumot(kampaniya, model, rangi, karobka, narh, yili))
   # javob  = input("Yana avto qo'shasizmi: yes/no ")
   # if javob=='no':
    #   break
    

#for avto in avtolar:
 #   if avto['narh']:
 #       narh = avto['narh']
 #   else:
 #       narh = "Noma'lum"
 #   print(f"{avto['rangi'].title()} {avto['model'].title()}, {karobka} korobka. Narhi: {narh}")
    
  #_______________________________++++++++++++++++++__________________________________________            


tub = list(range(1,100))

for n in tub:
  if n%1==0 and n%n==0:
      print(n)


























