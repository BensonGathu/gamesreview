from django.contrib import admin
from .models import Profile,Game,Review,Forum,Query,Answers
# Register your models here.

admin.site.register(Profile)
admin.site.register(Game)
admin.site.register(Review)
admin.site.register(Forum)
admin.site.register(Query)
admin.site.register(Answers)