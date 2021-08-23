# -*- coding: utf-8 -*-
"""
Created on Mon Jun 28 14:23:46 2021

@author: Пользователь
"""

#car0 = {
 #       'model':'lacetti',
  #      'rang':'oq',
   #     'yil':2018,
    #    'narh':13000,
     #   'km':50000,
      #  'karobka':'avtomat'
       # }

#car1 = {
 #       'model':'nexia',
  #      'rang':'kok',
   #     'yil':'2016',
    #    'narh':'12000',
     #   'km':'30000',
      # 'karobka':'ruchnay'
       # }

#car2 = {
        
 #       'model':'gentra',
  #      'rang':'qora',
   #     'yil':'2020',
    #    'narh':40000,
     #   'km':'35000',
      #  'karobka':'avtomat',
       # }

#cars = [car0,car1,car2]

#for car in cars:
 #   print(f"{car['model'].title()},"
  #        f"{car['rang']} rang, "
   #       f"{car['yil']} yil,"
    #      f"{car['narh']} $,"
     #     f"{car['km']} km , "
      #    f"{car['karobka']} karobka")
#
#print(cars[0])
#print(cars[1])
#print(cars[2])

#print(f"Rangi {cars[0]['rang']}  {cars[0]['model']} ")
#________________________________________________________________________________




#malibus = []
#for n in range(10):
 #   new_car = {
  #      'model':'malibu',
   #     'rang':None, 
       # 'yil':2020,
    #    'narh':None, 
     #   'km':0,
      #  'korobka':'avto'
       # }
   # malibus.append(new_car)
    


#print(malibus)



#for malibu in malibus[:3]:
 #   malibu['rang'] = 'qizil'

#for malibu in malibus[3:6]:
 #   malibu['rang'] = 'qora'
    
#for malibu in malibus[6:]:
 #   malibu['rang'] = 'qora'
  #  malibu['karobka'] = 'mexanik'
    
    
    
#for malibu in malibus:
 #   if malibu['korobka'] == 'avto':
  #      malibu['narh'] = 40000
   # else:
    #    malibu['narh'] = 35000
    
#print(malibus)

#___________________________________________________________________________________



#dasturchilar = {
    
 #   'ali':['python','c++'],
  #  'vali':['java','python'],
   # 'hasan':['c#','php'],
    #'anvar':['mysql', 'web'],
    #'jasur':['c++','js'],
     #  }

#for ism, tillar in dasturchilar.items():
 #   print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: " , end=' ')
  #  for til in tillar:
   #     print(til.upper())
        
        
#for ism, tillar in dasturchilar.items():
 #   print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi: ")
  #  for til in tillar:
   #     print(f"{til.upper()} ",  end='  ')


#______________lug'at ichida lug'at_________________________________________________


#hamkasblar = {
 #   'alisher':{'familiya':'qarshiyev',
  #             'tyil':1995,
   #            'malumoti':'oliy',
    #           'yoshi':26,
     #          'tillar':['python','c++'],                              
      #         },
    #'sunnat':{'familiya':'qarshiboyev',
     #         'tyil':1998,
      #        'malumoti':'oliy',
       #      'yoshi':23,
        #      'tillar':['js','c#'],
              
        #      },
    
    #'lochin':{'familiya':'xaytboyev',
     #         'tyil':1998,
      #        'malumoti':'o\'rta',
       #       'yoshi':'20',
        #      'tillar':['java','php']
         #     },
    #'zafar':{'familiya':'nurmatov',
     #        'tyil':1997,
      #       'malumoti':'oliy',
       #      'yoshi':'24',
        #     'tillar':['cisco','web']
         #    }
    
    #}

#for ism, info in hamkasblar.items():
 #   print(f"\n{ism.title()} {info['familiya'].title()} "
  #        f"{info['tyil']}-yilda  tug'ilgan "
   #       f" ma'lumoti  {info['malumoti']} "
    #      f"yoshi {info['yoshi']} da "
     #     f"\nQuyidagi dasturlash tillarini biladi: ")

   # for til in info['tillar']:
    #    print(f"{til.upper()}")

#________amaliyot____________________________________________+++++++++++++++++++++++++==============

 

#navoiy = {
 #   'ism':'alisher',
  #  'familiya':'navoiy',
   # 'tyili':'1441',
    #'tjoyi':'hirot',
    #'yashagan':'63',
    #'asari':['layli majnun','farhod shirin','sabai sayyor','saddiy iskandar']
    #}


#bobur = {
 #   'ism':'bobur',
  #  'familiya':'zahriddin muhammad',
   # 'tyili':'1483',
    #'tjoyi':'samarqand',
    #'yashagan':'60 ' ,
    #'asari':['boburnoma','shohnoma']
    #}

#amir_temur = {
 #   'ism':'amir',
  #  'familiya':'temur',
   # 'tyili':'1336',
    #'tjoyi':'shahrisabz',
    #'yashagan':'68',
    #'asari':['saydana','temur tuzuklari']
    
    #}


#olim = [navoiy,bobur,amir_temur]

#for n in olim:
 #   print(f"\n{n['ism'].title()} "
  #        f"{n['familiya'].title()} "
   #       f"{n['tyili']}-yilda {n['tjoyi'].title()}da tavallud topgan "
    #      f"{n['yashagan']} yil yashagan. "
     #     f"\nQuyidagi asarlarni yozgan:")
    #for asar in n['asari']:
     #   print(asar.title())
              
#________________amaliyot________+++++++++++++___________+_+++++++++++_+_+_+_+++++++++++++++_________________



#kinolar = {
  #  'zafar':['panox','taxi1','terminator'],
   # 'alisher':['brusli','vandam','jekchan'],
    #'sunnat':['hindch','gooliwood','hollivood'],
    #'lochin':['rota','titanic','wuick']
    #}

#for k,q   in kinolar.items():
 #   print(f"\n{k.title()}ning yoqtirgan kinolari: ")
  #  for kino in q:  
   #     print(f"{kino.upper()}")

#____________________________amaliyot___________++++++++++++++_______________+===========


davlatlar = {
    'uzbekiston':{'poytaxt':'toshkent',
                  'hududi':448974,
                  'aholisi':33000000,
                  'pul birligi':'so\'m'},
    
    'turkmaniston':{'poytaxt':'ashxabad',
                  'hududi':5458974,
                  'aholisi':2500000,
                  'pul birligi':'manat'},
    
    'tojikiston':{'poytaxt':'dushanbe',
                  'hududi':328974,
                  'aholisi':780000,
                  'pul birligi':'kyupira'},
    
    'AQSH':{'poytaxt':'singapur',
                  'hududi':9832974,
                  'aholisi':93830000,
                  'pul birligi':'dollor'},
    
    }

for k,q in davlatlar.items():
    print(f"\n{k.title()}ning poytaxti {q['poytaxt'].title()}:",
         f"\nXududi {q['hududi']} kv km",
         f"\nAholi soni {q['aholisi']}", 
         f"\nPul birligi {q['pul birligi']} ")
  
















































       