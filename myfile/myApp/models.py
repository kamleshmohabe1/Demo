from django.db import models
class register(models.Model):
	Fname=models.CharField(max_length=50,null=True)
	Lname=models.CharField(max_length=50,null=True)
	Email=models.CharField(max_length=50,null=True)
	Phone=models.CharField(max_length=50,null=True)


