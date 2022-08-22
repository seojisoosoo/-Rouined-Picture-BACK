
# Create your views here.
from operator import index
from django.shortcuts import render, redirect, get_object_or_404
from .models import Photo
from django.utils import timezone
from django.http import JsonResponse
import json


def home(request):
    if request.method == 'GET':
        photos = Photo.objects.all()
        photo_list = []
        for photo in photos:
            photo_list.append({
                'id': photo.id,
                'img':photo.img,
                'title': photo.title,
                'writer': photo.writer,
                'body': photo.body, })

        return JsonResponse({
            'data': photo_list
        })
    elif request.method == 'POST':
        body = json.loads(request.body.decode('utf-8'))

        photo = Photo.objects.create(
            img=body['img'],
            title=body['title'],
            writer=body['writer'],
            body=body['body'],
            pub_date=timezone.now()
        )
        return JsonResponse({
            'ok': True,
            'data': {'img':photo.img,
                    'title': photo.title,
                     'writer': photo.writer,
                     'body': photo.body, }
        })
def update(request, id):
    if request.method == 'PUT':
        body = json.loads(request.body.decode('utf-8'))

        update = get_object_or_404(Photo, pk=id)
        # update = get_object_or_404(photo, pk=index)
        # update = photo.objects.get(id=id)
        # update.id = body['id']
        update.img=body['img']
        update.title = body['title']
        update.writer = body['writer']
        update.body = body['body']
        update.pub_date = timezone.now()
        update.save()
        return JsonResponse({
            'ok': True,
            'data': {
                # 'id': update.id,
                'img':update.img,
                'title': update.title,
                'writer': update.writer,
                'body': update.body, }
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
        like_b = get_object_or_404(Photo, id=id)
        like_b.like_count += 1
        like_b.save()
        return JsonResponse({
            'ok':True,
            'data':{
                'like':like_b
            }
        })