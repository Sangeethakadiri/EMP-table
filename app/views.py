from django.shortcuts import render
from app.models import *
from django.db.models.functions import Length
# Create your views here.
from django.db.models import Q
from django.http import HttpResponse


def display_depts(request):
    LOT=DEPT.objects.all()#it will fetch all the data
    LOT=DEPT.objects.order_by('Loc')#it fetch the assencending order
    LOT=DEPT.objects.order_by('-Loc')#it will fetch the desending order
    LOT=DEPT.objects.order_by(Length('Loc'))#it will arrange the data in asscen order acccording to location based on asci values
    LOT=DEPT.objects.order_by(Length('Loc').desc())#it will arrange the data in dec order acccording to location based on asci values
    LOT=DEPT.objects.filter(DEPTNO=10)#it will fetch only deptno 10 data
    LOT=DEPT.objects.exclude(Dname='SALES')#it will fetch all data except dname=sales 
    LOT=DEPT.objects.filter(DEPTNO__gt=20)#it will fetch greater than 20 deptno
    LOT=DEPT.objects.filter(DEPTNO__lt=20)#it will fetch less than 20 deptno
    LOT=DEPT.objects.filter(DEPTNO__gte=20)#it will fetch deptno 20 and greaterthan deptno 20 values
    LOT=DEPT.objects.filter(DEPTNO__lte=20)#it will fetch deptno 20 and lessthan deptno 20 values
    

def update_dept(request):
    DEPT.objects.filter(DEPTNO=10).update(Loc='bangalore')


    d={'depts':LOT}
    return render(request,'display_dept.html',context=d)



def display_emp(request):
    LOT=EMPNO.objects.all()
    LOT=EMPNO.objects.filter(HIREDATE='1981-2-20')#it will fetch who r join in that specific data
    LOT=EMPNO.objects.exclude(HIREDATE='1981-2-20')#it will fetch who not joined in that specific data
    LOT=EMPNO.objects.filter(HIREDATE__year='1982')#it fecth who join in year 1982
    LOT=EMPNO.objects.filter(HIREDATE__month='5')#it will fetch who join in month of may only
    LOT=EMPNO.objects.filter(HIREDATE__day='23')#it will fetch who join in day 23 only
    LOT=EMPNO.objects.filter(JOB__startswith='s')#it will fetch  who's job starts with 's'
    LOT=EMPNO.objects.filter(JOB__endswith='k')#it will fetch whos job endswith 'k'
    LOT=EMPNO.objects.filter(JOB__contains='r')#it will fetch whos job having the character r
    LOT=EMPNO.objects.filter(ENAME__in=('SMITH','ALLEN','KING'))#IT will fetch only smith.allen.king
    LOT=EMPNO.objects.filter(Q(SAL__gt=800)&Q(SAL__lt=2000))#it will fetch the data who salary is greaterthan 800 and lessthan 2000
    LOT=EMPNO.objects.all()[0:5]#it will fetch the only 5 records

    
    d={'emp':LOT}
    return render(request,'display_emp.html',context=d)