from django.shortcuts import render,redirect
from django.contrib.auth.hashers import make_password,check_password
from django.views import View
from store.models.customer import Customer
class Signup(View):
    def get(self,request):
        return render(request, 'signup.html')
    def post(self,request):
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        # Validation Part
        value = {
            'first_name': first_name,
            'last_name': last_name,
            'phone': phone,
            'email': email
        }
        customer = Customer(first_name=first_name, last_name=last_name, phone=phone, email=email, password=password)
        # Saving customer
        error_message = self.validateCustomer(customer)
        if not error_message:
            customer.password = make_password(customer.password)
            customer.register()
            return redirect("index")
        else:
            data = {
                'error': error_message,
                'values': value
            }
            return render(request, 'signup.html', data)

    def validateCustomer(self,customer):
        error_message = None
        if not customer.first_name:
            error_message = "First Name Required!"
        elif len(customer.first_name) < 2:
            error_message = "First Name must be 2 character long!"
        elif not customer.last_name:
            error_message = "last Name Required!"
        elif len(customer.last_name) < 2:
            error_message = "Last Name must be 2 character long!"
        elif not customer.phone:
            error_message = "Phone Number Required!"
        elif not customer.phone.isdigit():
            error_message = "Phone Number should only contain Digits!"
        elif len(customer.phone) < 10:
            error_message = "Phone Number must be 10 digits long!"
        elif not customer.email:
            error_message = "Email Required!"
        elif not customer.password:
            error_message = "Password Required!"
        elif len(customer.password) < 6:
            error_message = "Password will be atleast 6 characters long!"
        elif customer.isExist():
            error_message = "Email Address already registered!"
        return error_message