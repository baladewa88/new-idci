from django.contrib import admin

from .models import Affiliations, Urls, Keywords, Papers, Citations, Authors, Venues
from random import randint

import time
class PapersAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['title','abstract','year', 'venue', 'pages', 'volume', 'number','selfcites','publisher','pubaddress']})]
    list_filter = ('crawldate'),('year')
    list_display = ('id','title','ncites')
    ordering = ('-crawldate',)
    search_fields = ['title']
    
    def save_model(self, request, obj, form, change):
        currentTime = int(round(time.time() * 1000))+randint(0,99)
        obj.id = str(currentTime)
        refCount = Citations.objects.filter(title=form.cleaned_data['title']).count()
        obj.ncites = refCount
        print("ID => "+str(currentTime))
        obj.save()

class CitationsAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['title','authors','venue', 'venuetype', 'year', 'pages', 'editors', 'volume', 'number', 'paperid', 'self', 'publisher','pubaddress']})]
    list_filter = ('authors'),('publisher')
    list_display = ('id','title','authors')
    ordering = ('authors',)

class AffiliasiAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['name','address','url']})]
    list_display = ('name','address','url')
    ordering = ('name',)

class AuthorsAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['paperid','name','affil','address', 'email', 'ord']})]
    list_display = ('name','affil', )
    ordering = ('name',)

class AuthorsAdmin(admin.ModelAdmin):
    fieldsets = [('Description',{'fields':['paperid','name','affil','address', 'email', 'ord']})]
    list_display = ('name','affil', )
    ordering = ('name',)
    
admin.site.register(Papers, PapersAdmin)
admin.site.register(Urls)
admin.site.register(Keywords)
admin.site.register(Affiliations, AffiliasiAdmin)
admin.site.register(Citations, CitationsAdmin)
admin.site.register(Authors, AuthorsAdmin)
admin.site.register(Venues)

