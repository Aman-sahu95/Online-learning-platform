from django.shortcuts import render,redirect
from .models import Student, Login ,Admin
from myapp.models import Course, Branch, Session
import datetime
from django.conf import settings
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from .models import Enquiry


# Create your views here.

def home(request):
    return render(request,'home.html')
def about(request):
    return render(request,'about.html')

def logout(request):
    request.session.flush()
    return redirect('mainapp:home')

def registration(request):
    if request.method=="POST":
        name = request.POST['name']
        fname = request.POST['fname']
        mname = request.POST['mname']
        number = request.POST['number']
        email = request.POST['email']
        password = request.POST['password']
        gender = request.POST['gen']
        course = request.POST['course']
        branch = request.POST['branch']
        session = request.POST['session']
        address = request.POST['address']
        pic = request.FILES['pic']
        stu = Student()
        stu.name=name
        stu.fname=fname
        stu.mname=mname
        stu.number=number
        stu.email=email
        stu.gender=gender
        stu.course=course
        stu.branch=branch
        stu.session=session
        stu.address=address
        stu.pic=pic
        lo = Login.objects.create(email=email,password=password)
        stu.save()
        # Send Email After Successful Registration
        context = {
            'name': name,
            'email': email,
            'password': password,
            'year': datetime.datetime.now().year
        }
        html_content = render_to_string('email.html', context)
        subject = "Welcome to Biotech Park OLP"
        from_email = settings.EMAIL_HOST_USER
        to = [email]

        msg = EmailMultiAlternatives(subject, '', from_email, to)
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return redirect('mainapp:login')
    course=Course.objects.all()
    branch=Branch.objects.all()
    session=Session.objects.all()
    return render(request,'reg.html',locals())

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        lo = Login.objects.get(email=email)
        if (lo and lo.password == password):
            student = Student.objects.get(email=email)
            request.session['student'] = student.id
            return redirect('studentapp:stuhome')
        else:
            return redirect('mainapp:login')
    return render(request,'login.html')

def adlogin(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']
        ad = Admin.objects.get(email=email)
        if (ad and ad.password == password):
            return redirect('myapp:adhome')
        else:
            return redirect('mainapp:adlogin')
    return render(request,'adlogin.html')

def org(request):
    return render(request,'org.html')

def cert(request):
    return render(request,'cert.html')

def outreach(request):
    return render(request,'outreach.html')

def service(request):
    return render(request,'service.html')

def training(request):
    return render(request,'training.html')

def enquiry(request):
     if request.method=="POST":
        name = request.POST['name']
        email = request.POST['email']
        number = request.POST['number']
        message = request.POST['message']
        enq = Enquiry()
        enq.name=name
        enq.number=number
        enq.email=email
        enq.message=message
        enq.save()
        context = {
            "name": name,
            "email": email,
            "number": number,
            "message": message,
        }
        html_content = render_to_string('email.html', context)
        return redirect('mainapp:enquiry')
     return render(request,'enquiry.html',locals())

def viewenquiry(request):
    et = Enquiry.objects.all() 
    return render(request,'viewenquiry.html',locals())

def ceo(request):
    return render(request,'ceo.html')
def error(request):
    return render(request,'error.html')
