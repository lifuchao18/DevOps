#encoding=utf-8
from django.contrib import admin
from .models import Post, UserMenu 
# Register your models here.

class PostAdmin(admin.ModelAdmin):     
    list_display = ('title', 'slug', 'author', 'publish', 'status')
    list_filter = ('status', 'created', 'publish', 'author')
    search_fields = ('title', 'body')
    prepopulated_fields = {'slug': ('title',)}     
    raw_id_fields = ('author',)     
    date_hierarchy = 'publish'     
    ordering = ['status', 'publish']
class UserMenuAdmin(admin.ModelAdmin):
    list_display = ('m_id', 'title', 'properties', 'status')
    list_filter = ('status','properties')
    search_fields = ('title', 'status')

admin.site.register(Post, PostAdmin)
admin.site.register(UserMenu, UserMenuAdmin)
