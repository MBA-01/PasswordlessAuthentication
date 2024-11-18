
# from django import forms
# class RegistrationForm(forms.Form):

#     First_Name=forms.CharField(max_length=128, help_text = "Enter firstname")
#     Last_Name=forms.CharField(max_length=128, help_text = "Enter lastname")
#     Email=forms.CharField(max_length=128, help_text = "Enter email")
#     Password=forms.CharField(widget = forms.PasswordInput())
#     RetypePassword=forms.CharField(widget = forms.PasswordInput())
#     Address=forms.CharField(max_length=128)
#     Phone=forms.CharField(max_length=128, help_text = "Enter phone number")
#     National_Identity_Code=forms.CharField(max_length=128)
#     BirthDate=forms.CharField(max_length=128)
#     Country=forms.CharField(max_length=128)
#     City=forms.CharField(max_length=128)
#     Zip_Code=forms.CharField(max_length=128)
#     MACAddress=forms.CharField(widget=forms.HiddenInput())
#     DeviceType=forms.CharField(widget=forms.HiddenInput())

# class PasswordlessLoginForm(forms.Form):
#       Email=forms.EmailField(max_length=128, help_text = "Enter Email", label="Email")
#       MACAddress=forms.CharField(widget=forms.HiddenInput())

# class PasswordfullLoginForm(forms.Form):
#       Email=forms.EmailField(max_length=128, help_text = "Enter firstname", label="Email")
#       Password=forms.PasswordInputField(max_length=128, help_text = "Enter password", label="Password")


from django import forms
from .models import  Students, Encrypted_Data

COUNTRY_CHOICES =(
    ("1", "UK"),
    ("2", "Morocco"),
    ("3", "USA"),
    ("4", "South Korea"),
    ("5", "Germany"),
)
class RegistrationForm(forms.ModelForm):
 #class Meta:
   # model=Encrypted_Data
    First_Name=forms.CharField(max_length=128)
    Last_Name=forms.CharField(max_length=128)
    Email=forms.CharField(max_length=128)

    Address=forms.CharField(max_length=128, widget = forms.TextInput() )
    Phone=forms.CharField(max_length=128)
    National_Identity_Code=forms.CharField(max_length=128)
    BirthDate=forms.DateField(widget=forms.DateInput(format="%Y-%m-%d", attrs={"type": "date"}), input_formats=["%Y-%m-%d"])
    Country=forms.ChoiceField(choices = COUNTRY_CHOICES)
    City=forms.CharField(max_length=128)
    Zip_Code=forms.CharField(max_length=128)
    MACAddress=forms.CharField(widget=forms.HiddenInput())
    DeviceType=forms.CharField(widget=forms.HiddenInput())
    Password=forms.CharField(widget = forms.PasswordInput())
    RetypePassword=forms.CharField(widget = forms.PasswordInput())
    class Meta:
          model=Encrypted_Data
          fields=['First_Name', 'Last_Name', 'Email', 'Password', 'Address', 'Phone', 'National_Identity_Code', 'BirthDate', 'Country', 'City', 'Zip_Code' ]

class PasswordlessLoginForm(forms.ModelForm):
      Email=forms.EmailField(max_length=128, label="Email")
      PC_MAC_Address=forms.CharField(widget=forms.HiddenInput())
      class Meta:
          model=Students
          fields=['Email', 'PC_MAC_Address']

class PasswordfulLoginForm(forms.ModelForm):
      Email=forms.EmailField(max_length=128, label="Email")
      Password=forms.CharField(label="Password", widget=forms.PasswordInput())
      class Meta:
          model=Students
          fields=['Email', 'Password']
