from django.views import View
from django.shortcuts import render,redirect,HttpResponseRedirect
from django.contrib.auth.hashers import check_password
from store.models.customer import Customer

class Login(View):
    returnUrl = None
    def get(self,request):
        Login.returnUrl = request.GET.get('returnUrl')
        return render(request, 'login.html')
    def post(self,request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        customer = Customer.get_customer_by_email(email)
        error_message = None
        if customer:
            flag = check_password(password, customer.password)
            if flag:
                request.session['customer'] = customer.id
                #request.session['email'] = customer.email
                if Login.returnUrl:
                    return HttpResponseRedirect(Login.returnUrl)
                else:
                    Login.returnUrl = None
                    return redirect('index')
            else:
                error_message = "Incorrect Email or Password!"
                return render(request, 'login.html', {'error': error_message})
        else:
            error_message = "Incorrect Email or Password!"
            return render(request, 'login.html', {'error': error_message})


def logout(request):
    request.session.clear()
    return redirect('login')