# -*- coding: utf-8 -*-
"""
Created on Sun May 16 23:54:23 2021

@author: Пользователь
"""

bosh_royxat = []
mevalar = ['olma', 'anjir', 'uzum', 'gilos', 'olxori', 'olcha']

sabzavotlar = ['sabzi', 'kartoshka', 'piyoz', 'turp', 'qovoq']
narxlar=[12000, 20000, 30000, 232423, 111111, 444444]
sonlar = ['bir', 'ikki', 'uch', '1', '2', '3', '4', '5']

print(mevalar[1])
print(mevalar)
#print(mevalar,narxlar,sabzavotlar,sonlar)

sonlar[2] = "to\'rt"
print(sonlar)
print(sonlar)
sonlar.append('olti' )
print(sonlar)
sabzavotlar.insert(2, 'sholg\'om')
narxlar.insert(2, '50000')
print(sabzavotlar,narxlar)

del sonlar[2]
print(sonlar)
sonlar.remove('3')
print(sonlar)

dostlarim = ['Asin', 'Turg\'un', 'Sodiq', 'Muxi']
print('Salom '+dostlarim[1]+' bugun toqqa chiqamizmi?')

print('Salom '+dostlarim[0]+' do\'stim bugun choyxona bormi? '+'\nSalom '+dostlarim[3]+' bugun uyga kelasanmi')

print('yig\'indi = '+str(narxlar[0]+narxlar[1]))
poliz = sabzavotlar.pop(1)
print(sabzavotlar)
print('men bugun bozordan '+poliz+' sotib oldim')

z_shaxslar = ['A.Aripov','M.Yusuf','A.Qayum','Putin','Tramp']
t_shaxslar = ['Amir.T','Beruniy','Ibn sino', 'Xorazmiy']
print(t_shaxslar,z_shaxslar)
























