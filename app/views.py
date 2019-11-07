from django.shortcuts import render, redirect
from app.models import Album, Song


def album_list(request):
    albums = Album.objects.all()
    return render(request, "album_list.html", {"albums": albums})


def album_detail(request, id):
    album = Album.objects.get(id=id)
    return render(request, "album_detail.html", {"album": album})

def new_song(request, id):
    if request.method == "GET":
        return render(request, "album_detail.html")
    elif request.method == "POST":
        album = Song(title=request.POST["title"], seconds=int(request.POST["seconds"]), album_id=id)
        album.save()
        return redirect(f"album/{id}", {"album": album})