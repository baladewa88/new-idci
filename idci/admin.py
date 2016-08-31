from django.contrib import admin

from .models import Affiliations, Urls, Keywords, Papers, Citations, Authors, Venues

admin.site.register(Papers)
admin.site.register(Urls)
admin.site.register(Keywords)
admin.site.register(Affiliations)
admin.site.register(Citations)
admin.site.register(Authors)
admin.site.register(Venues)

