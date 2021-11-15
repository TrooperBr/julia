from django.db import models

# Create your models here.




class Produto(models.Model):
	name = models.CharField(max_length=256)
	price = models.FloatField()
	link  = models.CharField(max_length=512)
	image = models.ImageField(upload_to='produtos')
	text  = models.TextField()
	views = models.IntegerField(default=0)


	def __str__(self):
		return self.name