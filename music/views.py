from django.http import HttpResponse
from .models import Album
from django.http import Http404
from django.shortcuts import render

def index(request):
    all_albums = Album.objects.all()
    html = ''
    for album in all_albums:
        url = '/music/'+str(album.id)+'/'
        html += '<a href="'+url+'">'+album.album_title+'</a><br>'

    return HttpResponse(html)

def detail(request, album_id):
    try:
        album = Album.objects.get(id=album_id)
    except Album.DoesNotExist:
             raise Http404("Album does not exist.")
    return render(request, 'music/detail.html', {'detail':album})