from django.db import models
import datetime
# Create your models here.


now=datetime.datetime.now()


class Note(models.Model):
    nid=models.IntegerField()
    name=models.CharField(max_length=128)
    txt=models.TextField()
    date_created=models.DateTimeField("Date Created")
    date_edited=models.DateTimeField("Date last Edited")
    last_change=models.CharField(max_length=128)
    
    #def __init__(self,nm="New Note",txt="Please Enter text"):
	#self.nid=0;       
	#self.name="Post-It Note"
        #self.txt=""
        #self.date_created=now
        #self.date_edited=now
        #self.last_change="No Change"
        
    def update_name(self,newname):
        self.name=newname
        self.date_edited=now
        self.last_change="Name Changed"

    def edit_text(self,newtxt):
        self.txt=txt+newtxt
        self.date_edited=now
        self.last_change="Content Changed"

    class Admin:
    	pass

    def __str__(self):
    	return "Note(name = '%s')" &self.name
    
