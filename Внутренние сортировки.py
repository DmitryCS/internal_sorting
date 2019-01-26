from random import randint
from time import time

#Проверка правильности сортировки
def check(ch):
    for i in range(1,len(ch)):
        if ch[i-1]>ch[i]:
            return "No"
    return "Yes"
#Пузырьковая сортировка
def BubbleSort(a1):
    t=time()
    a=a1.copy()
    R=len(a)-1
    wasswap=True
    while R>0 and wasswap:
        wasswap=False
        for j in range(R):
            if a[j]>a[j+1]:
                a[j],a[j+1]=a[j+1],a[j]
                wasswap=True
        R=R-1
    return time()-t
#Шейкерная сортировка
def CocktailSort(b1):
    t=time()
    b=b1.copy()
    left=0; right=len(b)-1
    while left<=right:
        for i in range(left,right):
            if b[i]>b[i+1]:
               b[i],b[i+1]=b[i+1],b[i]
        right-=1
        for i in range(right,left,-1):
            if b[i]<b[i-1]:
                b[i],b[i-1]=b[i-1],b[i]
        left+=1
    return   time()-t
#Сортировка Шелла
def ShellSort(c1):
    t=time()
    c=c1.copy()
    n=len(c); d=n//2+1
    while d>0:
        for i in range(n-d):
            if c[i]>c[i+d]:
                c[i],c[i+d]=c[i+d],c[i]
        d-=1
    return  time()-t
#Сортировка выбором
def SelectionSort(d1):
    t=time()
    d=d1.copy()
    n=len(d)
    for i in range(n-1):
        minR=d[i]; k=i
        for j in range(i+1,n):
            if d[j]<minR:
                minR=d[j]; k=j
        d[k]=d[i]; d[i]=minR
    return time()-t
#Сортировка простыми вставками
def InsertionSort(f1):
    t=time()
    f=f1.copy(); n=len(f)
    for i in range(1,n):
        r=f[i]
        j=i-1
        while r<f[j] and j>=0:
            f[j+1]=f[j]; j-=1
        f[j+1]=r
    return time()-t
#Моя сортировка
def MySort(e1):
    t=time()
    e=e1.copy()
    for i in range(len(e)):
        for j in range(i):
            if e[i]<e[j]:
                e[i],e[j]=e[j],e[i]
    return  time()-t
#Быстрая сортировка
def QuickSort(g,b,e): #массив,индекс первого и последнего элемента
    #w=g[(b+e)//2]
    w=g[randint(b,e)]
    l=b;r=e
    while l<=r:
        while g[l]<w:
            l+=1
        while w<g[r]:
            r-=1
        if l<=r:
            g[l],g[r]=g[r],g[l]
            l+=1; r-=1
    if b<r:
        QuickSort(g,b,r)
    if l<e:
        QuickSort(g,l,e)
# Сортировка подсчетом
def BadSort(j1):
    t=time()
    j=j1.copy()
    c=[0]*(max(j)+1)
    b=[]
    for i in range(len(j)):
        c[j[i]]+=1
    for i in range(len(c)):
        for d in range(c[i]):
            b.append(i)
    return time()-t
#Бинарный поиск (для сортировки Бинарными вставками)
def BinarySearch(a,left,right,key):
    #left=0;right=len(a)-1; 
    while True:
        w=(left+right)//2
        if key>a[w]:
            left=w+1
        elif key<a[w]:
            right=w-1
        else:
            return w
        if left>right:
            return left
#Сортировка Бинарными вставками
def B(o1):
    t=time()
    o=o1.copy(); n=len(o)
    for i in range(1,n): #i = 1 to n - 1
        r=o[i]
        j = i - 1
        k = BinarySearch(o, 0, j, o[i])
        for m in range(j,k-1,-1): #m = j downto k
            o[m], o[m+1] = o[m+1],o[m]
    return time()-t
if __name__=='__main__':
    a=[]
    n=5000
    print('Количество элементов: ', n)
    for i in range(n):
        a.append(randint(1,100000))
    #print('Массив отсортирован? ',check(a))
    print('Рандомный набор элементов.')
    print('Пузырьковая сортировка: ',BubbleSort(a))
    print('Шейкерная сортировка: ',CocktailSort(a))
    print('Сортировка Шелла: ', ShellSort(a))
    print('Сортировка выбором:  ', SelectionSort(a))
    print('Сортировка простыми вставками: ', InsertionSort(a))
    print('Сортировка бинарными вставками: ', B(a))
    print('\"Моя сортировка\": ', MySort(a))
    print('Сортировка подсчетом: ',BadSort(a))
    t=time()
    QuickSort(a,0,len(a)-1)
    print('Быстрая сортировка: ',time()-t)
    input('Нажмите Enter для завершения программы.')
