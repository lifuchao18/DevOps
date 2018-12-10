#encoding=utf-8
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect 
from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse

from web.models import UserMenu, OsInfo
# Create your views here.

def userLogin(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    user = authenticate(username=username,password=password)
    infor = u'用户名或密码错误'
    if username == '' or password == '':
        return render(request, "login.html")
    else:
        if user is not None:
            if user.is_active:
                login(request,user)
                return redirect('/index/')
        else:
             return render(request, "login.html", {'infor': infor})
def userLogout(request):
    logout(request)
    return HttpResponseRedirect('/login/')

@login_required
def Index(request):
    order_list = UserMenu.objects.all()
    list2 = []
    for i in order_list:
        if i.m_id == 1:
            order1 = i.title
        elif i.m_id == 2:
            order2 = i.title
    for s in order_list:
        list1 = []
        if s.master == 1:
            list1.append(s.submenu_sort)
            list1.append(s.title)
            list2.append(list1)
    f_order = dict(x for x in list2)
    return render(request, "index.html", {'order1': order1, 'order2': order2,
        'f_order': f_order
    })

def OsView(request):
    data = OsInfo.objects.all()
    return render(request,'access/os_view.html',locals())

def delete_osinfo(request,_id):
    try:
        data = OsInfo.objects.get(pk=_id).delete()
    except OsInfo.DoesNotExist:
        pass
    return HttpResponseRedirect(reverse('osview'))

def OsCreat(request):
    if request.method == 'POST':
        ip = request.POST['ip']
        cpu = request.POST['cpu']
        mem = request.POST['mem']
        OsInfo.objects.create(ip=ip,cpu=cpu,mem=mem)
        return redirect('/oscreat/')
    return render(request, 'access/os_creat.html')

def OsUpdate(request,_id):
    try:
        osdata = OsInfo.objects.get(pk=_id)
    except OsInfo.DoesNotExist:
        return HttpResponseRedirect(reverse('osview'))
    if request.method == 'POST':
        for key,value in request.POST.iteritems():
            if value and hasattr(osdata,key):
                setattr(osdata,key,value)
        osdata.save()
        return HttpResponseRedirect(reverse('osview'))
    return render(request,'access/os_update.html',context={'osdata':osdata})
