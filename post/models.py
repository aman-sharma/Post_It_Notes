from django.db import models
import datetime
     
PRIORITY_CHOICES = (
      	(1, 'Low'),
      	(2, 'Normal'),
      	(3, 'High'),
    )
        
class Note(models.Model):
    	nid=models.IntegerField(default=0)
   	name=models.CharField(max_length=128)
 	txt=models.TextField()
    	date_created=models.DateTimeField("Date Created")
   	date_edited=models.DateTimeField("Date last Edited")
    	last_change=models.CharField(max_length=128)
      	def __str__(self):
        	return self.name
      	class Admin:
        	pass
