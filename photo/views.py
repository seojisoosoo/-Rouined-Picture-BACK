
# Create your views here.
from operator import index
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo,Visitor

from django.utils import timezone
from django.http import JsonResponse
import json

# BASE_URL = "http://127.0.0.1:8000"
# BASE_URL='https://rouined-photo-exhibition.herokuapp.com'

def home(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        photo_list = []
        for photo in photos:
            photo_list.append({
                'id': photo.id,
                # 'img':BASE_URL+"/media/"+str(photo.img),
                'img':"/media/"+str(photo.img),

                'title': photo.title,
                'writer': photo.writer,
                'body': photo.body,
                'password':photo.password,
                'like_count':photo.like_count
                 })

        return JsonResponse({
            'data': photo_list
        })
    elif request.method == 'POST':
        # body = json.loads(request.body.decode('utf-8'))
        body = request.POST
        file = request.FILES
        print(body, file)

        photo = Photo.objects.create(
            title=body['title'],
            writer=body['writer'],
            body=body['body'],
            password=body['password'],
            pub_date=timezone.now()
        )

        if(file['imgFile']): photo.img = file['imgFile']
        photo.save()

        return JsonResponse({
            'ok': True,
            'data': {
                        # 'img': BASE_URL+"/media/"+str(photo.img),
                        'img': "/media/"+str(photo.img),
                        'title': photo.title,
                        'writer': photo.writer,
                        'body': photo.body,
                        'password': photo.password
                     }
        })


def update(request, id):
    if request.method == 'POST':
        # body = json.loads(request.body.decode('utf-8'))
        body = request.POST
        file = request.FILES
        print(body,file)
        update = get_object_or_404(Photo, pk=id)
        # update = get_object_or_404(photo, pk=index)
        # update = photo.objects.get(id=id)
        # update.id = body['id']
        # update.img=body['imgFile']
        update.title = body['title']
        update.writer = body['writer']
        update.body = body['body']
        update.password = body['password']
        update.pub_date = timezone.now()
        # update.save()
        if(request.FILES): update.img = file['imgFile']
        update.save()

        return JsonResponse({
            'ok': True,
            'data': {
                # 'id': update.id,
                # 'img':BASE_URL+"/media/"+str(update.img),
                'img':"/media/"+str(update.img),
                'title': update.title,
                'writer': update.writer,
                'body': update.body, 
                'password': update.password}
        })
def delete(request, id):
    if request.method == 'DELETE':
        delete = get_object_or_404(Photo, pk=id)
        # delete = photo.objects.get(id=id-1)

        delete.delete()
        return JsonResponse({
            'ok': True,
            'data': None
        })

def like(request,id):
    if request.method == 'POST':
        like_b = get_object_or_404(Photo, pk=id)
        # like_b = get_object_or_404(Photo, id=id)

        # like_b.like_count += 1
        like_b.like_count =like_b.like_count + 1

        like_b.save()
        return JsonResponse({
            'ok':True,
            'data':{
                'id':like_b.id,
                'like':like_b.like_count
            }
        })


def visitor(request):
    if request.method == 'GET':
        visitors = Visitor.objects.all()
        visitor_list = []
        for visitor in visitors:
            visitor_list.append({
                'id': visitor.id,
                'visitor':visitor.visitor,
                'year':visitor.date.year,
                'month':visitor.date.month,
                'day':visitor.date.day
                 })

        return JsonResponse({
            'data': visitor_list
        })
    elif request.method == 'POST':
        
        body = json.loads(request.body.decode('utf-8'))
        
        visitor= Visitor.objects.create(
            visitor=body['visitor']
        )
       
        return JsonResponse({
            'ok': True,
            'data': {
                'id':visitor.id,
                        'visitor':visitor.visitor
                     }
        })