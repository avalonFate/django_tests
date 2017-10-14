import django.shortcuts
from django.http import JsonResponse
from django.db.models import F, Q, Sum
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from datetime import date
# Create your views here.


# 查询所有图书并显示
def index(request):
    strs = 'request: path %s <br> request: encoding %s <br> ' % (request.path, request.encoding,)
    return HttpResponse(strs)


# 逻辑删除指定编号的图书
def delete(request, id):
    book = BookInfo.objects.get(pk=int(id))
    book.isDelete = True
    book.save()
    return django.shortcuts.redirect('/')


def create(request):
    book = BookInfo()
    book.btitle = '流星蝴蝶剑'
    book.bpub_date = date(1995,12,30)
    book.save()
    #转向到首页
    return django.shortcuts.redirect('/')


def show1(requset, id1,id2,id3):
    return HttpResponse("id:%s %s %s " %(id1,id2,id3))


def get1(request):
    return django.shortcuts.render(request, 'booktest/get1.html')


def get2(request):
    dic = request.GET
    a = dic.get('a', '未找到')
    b = dic.get('b', '未找到')
    c = dic.get('c', '未找到')
    context_ = {'a': a, 'b': b, 'c': c,}
    return django.shortcuts.render(request, 'booktest/get2.html', context_)


def get3(request):
    dic = request.GET
    a = dic.getlist('a', '未找到')
    b = dic.get('b', '未找到')
    c = dic.get('c', '未找到')
    context_ = {'a': a, 'b': b, 'c': c,}
    return django.shortcuts.render(request, 'booktest/get3.html', context_)


def post1(request):
    return django.shortcuts.render(request, 'booktest/post1.html')

def post2(request):
    dic = request.POST
    uname = dic.get('uname')
    upwd = dic.get('upwd')
    ugender = dic.get('ugender')
    uhobby = dic.getlist('uhobby')
    context_ = {'uname': uname, 'upwd': upwd, 'ugender': ugender, 'uhobby': uhobby}
    return django.shortcuts.render(request, 'booktest/post2.html', context_)


def json1(request):
    return django.shortcuts.render(request, 'booktest/json1.html')


def json2(request):
    return JsonResponse({'h1':'hello','h2':'world'})


def red1(request):
    return HttpResponseRedirect('/')

def cookie_set(request):
    response = HttpResponse("<h1>设置Cookie，请查看响应报文头</h1>")
    response.set_cookie('h1', 'hello django',expires=60*60*24*14)
    return response


def cookie_get(request):
    response = HttpResponse("读取Cookie，数据如下：<br>")
    # if request.COOKIES.get('h1'):
    if 'h1' in request.COOKIES:
        response.write('<h1>' + request.COOKIES['h1'] + '</h1>')
    return response


def session_test(request):
    request.session['h1'] = 'hello'
    return HttpResponse("写完session了")


def session_get(request):
    return HttpResponse(request.session.get('h1'))


def session_delete(request):
    # del request.session['h1']
    request.session.clear()
    return HttpResponse('删除')