# Create your views here.
from django.shortcuts import render_to_response,get_object_or_404
from django.http import HttpResponse
from django.template import RequestContext
from Post_It_Notes.post.models import Note 
import datetime
from django.views.decorators.csrf import csrf_exempt

def index(request):
	latest= Note.objects.all().order_by('-id')
	return render_to_response('post/index.htm', {'latest': latest})

def new(request):
	return render_to_response('post/new_note.htm')

def detail(request,nid):
	note=get_object_or_404(Note,pk=nid)
	return render_to_response('post/detail.htm',{'note': note})

@csrf_exempt
def create_note(request):
	n=Note(name='New Note',nid=5,txt=request.POST['txt'],date_created=datetime.datetime.now(),date_edited=datetime.datetime.now(),last_change='None')
	n.save()	
	return index(request)

def delete_note(request,nid):
	n=get_object_or_404(Note,pk=nid)
	n.delete()	
	return index(request)

def update_note(request,nid):
	note=get_object_or_404(Note,pk=nid)	
	return render_to_response('post/update.htm',{'note': note})

@csrf_exempt
def upd(request,nid):
	n=get_object_or_404(Note,pk=nid)	
	n.txt=request.POST['txt']
	n.date_edited=str(datetime.datetime.now())
	n.save()
	n.last_change="Note changed to "+n.txt+"on "+n.date_edited
	n.save()
	return index(request)

