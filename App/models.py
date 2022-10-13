from django.db import models
class prepaid(models.Model):
    pname= models.CharField(max_length=70)
    calls= models.CharField(max_length=200)
    data = models.CharField(max_length=70)
    validity = models.CharField(max_length=70)
    amount=models.IntegerField()
    def __str__(self):
        return self.pname
class postpaids(models.Model):
    id= models.IntegerField(primary_key=True)
    pname= models.CharField(max_length=70)
    calls= models.CharField(max_length=200)
    data = models.CharField(max_length=70)
    validity = models.CharField(max_length=70)
    amount = models.IntegerField()
    def __str__(self):
        return self.pname
class payment(models.Model):
    cname=models.CharField(max_length=80)
    #pname=models.ForeignKey(prepaid,related_name='prepaid',on_delete=models.CASCADE)
    Ano=models.IntegerField()
    edate=models.CharField(max_length=80)
    cvv=models.CharField(max_length=3)
    mobile=models.IntegerField()
    def __str__(self):
        return self.cname
class prepayment(models.Model):
    cname = models.CharField(max_length=80)
    pname=models.CharField(max_length=30)
    Ano=models.IntegerField()
    edate=models.DateField()
    cvv=models.CharField(max_length=3)
    mobile=models.IntegerField()
    date = models.CharField(max_length=80)
    def __str__(self):
        return self.cname
#class payment1(models.Model):
#    id=models.IntegerField(primary_key=True)
#    cname=models.CharField(max_length=80)
#    Amount=models.CharField(max_length=60)
#    UPIaddress=models.CharField(max_length=90)
#    UPInumber=models.CharField(max_length=90)
#buy new sim
class recs(models.Model):
    cname=models.CharField(max_length=70)
    mobile=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=1000)
    def __str__(self):
        return self.cname

class postrecs(models.Model):
    cname=models.CharField(max_length=70)
    mobile=models.IntegerField()
    email=models.EmailField()
    address=models.CharField(max_length=1000)
    Amount = models.CharField(max_length=60)
    date = models.CharField(max_length=80)
    def __str__(self):
        return self.cname

class postpayment1(models.Model):
    #data=models.CharField(max_length=60)
    cname = models.CharField(max_length=70)
    Ano=models.IntegerField()
    edate=models.DateField()
    cvv = models.CharField(max_length=3)

    def __str__(self):
        return self.cname
class Feedback(models.Model):
    name = models.CharField(max_length=70)
    feed = models.CharField(max_length=70)
    def __str__(self):
        return self.name
#class upipayment(models.Model):
 #   id=models.IntegerField(primary_key=True)
  #  cname=models.CharField(max_length=80)
   # Amount=models.CharField(max_length=60)
   # UPIaddress=models.CharField(max_length=90)
    #UPInumber=models.CharField(max_length=90)

# Create your models here.
class payment1(models.Model):
    mobile = models.IntegerField()

class Queries(models.Model):
    name = models.TextField(blank=False,null=False)
    email = models.TextField(blank=False,null=False)
    query = models.TextField(blank=False,null=False)
    phone = models.TextField(blank=False,null=False)
    def __str__(self):
        return str(self.name)



