from django.shortcuts import render
from django.http import HttpResponse
from . models import *
from django.shortcuts import render_to_response

# Create your views here.
def fn_home(request):
    try:
        return render(request,'home.html')
    except:
        return HttpResponse("error occured")

def fn_login(request):
    try:
        if request.method == 'POST':
            username   = request.POST['email']
            password   = request.POST['password']
            login_obj  = Login.objects.get(email=username)
            request.session['user_id'] = login_obj.id
            if login_obj.password == password:
                if login_obj.role == 'doctor':
                    doctor_obj = Doctor.objects.get(fk_login__id=login_obj.id)
                    return render(request,"doctorsuccess.html",{'doctor_obj':doctor_obj})
                departments = Department.objects.all()
                patient_obj = Patient.objects.get(fk_login__id=login_obj.id)
                return render(request,"usersuccess.html",{'depts': departments, 'patient_obj': patient_obj})
        return render(request,'userlogin.html')
    except Exception as e:
        print(e)
        return HttpResponse("login failed")

def fn_load(request):
    return render(request,'userlogin.html')
def fn_patient(request):
    patient_obj = Patient.objects.all()
    return render(request,'patient.html',{'patient_list':patient_obj})
def fn_doctor(request):
    doctor_obj = Doctor.objects.all()
    return render(request,'doctor.html',{'doctor_list':doctor_obj})


def fn_editpat(request):
    
    if request.method == 'POST':
        Patient.objects.get(id=request.POST['id']).delete()
        return HttpResponse('deleted succesfully')
    patient_id = request.GET['id']
    patient_obj = Patient.objects.get(id=patient_id)
    return render(request,'patientprofile.html',  {'patient': patient_obj})

def fn_adminlog(request):
    return render(request,'admin.html')
def fn_ureglog(request):
    return render(request,'userregister.html')

def fn_dreglog(request):
    departments = Department.objects.all()
    return render(request,'doctorregister.html', {'depts': departments})

def fn_about(request):
    return render(request,'about.html')
def fn_add(request):
    return render(request,'addept.html')

def fn_adddep(request):
    return render(request,'adddep.html')

def fn_homes(request):
    
    login_obj=Login.objects.get(id=request.session['user_id'])
    departments = Department.objects.all()
    patient_obj = Patient.objects.get(fk_login__id=login_obj.id)
    return render(request,"usersuccess.html",{'depts': departments, 'patient_obj': patient_obj})

def fn_dochome(request):
    
    login_obj=Login.objects.get(id=request.session['user_id'])
    departments = Department.objects.all()
    doctor_obj = Doctor.objects.get(fk_login__id=login_obj.id)
    return render(request,"doctorsuccess.html",{'depts': departments, 'doctor_obj': doctor_obj})

def fn_editdoctor(request):
    doctor_id = request.GET['id']
    doctor_obj = Doctor.objects.filter(id=doctor_id)
    return render(request,'editdoctor.html',{'docts':doctor_obj})


def fn_editdep(request):
    departments = Department.objects.all()
    if request.method == 'POST':
        Department.objects.get(id=request.POST['dept_id']).delete()
        return HttpResponse('1')
    return render(request,'editdep.html',  {'depts': departments})

def fn_depadd(request):
    department=request.POST['adddept']
    
    dept_obj=Department(departmentname=department)
    dept_obj.save()
    if dept_obj.id > 0:
        return HttpResponse('added succesfully')
    return HttpResponse('error occured')

def fn_change(request):
    return render(request,'changepassword.html')

def fn_changes(request):
    return render(request,'changepasswords.html')


    

def fn_passwordchange(request): 
    login_obj=Login.objects.get(id=request.session['user_id'])
    password=request.POST['npassword']
    cpassword=request.POST['cpassword']
    if password==cpassword:
        Login.objects.filter(id=login_obj.id).update(password=password)
        return render(request,'passwordchanged.html')
    else:
        return HttpResponse("passwords not matching")   

def fn_edituser(request):
    login_obj=Login.objects.get(id=request.session['user_id'])
    patient_obj = Patient.objects.get(fk_login__id=login_obj.id)
    return render(request,'edituserprofile.html',{'patient_obj':patient_obj})

def fn_saveuser(request):
    login_obj=Login.objects.get(id=request.session['user_id'])
    if request.method=='POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        mobile=request.POST['mobile']  
        Patient.objects.filter(fk_login__id=login_obj.id).update(firstname=firstname,lastname=lastname,mobilenumber=mobile)
        patient_obj = Patient.objects.get(fk_login__id=login_obj.id)
        return render(request,'detailsuser.html',{'patient_obj':patient_obj})
def fn_editdoc(request):
    login_obj=Login.objects.get(id=request.session['user_id'])
    doctor_obj = Doctor.objects.get(fk_login__id=login_obj.id)
    department_obj=Department.objects.all()
    return render(request,'editdoctor.html',{'doctor_obj':doctor_obj,'department_obj':department_obj})
def fn_savedoctor(request):
    login_obj=Login.objects.get(id=request.session['user_id'])
    if request.method == 'POST':
        firstname=request.POST['firstname']
        lastname=request.POST['lastname']
        mobile=request.POST['mobile']
        city=request.POST['city']
        department=request.POST['department']
        optiming=request.POST['optiming'] 
        opaddress=request.POST['opaddress']
        fee=request.POST['fee']
        dept_obj = Department.objects.get(id=department)
        Doctor.objects.filter(fk_login__id=login_obj.id).update(firstname=firstname,lastname=lastname,mobilenumber=mobile,city=city,department=dept_obj,optiming=optiming,opaddress=opaddress,fee=fee)
        doctor_obj = Doctor.objects.get(fk_login__id=login_obj.id)
        if request.FILES:
             image=request.FILES['userimage']
             doctor_obj.image = image
             doctor_obj.save()
        return render(request,'detailsdoc.html',{'doctor_obj':doctor_obj})
    return HttpResponse("failed to save")


def fn_userregister(request):
    try:
        if request.method=='POST':
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            mobile=request.POST['mobile']
            email=request.POST['email']
            password=request.POST['password']
            check_exist=Login.objects.filter(email=email).exists()
            if not check_exist:
                login_obj=Login(email=email,password=password,role="patient")
                login_obj.save()
                if login_obj.id >0:
                    register_obj   = Patient(firstname=firstname,lastname=lastname,mobilenumber=mobile,fk_login=login_obj) 
                    register_obj.save()
                    if register_obj.id>0:
                        return HttpResponse("registered successfully")
                return HttpResponse('success')
            return HttpResponse('account already exist')
        return render(request,'userregister.html')
        
    except Exception as e :
        print(e)
        return HttpResponse("an error occured")
    except:
        return HttpResponse('error occured')


def fn_doctorregister(request):
    try:
        if request.FILES and request.POST:
            firstname=request.POST['firstname']
            lastname=request.POST['lastname']
            mobile=request.POST['mobile']
            email=request.POST['email']
            password=request.POST['password']
            city=request.POST['city']
            department = request.POST['department']
            optiming=request.POST['optime']
            opaddress=request.POST['opaddress']
            location=request.POST['location']
            fee=request.POST['fee']
            image=request.FILES['userimage']
            check_exist=Login.objects.filter(email=email).exists()
            if not check_exist:
                login_obj=Login(email=email,password=password,role="doctor")
                login_obj.save()
                if login_obj.id > 0:
                    dept_obj = Department.objects.get(id=department)
                    register_obj = Doctor(firstname=firstname,lastname=lastname,mobilenumber=mobile,city=city,department=dept_obj,optiming=optiming,opaddress=opaddress,fee=fee,location=location,image=image,fk_login=login_obj) 
                    register_obj.save()
                    if register_obj.id>0:
                        return HttpResponse("registered successfully")
                return HttpResponse('success')
            return HttpResponse('account already exist')
        return render(request,'userregister.html')
        
    except Exception as e :
        print(e)
        return HttpResponse("an error occured")
    except:
        return HttpResponse('error occured')

def fn_admin(request):
    try:
        email=request.POST['email']
        password=request.POST['password']
        if email=='admin@gmail.com' and password=='admin123':
            return render(request,'adminhome.html')
        return httpResponse('username or password incorrect')

    except:
        return HttpResponse('error occured')

def fn_doctprofile(request):
    doctor_id = request.GET['id']
    doctor_obj = Doctor.objects.get(id=doctor_id)
    return render(request,'doctorprofile.html', {'doctor': doctor_obj})


def fn_listdoc(request):
    city = request.POST['city']
    department = request.POST['department']
    doctor_obj = Doctor.objects.filter(city=city, department=department)
    return render(request,'doctorlist.html',{'doctor_list': doctor_obj})
def fn_adminhome(request):
    return render(request,'adminhome.html')




def fn_loadbkng(request):
    doctor_id = request.GET['id']
    doctor_obj = Doctor.objects.get(id=doctor_id)
    if request.method == 'POST':
        patient_id = request.session['user_id']
        patient_obj=Patient.objects.get(fk_login__id=patient_id)
        booking_time = request.POST['time']
        booking_date = request.POST['date']
        booking_obj=Booking.objects.filter(date=booking_date,time=booking_time,doctor_id=doctor_id).exists()
        if not booking_obj:
            book_obj=Booking(date=booking_date,time=booking_time,doctor_id=doctor_obj,patient_id=patient_obj)
            book_obj.save()
            return HttpResponse('booking done succesfully')
        return HttpResponse('slot is not available select another slot')      
    return render(request,'booking.html', {'doctor': doctor_obj})


def fn_mybooking(request):
    patient_id = request.session['user_id']
    booking_obj=Booking.objects.filter(patient_id__fk_login__id=patient_id)
    print(booking_obj)
    return render(request,'mybookings.html',{'booking':booking_obj})

def fn_myappoinments(request):
    doctor_id = request.session['user_id']
    print(doctor_id)
    appoinment_obj=Booking.objects.filter(doctor_id__fk_login__id=doctor_id)
    print(appoinment_obj)
    return render(request,'myappoinments.html',{'appoinments':appoinment_obj})




def fn_doctprofilelist(request):
    if request.method == 'POST':
        Doctor.objects.get(id=request.POST['id']).delete()
        return HttpResponse('deleted succesfully')
    doctor_id = request.GET['id']
    doctor_obj = Doctor.objects.get(id=doctor_id)
    return render(request,'doctorprofilelist.html', {'doctor': doctor_obj})   




