
# Create your views here.
from operator import index
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from django.utils import timezone
from django.http import JsonResponse
import json

BASE_URL = "http://127.0.0.1:8000"

def home(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        photo_list = []
        for photo in photos:
            photo_list.append({
                'id': photo.id,
                'img':BASE_URL+"/media/"+str(photo.img),
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
                        'img': BASE_URL+"/media/"+str(photo.img),
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
                'img':BASE_URL+"/media/"+str(update.img),
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

# def like(request,id):
#     if request.method=='POST':
#         photos= Photo.objects.all()
#         likes_list = {}
#         for photo in photos:
#             # likes_list.append({
#             #     'like_count': photo.like_count+1
#             #      })
#             likes_list[photo.id]=photo.like_count+1

#         return JsonResponse({
#             'ok':True,
#             'data': likes_list
#         })
        