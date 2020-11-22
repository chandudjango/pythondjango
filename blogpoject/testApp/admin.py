from django.contrib import admin
from testApp.models import Post
# Register your models here.
class PostAdmin(admin.ModelAdmin):
    list_display=['title','slug','author','body','publish','created','updated','status']
    prepopulated_fields={'slug':('title',)}
    list_filter=('status','created','updated','author')
    search_fields=('title','body')
    raw_id_fields=('author',)
    date_hierarchy='publish'
    ordering=['status','publish','created','updated']
admin.site.register(Post,PostAdmin)
