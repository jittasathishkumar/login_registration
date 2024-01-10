from django.contrib import admin
from .models import info,issue


class ADMIN(admin.ModelAdmin):
    list_display=['Name','Email','Mobile','Address','Password']
    search_fields=['Name','Email','Mobile','Address','Password']
admin.site.register(info,ADMIN)



class Admin1(admin.ModelAdmin):
    list_display=['Name','Mobile','concern','query','feedback']
admin.site.register(issue,Admin1)




