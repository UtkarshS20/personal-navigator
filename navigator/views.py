from django.http import HttpResponse
def links(request):
    return HttpResponse('<h1>Anime List</h1>\n <a href="https://gogoanime.pe/category/kanojo-okarishimasu">Rental Girlfriend</a><br><a href="https://gogoanime.vc/category/fairy-tail">Fairy Tail</a><br><a href="href="https://gogoanime.vc/category/gintama">Gintama</a>')