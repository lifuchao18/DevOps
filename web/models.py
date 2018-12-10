#encoding=utf-8
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.

class Post(models.Model):     
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )
    title = models.CharField(max_length=250)     
    slug = models.SlugField(max_length=250, unique_for_date='publish')     
    author = models.ForeignKey(User, related_name='blog_posts')     
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)     
    created = models.DateTimeField(auto_now_add=True)     
    updated = models.DateTimeField(auto_now=True)     
    status = models.CharField(max_length=10,                               
    choices=STATUS_CHOICES, default='draft')

    class Meta:         
        ordering = ('-publish',)

    def __str__(self):         
        return self.title

class UserMenu(models.Model):
    STATUS_CHOICES = (
        ('enable', 'enable'),
        ('disable', 'disable'),
    )
    P_CHOICES = (
        ('FirstOrder', 'FirstOrder'),
        ('SecondOrder', 'SecondOrder'),
    )
    m_id = models.AutoField(primary_key=True)
    title = models.CharField(blank=True, null=True, verbose_name=u'菜单内容', max_length=25)
    properties = models.CharField(verbose_name=u'菜单等级', max_length=25,
    choices=P_CHOICES, default='SecondOrder')
    status = models.CharField(verbose_name=u'是否启用', max_length=10,
    choices=STATUS_CHOICES, default='enable')
    master = models.IntegerField(blank=True, null=True, verbose_name=u'上级菜单id')   
    submenu_sort = models.PositiveIntegerField(blank=True, null=True, verbose_name=u'子菜单顺序')
    class Meta:
        verbose_name = '菜单栏'
        verbose_name_plural = '菜单栏' 

class OsInfo(models.Model):
    ip = models.GenericIPAddressField()
    cpu = models.PositiveIntegerField(blank=False, null=False)
    mem = models.PositiveIntegerField(blank=False, null=False)
    class meta:
        verbose_name = 'OS信息'
        verbose_name_plural = 'OS信息' 
