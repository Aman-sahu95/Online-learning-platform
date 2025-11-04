from django.shortcuts import render,redirect
from .models import News
from .models import Branch
from .models import Course
from .models import Session
from .models import Study
from mainapp.models import Enquiry
from mainapp.models import Student
from studentapp.models import Feedback

# Create your views here.

def index(request):
    return render(request,'index.html')

def adnews(request):
    if request.method=="POST":
            title=request.POST['title']
            desc=request.POST['desc']
            news=News.objects.create(title=title,desc=desc)
            return redirect('myapp:adnews')
    news=News.objects.all()
    return render(request,'adnews.html',{"news":news})

def adbranch(request):
    if request.method=="POST":
        branch=request.POST['branch']
        branch=Branch.objects.create(branch=branch)
        return redirect('myapp:adbranch')
    branch=Branch.objects.all()
    return render(request,'adbranch.html',{"branch":branch})

def adcourse(request):
    if request.method=="POST":
        course=request.POST['course']
        course=Course.objects.create(course=course)
        return redirect('myapp:adcourse')
    course=Course.objects.all()
    return render(request,'adcourse.html',{"course":course})

def adsession(request):
    if request.method=="POST":
        session=request.POST['session']
        session=Session.objects.create(session=session)
        return redirect('myapp:adsession')
    session=Session.objects.all()
    return render(request,'adsession.html',{"session":session})


def adstudy(request):
    return render(request,'adstudy.html')
def adhome(request):
    st = Study.objects.all()
    stl = len(st)
    st = Student.objects.all()
    stul = len(st)
    n = News.objects.all()
    nl = len(n)
    fe = Feedback.objects.filter(feedtype="Feedback")
    fel = len(fe)
    co = Feedback.objects.filter(feedtype="Complain")
    ca = len(co)
    sug = Feedback.objects.filter(feedtype="Suggestion")
    sul = len(sug)
    return render(request,'adhome.html',locals())

def viewstudy(request):
    st = Study.objects.all() 
    return render(request,'viewstudy.html',locals())

def editnews(request,id):
    if request.method=="POST":
        title=request.POST['title']
        desc=request.POST['desc']
        News.objects.filter(id=id).update(title=title,desc=desc)
        return redirect('myapp:adnews')
    news=News.objects.all()
    n=News.objects.get(id=id)
    return render(request,'adnews.html',{'n':n,'news':news})

def editbranch(request,id):
    if request.method=="POST":
        branch=request.POST['branch']
        Branch.objects.filter(id=id).update(branch=branch)
        return redirect('myapp:adbranch')
    branch=Branch.objects.all()
    b=Branch.objects.get(id=id)
    return render(request,'adbranch.html',{'b':b,'branch':branch})

def editcourse(request,id):
    if request.method=="POST":
        course=request.POST['course']
        Course.objects.filter(id=id).update(course=course)
        return redirect('myapp:adcourse')
    course=Course.objects.all()
    c=Course.objects.get(id=id)
    return render(request,'adcourse.html',{'c':c,'course':course})

def editsession(request,id):
    if request.method=="POST":
        session=request.POST['session']
        Session.objects.filter(id=id).update(session=session)
        return redirect('myapp:adsession')
    session=Session.objects.all()
    s=Session.objects.get(id=id)
    return render(request,'adsession.html',{'s':s,'session':session})

def deletenews(request,id):
    News.objects.filter(id=id).delete()
    return redirect('myapp:adnews')

def deletebranch(request,id):
    Branch.objects.filter(id=id).delete()
    return redirect('myapp:adbranch')

def deletecourse(request,id):
    Course.objects.filter(id=id).delete()
    return redirect('myapp:adcourse')

def deletesession(request,id):
    Session.objects.filter(id=id).delete()
    return redirect('myapp:adsession')

def adstudy(request):
    if request.method=="POST":
        course=request.POST['course']
        branch=request.POST['branch']
        session=request.POST['session']
        subject=request.POST['subject']
        file_name=request.POST['file_name']
        file=request.FILES['file']
        stu=Study()
        stu.course=course
        stu.branch=branch
        stu.session=session
        stu.subject=subject
        stu.file_name=file_name
        stu.file=file
        stu.save()
        return redirect('myapp:adstudy')
    course=Course.objects.all()
    branch=Branch.objects.all()
    session=Session.objects.all()
    return render(request, 'adstudy.html',locals())

def editstudy(request, id):
    if request.method=="POST":
        course=request.POST['course']
        branch=request.POST['branch']
        session=request.POST['session']
        subject=request.POST['subject']
        file_name=request.POST['file_name']
        study = Study.objects.get(id=id)
        study.course=course
        study.branch=branch
        study.session=session
        study.subject=subject
        study.file_name = file_name
        try:
            if (request.FILES['file']):
                study.file=request.FILES['files']
        except:
            pass
        study.save()
        return redirect('myapp:viewstudy')
    st =Study.objects.get(id=id)
    course = Course.objects.all()
    branch = Branch.objects.all()
    session = Session.objects.all()
    return render(request,'adstudy.html',locals())

def deletestudy(request,id):
    Study.objects.filter(id=id).delete()
    return redirect('myapp:viewstudy')


def adstu(request):
    stu = Student.objects.all()
    return render(request, 'adstu.html',locals())



