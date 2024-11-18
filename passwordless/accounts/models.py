from django.db import models

# Create your models here.
class Encrypted_Data(models.Model):    
    id=models.AutoField(primary_key=True, unique=True) 
    USERCODE=models.CharField(unique=True, max_length=200) 
    First_Name=models.TextField(max_length=128)
    Last_Name=models.TextField(max_length=128)
    Address=models.TextField(max_length=128)
    Phone=models.TextField(max_length=128)
    National_Identity_Code=models.TextField(max_length=128)
    BirthDate=models.TextField(max_length=128)
    Country=models.TextField(max_length=128)
    City=models.TextField(max_length=128)
    Zip_Code=models.TextField(max_length=128)

    def ___str__(self):
        return self.USERCODE


class Students (models.Model):
    id=models.AutoField(primary_key=True)
    Email=models.CharField(max_length=55, unique=True)
    Password=models.CharField(max_length=12)
    Email=models.CharField(max_length=55)
    Phone_MAC_Address=models.CharField(max_length=23)
    PC_MAC_Address=models.CharField(max_length=23)
    USERCODE=models.ForeignKey(Encrypted_Data, on_delete=models.CASCADE, unique=True)
    Affiliation=models.TextField()
    Inscription_Year=models.DateField()
    Phone=models.CharField(max_length=14)

    def str (self):
        return self.id


class Encryption_Keys (models.Model): 
    id=models.AutoField (primary_key=True) 
    Encryption_Code=models.CharField(max_length=128) 
    Generation_DateTime=models.DateTimeField()
    Expiering_DateTime=models.DateTimeField()
    USERCODE=models.ForeignKey(Encrypted_Data, on_delete=models. CASCADE, unique=True)
    def str (self):
        return self.id
