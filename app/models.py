from django.db import models

# Create your models here.
class DEPT(models.Model):
    DEPTNO=models.IntegerField(primary_key=True)
    Dname=models.CharField(max_length=100)
    Loc=models.CharField(max_length=100)

    def __int__(self):
        return self.DEPTNO



class EMPNO(models.Model):
    EMPNO=models.IntegerField()
    ENAME=models.CharField(max_length=100)
    JOB=models.CharField(max_length=100)
    MGR=models.IntegerField()
    HIREDATE=models.DateField()
    SAL=models.IntegerField()
    COMM=models.IntegerField()
    DEPTNO=models.IntegerField()

    def __int__(self):
        return self.EMPNO
