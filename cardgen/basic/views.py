from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.contrib import messages
from django.contrib.auth import login, logout,get_user, get_user_model
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth.hashers import make_password, check_password
from .models import NewUserModel
from .pingen import genMtnEpin, genGloEpin, genAirtelEpin, gen9mobileEpin, genref, genAuth
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
import smtplib



# Create your views here.
dict = {}


def home(request) -> HttpResponse:
    current_user = get_user(request)
    try:
        current_user = NewUserModel.objects.get(username=current_user.username)
    except:
        error = True
    else:
        error = False
    return render(request, 'index.html', {'current_user': current_user, 'error': error})




@login_required
def verifyAuth(request) -> HttpResponse:
    current_user = get_user(request)
    current_user = NewUserModel.objects.get(username=current_user.username)
    if request.method == 'POST':
        code = int(request.POST.get('auth'))
        if current_user.authkey != code:
            return JsonResponse({'status': 'error', 'msg': 'You Have Entered an Invalid Authorization Key. Please Contact the Admin and Try Again'})
        else:
            current_user.is_verified = True
            current_user.save()
            messages.success(request, 'Your application has been verified successfully. Enjoy')
            return JsonResponse({'status': 'success'})
        
            
    return render(request, 'auth.html', {'current_user': current_user})

@login_required
def buidEpin(request):
    current_user = get_user(request)
    current_user = NewUserModel.objects.get(username=current_user.username)
    if current_user.is_verified == False:
        messages.error(request, 'Oops. You have\'nt verified your account yet. Please Enter a Valid Auth Key to Continue.')
        return redirect('basicapp:verifyauth')
    else:
        if request.method == 'POST':
            global dict
            if request.POST.get('network') == 'mtn':
                compiled_data = genMtnEpin(msg=str(request.POST.get('pin')), amount=int(request.POST.get('amount')))
                ref = genref()
                dict = {
                    'value': f'{request.POST.get("pin")}',
                    'amount': int(request.POST.get("amount")),
                    'network': f'{request.POST.get("network")}',
                    'list': compiled_data,
                    'ref': ref,
                    'exist': 'true'
                }
                
                return redirect('basicapp:print', epin='true')
            elif request.POST.get('network') == 'glo':
                compiled_data = genGloEpin(msg=str(request.POST.get('pin')), amount=int(request.POST.get('amount')))
                ref = genref()
                
                dict = {
                    'value': f'{request.POST.get("pin")}',
                    'amount': int(request.POST.get("amount")),
                    'network': f'{request.POST.get("network")}',
                    'list': compiled_data,
                    'ref': ref,
                    'exist': 'true'
                }
                
                return redirect('basicapp:print', epin='true')
                
            elif request.POST.get('network') == 'airtel':
                compiled_data = genAirtelEpin(msg=request.POST.get('pin'), amount=request.POST.get('amount'))
                ref = genref()
                dict = {
                    'value': f'{request.POST.get("pin")}',
                    'amount': int(request.POST.get("amount")),
                    'network': f'{request.POST.get("network")}',
                    'list': compiled_data,
                    'ref': ref,
                    'exist': 'true'
                }
                
                return redirect('basicapp:print', epin='true')
                
            elif request.POST.get('network') == '9mobile':
                compiled_data = gen9mobileEpin(msg=request.POST.get('pin'), amount=request.POST.get('amount'))
                ref = genref()
                
                dict = {
                    'value': f'{request.POST.get("pin")}',
                    'amount': int(request.POST.get("amount")),
                    'network': f'{request.POST.get("network")}',
                    'list': compiled_data,
                    'ref': ref,
                    'exist': 'true'
                }
                
                return redirect('basicapp:print', epin='true')
                
            else:
                messages.error(request, 'Sorry an Error has occured. Please recheck the data you provided.')
                return redirect('basicapp:buildepin')
        

    return render(request, 'build.html', {'current_user': current_user})

@login_required
def changePassword(request):
    current_user = get_user(request)
    current_user = NewUserModel.objects.get(username=current_user.username)
    if not current_user.is_verified:
        messages.error(request, 'Oops. You haven\'t verified your account yet. Please Enter a Valid Auth Key to Continue.')
        return redirect('basicapp:verifyauth')
    else:
        if request.method == 'POST':
            oldpwd = str(request.POST.get('oldpwd'))
            if check_password(oldpwd, current_user.password):
                newpwd = str(request.POST.get('pword'))
                current_user.password = make_password(newpwd)
                current_user.save()
                messages.success(request, 'Your Password has Been Changed Successfuly. Please Login.')
                logout(request)
                return JsonResponse({'status': 'success'},)
            else:
                return JsonResponse({'status': 'error', 'msg': 'Incorrect Password. Please Try Again.'})
        return render(request, 'change.html', {'current_user': current_user})
    




@login_required
def formatCard(request):
    current_user = get_user(request)
    current_user = NewUserModel.objects.get(username=current_user.username)
    if not current_user.is_verified:
        messages.error(request, 'Oops. You haven\'t verified your account yet. Please Enter a Valid Auth Key to Continue.')
        return redirect('basicapp:verifyauth')
    else:
        return render(request, 'format.html', {'current_user': current_user})

@login_required
def printCard(request, epin):
    current_user = get_user(request)
    current_user = NewUserModel.objects.get(username=current_user.username)
    if not current_user.is_verified:
        messages.error(request, 'Oops. You haven\'t verified your account yet. Please Enter a Valid Auth Key to Continue.')
        return redirect('basicapp:verifyauth')
    else:
        global dict
        if epin == 'true':
            messages.success(request, 'Epin has been pasted automatically. Click on the "Print button" to print your recharge cards')
            # return render(request, 'print.html', {'dict': dict})
            return render(request, 'format.html', {'dict': dict, 'current_user': current_user})
        else:
            if request.method == 'POST':
                return render(request, 'format.html', {'dict': dict, 'current_user': current_user})
            else:
                return render(request, 'print.html', {'current_user': current_user})

            

def signUp(request):
    if request.method == 'POST':
        newuser = NewUserModel()
        authkey = genAuth()
        newuser.businessname = str(request.POST.get('businessName')).title()
        username = str(request.POST.get('username'))
        newuser.username = username.lower()
        newuser.password = make_password(str(request.POST.get('pword')))
        newuser.authkey = authkey
        
        try:
            newuser.save()
        except:
            messages.error(request,f'{username.title()} already exists. Please Login Instead.') 
            return JsonResponse({'status': 'exist'})
        else:
            try:
                with smtplib.SMTP_SSL("smtp.gmail.com") as connection:
                    connection.login(user=settings.GMAIL, password=settings.GMAIL_PASSWORD)
                    connection.sendmail(from_addr=settings.GMAIL, to_addrs=settings.GMAIL, msg="Subject:New User"
                                                                            f"\n\nUsername: {username.title()}\nAuthKey: {authkey}")
            except:
                return JsonResponse({'status': 'error', 'msg': 'Something Went Wrong. Please Try Again.'})
            else:
                login(request,newuser)
                messages.success(request, message=f'Welcome \'{username.title()} \'. Please type your Valid Auth Key to Unlock the app.')
                return JsonResponse({'status': 'success'})

        
            

        
    return render(request, 'profile.html')

def signIn(request):
    if request.method == 'POST':
        username = str(request.POST.get('username'))
        password = str(request.POST.get('pword'))
        try:
            user = NewUserModel.objects.get(username=username.lower())
        except:
            messages.error(request, message=f'Sorry {username.title()} does not exit. Please register and try again')
            return JsonResponse({'status': 'register'})
        else:
            if check_password(password, user.password):
                login(request, user)
                messages.success(request, message=f'Successfully signed in as {username.title()}')
                return JsonResponse({'status': 'success'})
            else:
                return JsonResponse({'status': 'error', 'msg': 'Incorrect password. Please try again'})
    
    return render(request, 'signin.html')

def signOut(request):
    logout(request)
    return redirect('basicapp:index')