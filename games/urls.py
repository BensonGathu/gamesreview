from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='index'),
    path('reviews/<int:id>/',views.reviews,name='reviews'),
    path('game/<int:id>/',views.singlegame,name='singlegame'),
    path('search/',views.search_game,name='searchgame'),
    path('profile/',views.profile,name='profile'),
    path('uploadgame/',views.upload_game,name='uploadgame'),
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)