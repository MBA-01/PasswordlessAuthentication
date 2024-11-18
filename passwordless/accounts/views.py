# from django.shortcuts import render
# from django.http import HttpResponseRedirect
# from django.http import HttpRequest
# from django.contrib.auth.forms import UserCreationForm
# from django.urls import reverse_lazy
# from django.views import generic
# from .forms import RegistrationForm, PasswordlessLoginForm, PasswordfullLoginForm

# class SignUpView(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy("login")
#     template_name = "registration/signup.html"

# def RegistrationView(request):
#       context ={}
#       context['form']= RegistrationForm()
#       return render(request, "registration2.html", context)

# def PasswordfulLoginView(request):
#      context ={}
#      context['form']= PasswordfullLoginForm()
#      return render(request, "passwordfullogin.html", context)

# def PasswordlessLoginView(request):
#     context ={}
#     context['form']= PasswordlessLoginForm()
#     return render(request, "passwordlesslogin.html", context)

from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from django.http import HttpRequest
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from .forms import RegistrationForm, PasswordlessLoginForm, PasswordfulLoginForm
from .models import Encrypted_Data
from django.contrib.auth import logout,authenticate, login
import uuid
from django.db import IntegrityError, transaction
import datetime
import logging
import time
logger = logging.getLogger('accounts')

class SignUpView(generic.CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/signup.html"

class RegistrationView(generic.CreateView):
    form_class = RegistrationForm
    success_url = reverse_lazy("login")
    template_name = 'registration2.html'
    
    def form_valid(self, form):
        form.instance.MACAddress = self.request.POST.get('MACAddress')
        form.instance.DeviceType = self.request.POST.get('DeviceType')

        # Attempt to create the Encrypted_Data object with a unique USERCODE
        max_attempts = 10  # Increase the number of attempts
        delay = 0.1  # Delay in seconds between attempts
        for attempt in range(max_attempts):
            usercode = self.generate_unique_usercode()
            try:
                with transaction.atomic():
                    encrypted_data = Encrypted_Data.objects.create(
                        USERCODE=usercode,
                        First_Name=form.cleaned_data['First_Name'],
                        Last_Name=form.cleaned_data['Last_Name'],
                        Address=form.cleaned_data['Address'],
                        Phone=form.cleaned_data['Phone'],
                        National_Identity_Code=form.cleaned_data['National_Identity_Code'],
                        BirthDate=form.cleaned_data['BirthDate'],
                        Country=form.cleaned_data['Country'],
                        City=form.cleaned_data['City'],
                        Zip_Code=form.cleaned_data['Zip_Code']
                    )
                    form.instance.USERCODE = usercode
                    print(f"Created Encrypted_Data: {encrypted_data}")
                    logger.debug(f"Created Encrypted_Data: {encrypted_data}")
                    return super().form_valid(form)
            except IntegrityError as e:
                logger.error(f"Attempt {attempt + 1}/{max_attempts} - IntegrityError: {e}")
                time.sleep(delay)  # Introduce a small delay before retrying
                if attempt == max_attempts - 1:
                    form.add_error(None, 'Could not generate a unique USERCODE. Please try again later.')
                    return self.form_invalid(form)
        return self.form_invalid(form)

    def generate_unique_usercode(self):
        return str(uuid.uuid4().hex[:8])  # Shorten UUID to 8 characters



    # def form_valid(self, form):
    #     form.instance.MACAddress = self.request.POST.get('MACAddress')
    #     form.instance.DeviceType = self.request.POST.get('DeviceType')

        
    #     usercode = self.generate_unique_usercode()
    #     form.instance.USERCODE = usercode
   
        
    #     try:
        
    #         with transaction.atomic():
    #             encrypted_data = Encrypted_Data.objects.create(
    #                 USERCODE=usercode,
    #                 First_Name=form.cleaned_data['First_Name'],
    #                 Last_Name=form.cleaned_data['Last_Name'],
    #                 Address=form.cleaned_data['Address'],
    #                 Phone=form.cleaned_data['Phone'],
    #                 National_Identity_Code=form.cleaned_data['National_Identity_Code'],
    #                 BirthDate=form.cleaned_data['BirthDate'],
    #                 Country=form.cleaned_data['Country'],
    #                 City=form.cleaned_data['City'],
    #                 Zip_Code=form.cleaned_data['Zip_Code']
    #             )
                
    #             print(f"Created Encrypted_Data: {encrypted_data}")
    #             logger.debug(f"Created Encrypted_Data: {encrypted_data}")
    #     except IntegrityError as e:
            
    #         print(f"IntegrityError: {e}")
    #         logger.error(f"IntegrityError: {e}")
    #         form.add_error(None, 'A user with this USERCODE already exists. Please try again.')
    #         return self.form_invalid(form)
    #     return super().form_valid(form)


    # def generate_unique_usercode(self):

    #     max_retries = 5
    #     for _ in range(max_retries):
    #         usercode = str(uuid.uuid4().hex[:8])  # Shorten UUID to 8 characters
    #         if not Encrypted_Data.objects.filter(USERCODE=usercode).exists():
    #             return usercode
    #     raise ValueError('Unable to generate a unique USERCODE after multiple attempts')

class PasswordfulLoginView(generic.CreateView):
    form_class = PasswordfulLoginForm
    success_url = reverse_lazy("home")
    template_name = "passwordfullogin.html"

    def form_valid(self, form):
        # Set Inscription_Year to the current year if not provided
        form.instance.Inscription_Year = form.instance.Inscription_Year or datetime.date.today().year
        email=form.cleaned_data['Email']
        password=form.cleaned_data['Password']
        logger.debug("Form valid method called with email: %s", email)
        print(f"Attempting to authenticate user with email: {email}")

        user = authenticate(self.request,email=email, password = password)
        if user is not None:
            logger.debug("Authentication successful for user: %s", user)
            print(f"Authentication successful for user: {email}")
            login(self.request, user)
            return super().form_valid(form)
        else:
            logger.debug("Authentication failed for email: %s", email)
            print(f"Authentication failed for user: {email}")
            form.add_error(None, 'Invalid login credentials')
            return self.form_invalid(form)



class PasswordlessLoginView(generic.CreateView):
    form_class = PasswordlessLoginForm
    success_url = reverse_lazy("home")
    template_name = "passwordlesslogin.html"

    

def logout_view(request):
    logout(request)
    return redirect('home')