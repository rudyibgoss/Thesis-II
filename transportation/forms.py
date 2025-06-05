#imports for form handling
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import *
from django import forms
from django.db.models import Q

#user registration form
class MyUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['fname','lname','username', 'email', 'password1', 'password2'] #fields to be included in the form
        widgets = {
            'fname':forms.TextInput(attrs={'class':'form-control'}),
            'lname':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
        }

#form to update user profile data
class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['avatar','fname','lname','Contact','Address']
        widgets = {
            'avatar':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'fname': forms.TextInput(attrs={'class': 'form-control'}),
            'lname': forms.TextInput(attrs={'class': 'form-control'}),
            'Contact': forms.NumberInput(attrs={'class': 'form-control','min':'1'}),
            'Address': forms.TextInput(attrs={'class': 'form-control'}),
}
        
#form for Shop owners to register or update shop info
class ShopForm(ModelForm):
    class Meta:
        model = Shops
        fields = ['validids','banner','logo','shop_name','tin','brn','contact','email','address','shop_description','latitude', 'longitude']
        widgets = {
            'validids':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'banner':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'logo':forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'shop_name': forms.TextInput(attrs={'class': 'form-control'}),
            'tin': forms.TextInput(attrs={'class': 'form-control'}),
            'brn': forms.TextInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control','min':'1'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'shop_description': forms.Textarea(attrs={'class': 'form-control'}),
            'latitude': forms.HiddenInput(),
            'longitude': forms.HiddenInput(),
            
}
        
#form for vehicle registration or update
class VehicleForm(ModelForm):
    class Meta:
        model = Vehicle
        fields = ['documents','img1','img2','img3','img4','img5', 'categories', 'transmission', 'seat','fuels', 'color_description', 'model_car', 'plate', 'chasis_number', 'vin_no', 'vehicle_type','rent_per_hr']
        widgets = {
            'documents': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img1': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img2': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img3': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img4': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'img5': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'categories': forms.Select(attrs={'class': 'form-control'}),
            'transmission': forms.Select(attrs={'class': 'form-control'}),
            'seat': forms.Select(attrs={'class': 'form-control'}),
            'fuels': forms.Select(attrs={'class': 'form-control'}),
            'color_description': forms.TextInput(attrs={'class': 'form-control'}),
            'model_car': forms.TextInput(attrs={'class': 'form-control'}),
            'plate': forms.TextInput(attrs={'class': 'form-control'}),
            'chasis_number': forms.TextInput(attrs={'class': 'form-control'}),
            'vin_no': forms.TextInput(attrs={'class': 'form-control'}),
            'vehicle_type': forms.Select(attrs={'class': 'form-control'}),
            'rent_per_hr': forms.NumberInput(attrs={'class': 'form-control','min':'350'}),
        }

#form for assigning a driver to a shop
class DriverForm(ModelForm):
    class Meta:
        model = driver_shop
        fields = ['drivers_license','phone_number','drivers_rate']
        widgets = {
            'drivers_license': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'phone_number': forms.NumberInput(attrs={'class': 'form-control','min':'1'}),
            'drivers_rate': forms.NumberInput(attrs={'class': 'form-control','min':'50', 'max':'1000'}),
}

#form for creating a rental record
class Rented_CarsForm(ModelForm):
    class Meta:
        model = Rented_Cars
        fields = ['renter_validid','driver_shp', 'pick_up_unit', 'return_unit','payment_choice']
        widgets = {
            'renter_validid': forms.ClearableFileInput(attrs={'class': 'form-control'}),
            'driver_shp': forms.Select(attrs={'class': 'form-control'}),
            'payment_choice': forms.Select(attrs={'class': 'form-control'}),
            'pick_up_unit': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
            'return_unit': forms.DateTimeInput(attrs={'class': 'form-control', 'type': 'datetime-local'}),
        }
        input_formats = {
            'pick_up_unit': ['%Y-%m-%dT%H:%M'], 
            'return_unit': ['%Y-%m-%dT%H:%M'],   
        }

    def __init__(self, *args, **kwargs):
        super(Rented_CarsForm, self).__init__(*args, **kwargs)
        # Filter driver_shop to exclude those with status = 2
        #self.fields['driver_shp'].queryset = driver_shop.objects.exclude(Q(status=2)|Q(status=0))
        self.fields['driver_shp'].queryset = driver_shop.objects.filter(status=1)
        self.fields['driver_shp'].required = False  # Make driver_shp optional

#form for onsite payments made by users
class onsite_pay(ModelForm):
    class Meta:
        model = onsitepayment
        fields = ['first_name','last_name','email','contact','proof_resibo']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'contact': forms.NumberInput(attrs={'class': 'form-control','min':'1'}),
            'proof_resibo': forms.ClearableFileInput(attrs={'class': 'form-control'}),
}
        
#form to set hourly or other rental rates
class rates_form(ModelForm):
    class Meta:
        model = rates
        fields = ['rates']
        widgets = {
            'rates': forms.NumberInput(attrs={'class': 'form-control','min':'1', 'max':'15'}),
}

#form for submitting rating and review after rental
class ratings_review_form(ModelForm):
    class Meta:
        model = Rented_Cars
        fields = ['rating_star','rating_reviews']
        widgets = {
            'rating_star': forms.Select(attrs={'class': 'form-control','min':'1', 'max':'5'}),
            'rating_reviews': forms.Textarea(attrs={'class': 'form-control'}),
}

#form to report rental-related issues
class rent_issue_form(ModelForm):
    class Meta:
        model = rent_issue
        fields = ['issue_name','issue_details','issue_amount']
        widgets = {
            'issue_name': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_details': forms.Textarea(attrs={'class': 'form-control'}),
            'issue_amount': forms.NumberInput(attrs={'class': 'form-control'}),
}

