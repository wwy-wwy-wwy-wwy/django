from django.http import HttpResponse
from django.shortcuts import render
from .models import *


# Create your views here.

# 注册
def index_view(request):
    m = request.method
    if m == 'GET':        #等提交get请求时才会出发此选项，否则一直执行else的语句
        return render(request, 'register.html')
    else:
        # 获取请求参数
        uname = request.POST.get('uname', '')
        pwd = request.POST.get('pwd', '')
        print(uname)
        print(pwd)
        if uname and pwd:
            # 创建模型对象
            stu = Student(sname=uname, spwd=pwd)
            # 插入数据库
            stu.save()
            return HttpResponse('注册成功')
        else:
            return HttpResponse('注册失败')

# 查询
def test_view(request):
    m = request.method
    if m == 'GET':
        return render(request, 'test.html')
    else:
            uname = request.POST.get('uname','')
            truedata = []
            try:
                all_student = Student.objects.filter(sname=uname)

                print(all_student,'------------all_student')
                for i in all_student:
                    result = {
                        'name':i.sname,
                        'pwd':i.spwd,
                    }
                    truedata.append(result)
                print(truedata,'-----------------true data1')
                # truedata = {
                #     'info':truedata[0]
                # }
                truedata=truedata[0]
                print(truedata, '-----------------true data2')
                return render(request, 'test.html', {'fontdata': truedata})
            except:
                return HttpResponse('未查询到结果！')

#天气
def weather_view(request):
    m = request.method
    if m == 'POST':                 #当提交post请求时促发此选项
        return render(request, 'temp.html')
    else:
        return render(request, 'weather.html')

#气温
def temp_view(request):
    return render(request,'temp.html')

