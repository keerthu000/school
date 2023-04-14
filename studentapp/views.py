from django.shortcuts import render,redirect
from studentapp.models import Course
from studentapp.models import Student


# Create your views here.
def home(request):
    return render(request,'home.html')
def addcourse(request):
    return render(request,'add_course.html')
# def addstudent(request):
#     return render(request,'student.html')
def add_course(request):
    if request.method=='POST':
        course_name=request.POST.get('course')
        course_fee=request.POST.get('amount')
        course=Course(course_name=course_name,fee=course_fee)
        course.save()
        return redirect('/')
def add_student(request):
    course=Course.objects.all()
    return render (request,'student.html',{'course':course})

        
def add_studentdb(request):
    if request.method=='POST':
        student_name=request.POST['name']
        student_address=request.POST['address']
        age=request.POST['age']
        jdate=request.POST['date']
        sel=request.POST['sel']
        course1=Course.objects.get(id=sel)
        student=Student(student_name=student_name,student_address=student_address,student_age=age,joining_date=jdate,course=course1)
        student.save()
        return redirect('/')
def show_student(request):
    student=Student.objects.all()
    return render(request,'show_student.html',{'students':student})
def edit(request,pk):
    stu=Student.objects.get(id=pk)
    course=Course.objects.all()
    return render(request,'editstudent.html',{'stud':stu,'course':course})
   
def editpage(request,pk):
    if request.method=='POST':
        student=Student.objects.get(id=pk)
        student.student_name=request.POST.get('name')
        student.student_address=request.POST.get('address')
        student.student_age=request.POST.get('age')
        student.joining_date=request.POST.get('date')
        course=request.POST.get('sel')
        course1=Course.objects.get(id=course)
        student.course=course1
        student.save()
        return redirect('show_student')
    return render(request,'editstudent.html')

def deletepage(request,pk):
    stu=Student.objects.get(id=pk)
    stu.delete()
    return redirect('show_student')
