from django.db import models

# Create your models here.
class Expenses(models.Model):
	username = models.CharField(max_length=100, primary_key = True)

class UserAccounts(models.Model):
	accountname = models.CharField(max_length = 100)
	user = models.ForeignKey(Expenses)