from django.db import models

class Login(models.Model):
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    role=models.CharField(max_length=50)


class Patient(models.Model):
    firstname=models.CharField(max_length=50)
    lastname=models.CharField(max_length=50)
    mobilenumber=models.CharField(max_length=50)
    fk_login=models.ForeignKey(Login,on_delete=models.CASCADE)


class Department(models.Model):
    departmentname = models.CharField(max_length=50)
    

class Doctor(models.Model):
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    mobilenumber = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    optiming = models.CharField(max_length=50)
    opaddress = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    fee = models.IntegerField()
    image = models.FileField(upload_to='profile_picture/')
    fk_login = models.ForeignKey(Login,on_delete=models.CASCADE)


class Booking(models.Model):
    date=models.DateField()
    time=models.TimeField()
    doctor_id=models.ForeignKey(Doctor,on_delete=models.CASCADE)
    patient_id=models.ForeignKey(Patient,on_delete=models.CASCADE)