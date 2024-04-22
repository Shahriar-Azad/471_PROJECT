from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse
from .models import *
from django.contrib.auth import login,logout,authenticate
from django.http import HttpResponse
# from openpyxl import Workbook
# from google.oauth2 import service_account
# import googleapiclient.discovery
#from .models import Product
from django.utils.datastructures import MultiValueDictKeyError
from datetime import datetime, timedelta
from django.utils import timezone
# Create your views here.
def index(request):
    return render(request, 'index.html')

temp_list = []
username1=None
def register(request):
    error = ""
    if request.method == "POST":
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        gender = request.POST['gender']
        password = request.POST['password']
        try:
            user = User.objects.create_user(first_name=firstname, last_name=lastname, username=email,password=password)
            TutorDetail.objects.create(user=user, gender = gender)
            error="no"
        except:
            error="yes"

    return render(request, 'register.html',locals())



def t_login(request):
    global username1
    error = ""
    if request.method == "POST":
        email = request.POST['email']
        username1=email
        password = request.POST['password']
        user = authenticate(username=email, password=password)
        if user:
            login(request, user)
            error="no"
        else:
            error="yes"
    return render(request, 't_login.html',locals())


def t_home(request):
    temp=None
    var=tutorreg2.objects.all()
    if request.method=="POST":
        try:
            #print("tempvjdnvdjvnjvnkovnkvnkvn")
            temp=request.POST["submit_button"]
            #print("tempvjdnvdjvnjvnkovnkvnkvn")
            if temp!=None:
                print(temp)
                val2=tutorreg.objects.filter(name=temp)
                print(val2[0].name,"check5")
                return render(request, "edurecors.html",{'data2':val2[0]})
            else:
                return render(request, 't_home.html',{'data':var})  

        except:
            return render(request, 't_home.html',{'data':var})    



        
    return render(request, 't_home.html',{'data':var})


# def visa(request):
#     return render(request, 'visa.html')


def bkash(request):
    return render(request, "bkash.html")

def nagad(request):
    return render(request, "nagad.html")


def contact(request):
    return render(request, "contact.html")

def  tutor_reg(request):
    error = ""
    if request.method == "POST":
        Name = request.POST['Name']
        NID = request.POST['NID']
        address = request.POST['address']
        SSCDiv = request.POST['S.S.C_div']
        SSCyr = request.POST['S.S.C_yr']
        SSCres = request.POST['S.S.C_res']
        SSCname = request.POST['S.S.C_name']
        HSCDiv = request.POST['H.S.C_div']
        HSCyr = request.POST['H.S.C_yr']
        HSCres = request.POST['H.S.C_res']
        HSCname = request.POST['H.S.C_name']
        grad_sub = request.POST['grad_sub']
        grad_yr = request.POST['grad_yr']
        grad_cg = request.POST['grad_cg']
        grad_name = request.POST['grad_name']


        try:
            #user = User.objects.create_user(name=Name, NID=NID, Address=address,SSCDiv=SSCDiv,SSCyr=SSCyr,SSCres=SSCres,SSCinst=SSCname,HSCDiv=HSCDiv,HSCyr=HSCyr,HSCres=HSCres,HSCinst=HSCname,UNDRsub=grad_sub,UNDRyr=grad_yr,UNDRres=grad_cg,UNDRinst=grad_name)
            a=tutorreg.objects.create(name=Name, NID=NID, Address=address,SSCDiv=SSCDiv,SSCyr=SSCyr,SSCres=SSCres,SSCinst=SSCname,HSCDiv=HSCDiv,HSCyr=HSCyr,HSCres=HSCres,HSCinst=HSCname,UNDRsub=grad_sub,UNDRyr=grad_yr,UNDRres=grad_cg,UNDRinst=grad_name)
            a.save()
            error="no"
        except:
            error="yes"

    return render(request, 'tutor_reg.html')

def tutor_reg2(request):
    error = ""
    if request.method == "POST":
        Name = request.POST['Name']
        NID = request.POST['NID']
        try:
            primary=request.POST['primary']
        except MultiValueDictKeyError:
            primary=False

        try:
            junior_secondary=request.POST['junior_secondary']
        except MultiValueDictKeyError:
            junior_secondary=False
        
        try:
            secondary=request.POST['secondary']
        except MultiValueDictKeyError:
            secondary=False

        try:
            hsc=request.POST['hsc']
        except MultiValueDictKeyError:
            hsc=False
        
        try:
            undergrade=request.POST['undergrade']
        except MultiValueDictKeyError:
            undergrade=False
        
        try:
             postgrade=request.POST['postgrade']
        except MultiValueDictKeyError:
            postgrade=False
        
        
       
        area=request.POST['Area']
        experiance=request.POST['experiance']
        image=request.POST['image']
        
        mobile=request.POST['mobile']
                         
        try:
            b=tutorreg2.objects.create(name=Name, NID=NID,primary=primary,junior_secondary=junior_secondary,secondary=secondary,hsc=hsc,undergrade=undergrade,postgrade=postgrade,area=area,experiance=experiance,image=image,mobile=mobile)
            b.save()
            C=Data.objects.create(name=Name,location=area,phone=mobile)
            C.save()
            error="no"
        except:
            error="yes"

    return render(request, 'tutor_reg2.html',locals())

def addtutor1(request):
    error = ""
    if request.method == "POST":
        stdname = request.POST['stdname']
        tcrname = request.POST['tcrname']
        mobile = request.POST['mobile']
        startDate = request.POST['startDate']
        #count = request.POST['count']
        payment1 = request.POST['payment1']
        area=request.POST['area']


        try:
            
            new=addtutor.objects.create(stdname=stdname, tcrname=tcrname, mobile=mobile,satrtDate=startDate,payment=payment1,area=area)
            new.save()
            error="no"
        except:
            error="yes"
    print(error)
    return render(request, 'addtutor.html',locals())
    
# from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'shahriar.azad123@gmail.com',
#     ['tasnimneha42@gmail.com'],
#     fail_silently=False,
# )

# def export_to_excel(request):
#     # Fetch all products from the Product model
#     products = Product.objects.all()

#     # Create a new workbook
#     wb = Workbook()
#     ws = wb.active

#     # Write headers
#     ws.append(['Name', 'Price', 'Description'])

#     # Write data rows
#     for product in products:
#         ws.append([product.name, product.price, product.description])

#     # Save the workbook
#     response = HttpResponse(content_type='application/ms-excel')
#     response['Content-Disposition'] = 'attachment; filename="products.xlsx"'
#     wb.save(response)

#     return response

def video(request):
    obj = Item.objects.all()
    return render(request,'video.html',{'obj':obj})


def available(request):
    if 'q' in request.GET:
        q = request.GET['q']
        data = Data.objects.filter(location__icontains=q)
    else:

        data = Data.objects.all()
    context = {
        'data':data

    }
    return render(request, "available.html",context)





def profile(request):
    global username1
   # tutor=tutor.object.get(email=username)
    store=None
    user1=User.objects.filter(username=username1)
    #print(user1.first_name)
    print(len(user1))
    temp_new=None
    temp_ag=None
    if request.method == "POST":
       # print(temp_new,"uhfgefttttttttttttttttttttttttttttttttttttttttt")
        try:
            temp_new = request.POST['submit_button']
            
            print(temp_new,"djdbjbnfgjkfgnv")
            val=personaltutor.objects.filter(stdname=temp_new)
            
            val.update(attendence=val[0].attendence+1)
            #return render(request,"profile.html",{'data':user1,'data2':tutor,'addtutor':addtr,'tutornext':tutornext})

        except MultiValueDictKeyError:
            temp_new=None
        try:
            temp_ag = request.POST['reset']
            
            print(temp_new,"djdbjbnfgjkfgnv")
            val=personaltutor.objects.filter(stdname=temp_ag)
            val.update(attendence=0)
            #return render(request,"profile.html",{'data':user1,'data2':tutor,'addtutor':addtr,'tutornext':tutornext})


        except MultiValueDictKeyError:
            temp_ag=None
        


    for i in user1:
        store=i
        
    tutor=TutorDetail.objects.filter(user=store)
    for j in tutor:
        print(j.contact)

    addtr=personaltutor.objects.filter(stdname=store)  
    
    tutornext=personaltutor.objects.filter(tchrname=store)
    for i in tutornext:
        ##print(payment1,pay[0].payment,"pppppaaaaayyymmmmeeeennnnttt")
        a=i.Starting_Date
        b=(i.Starting_Date+ timedelta(days=30))
        c=timezone.now().date()
        if c>b:
            tutornext.update(Status='Due')
            tutornext.update(Starting_Date=b)
            #print(a,b,c)

    

    return render(request,"profile.html",{'data':user1,'data2':tutor,'addtutor':addtr,'tutornext':tutornext})

def notification(request):
    global temp_list
    app=None
    rej=None
    temp=[]
    store=True
    if request.method == "POST":
        try:
            app = request.POST['submit_button']
        except MultiValueDictKeyError:
            app=None
        
        print(app,"apppppppfdfegggggggfgrfgpppppppppppppppppppppppppppppp")
        
        try:
            rej = request.POST['reject_button']
        except MultiValueDictKeyError:
            rej=None
        print(rej)

    if app!=None:
        
        vlo=notification1.objects.filter(stdemail=app)
        teacher=vlo[0].tchrname
        
        vlo2=addtutor.objects.filter(tcrname=teacher).filter(stdname=app)
        for i in  temp_list:
            if i[0]==app and i[1]==teacher:
                store=False
        if len(vlo2)>0:
            print(vlo2[0],"hobee")
            if store==True:
                bad=personaltutor.objects.create(stdname=app,tchrname=teacher,Starting_Date=vlo2[0].satrtDate,payment=vlo2[0].payment)
                bad.save()
                temp.append(app)
                temp.append(teacher)
                temp_list.append(temp)
            # delt1=addtutor.objects.filter(stdname=app)
            # #print(rej,teacher,delt,"rej")
            # delt1.delete()

            # delt=notification1.objects.filter(stdemail=app)
            # print(rej,teacher,delt,"rej")
            # delt.delete()
            app=None

    if rej!=None:
        
        vlo=notification1.objects.filter(stdemail=rej)
        teacher=vlo[0].tchrname
        
        delt1=addtutor.objects.filter(stdname=rej)
        #print(rej,teacher,delt,"rej")
        delt1.delete()

        delt=notification1.objects.filter(stdemail=rej)
        print(rej,teacher,delt,"rej")
        delt.delete()
        delt3=personaltutor.objects.filter(stdname=rej)
        print(rej,teacher,delt,"rej")
        delt3.delete()
        rej=None
    #    # print(rej,teacher,delt,"rej")
    if rej==None and app==None:   
        global username1
        store2=None
        
        print(username1)
        addtut=addtutor.objects.filter(tcrname=username1)
        print((addtut))#teachername
        if len(addtut)!=0:
            count=0
            for i in addtut:  #i.stdname=student name
                count+=1
                print(count)
                tcr=i.tcrname
                std_email=i.stdname
                #print(temp1,"xcghgjhjhhghv")
                user2=User.objects.filter(username=i.stdname)
                first_name=user2[0].first_name
                second=user2[0].last_name
                temp=user2[0].username
                tutor2=TutorDetail.objects.filter(user=user2[0])

                contact=tutor2[0].contact
                wantjoin=i.satrtDate
                wantpay=i.payment
                area=i.area
                if count>0:
                    print(tcr,first_name,second,std_email,contact,area,wantjoin,wantpay,area,"dfhsagadbgjiadbvsdhnvbguyagfsui0ovbhzdhifgvbsaijhji")

                check=notification1.objects.filter(stdemail=std_email)
                print(check,std_email)
                if len(check)==0:
                    print(len(check),std_email)
                    new3=notification1.objects.create(tchrname=tcr,stdname=first_name, stdname_last=second,stdemail=std_email,contact=contact,Area=area,tcrname=tcr,date=wantjoin,pay=wantpay)
                    new3.save()
                    print(new3,"new3")
                    error="no"
                    
                else:
                    continue
            data=notification1.objects.all()
            print(data[0].stdemail,"data")
            return render(request,"notification.html",{'data':data})        
        else:
            return render(request,"nonotification.html")#def nonotification(request):
    # global username1
    # store2=None
    # #print(username1)
    # addtut=addtutor.objects.filter(tcrname=username1)
    
    return render(request,'notification.html')












def payment(request):
    global username1
    print("something")
    error = ""
    if request.method == "POST":
        
        tcrname = request.POST['tcrname']
        mobile = request.POST['mobile']
        stdname= request.POST['std']
        #count = request.POST['count']
        payment1 = request.POST['payment1']
        
        #print(payment1,pay[0].payment,"pppppaaaaayyymmmmeeeennnnttt")

        
        new2=Payment.objects.create(tcrname=tcrname, mobile=mobile,stdname=stdname,payment=payment1)
        pay=personaltutor.objects.filter(stdname=stdname,tchrname=tcrname)
        
        print(payment1,pay[0].payment,"pppppaaaaayyymmmmeeeennnnttt")
        if len(pay)>0:
           
            if int(payment1)-int(pay[0].payment)>=0:
                new2.save()
                print("jpppppppppppppppppppppppppppppppppppppp")
                pay.update(Status='Paid')
               
                
                
                return render(request, 'visa.html')
        else:
            return render(request, 'visa.html')
        
        
        
        
        
        
        
        
        #print(pay[0].payment,'hdfwsfbwejofgbvwaufgvwaifjwjofgbwauifgwa0ofwaiprfhwqjif')
            
            
        
        

        



    return render(request, 'visa.html')#,{'pay':pay})

    
    


        
def home(request):
    return render(request, 'home.html')

def room(request, room):
    username = request.GET.get('username')
    room_details = Room.objects.get(name=room)
    return render(request, 'room.html', {
        'username': username,
        'room': room,
        'room_details': room_details
    })

def checkview(request):
    room = request.POST['room_name']
    username = request.POST['username']

    if Room.objects.filter(name=room).exists():
        return redirect('/'+room+'/?username='+username)
    else:
        new_room = Room.objects.create(name=room)
        new_room.save()
        return redirect('/'+room+'/?username='+username)

def send(request):
    message = request.POST['message']
    username = request.POST['username']
    room_id = request.POST['room_id']

    new_message = Message.objects.create(value=message, user=username, room=room_id)
    new_message.save()
    return HttpResponse('Message sent successfully')

def getMessages(request, room):
    room_details = Room.objects.get(name=room)

    messages = Message.objects.filter(room=room_details.id)
    return JsonResponse({"messages":list(messages.values())})




    
def edurecors(request):
    print(temp,"hello")
    temp=request.POST["submit_button"]
    print(temp,"temppppppppppppppppppppppppppppppppppppppppppppp")
    val=tutorreg.objects.filter(name=temp)
    return render(request, "edurecors.html",{'data2':val})


def ratings(request):
    return render(request, 'ratings.html')