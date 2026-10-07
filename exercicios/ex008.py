n1=float(input("Digite uma medida em metros: "))
h=n1/100
q=n1/1000
dam=n1/10
d=n1*10
c=n1*100
m=n1*1000
print ('{:.2f} equivale a\n{:.3f}km \n{:.2f}hm \n{:.1f}dam \n{:.1f}dm \n{:.1f}cm \n{:.0f}mm'.format(n1, q, h,dam, d, c, m))
