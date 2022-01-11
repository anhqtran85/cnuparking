from django import forms

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User
from main.models import Parking_A, Parking_B, Parking_C1, Parking_C2, Parking_D, Parking_E1, Parking_E2, Parking_E3, \
    Parking_E4, Parking_F, Parking_G, Parking_H, Parking_I, Parking_J, Parking_K, Parking_L, Parking_M


class LoginForm(AuthenticationForm):
    class Meta:
        model = AuthenticationForm
        fields = ["username", "password"]


class ParkingForm(forms.ModelForm):
    class Meta:
        model = Parking_A
        fields = ("parking_spot", "parking_status")
        labels = {'parking spot': "", "parking status": "", }
        widgets = {'parking_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parking_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingBForm(forms.ModelForm):
    class Meta:
        model = Parking_B
        fields = ("parkingb_spot", "parkingb_status")
        labels = {'parkingb spot': "", "parkingb status": "", }
        widgets = {'parkingb_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingb_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingC1Form(forms.ModelForm):
    class Meta:
        model = Parking_C1
        fields = ("parkingc1_spot", "parkingc1_status")
        labels = {'parkingc1 spot': "", "parkingc1 status": "", }
        widgets = {'parkingc1_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingc1_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingC2Form(forms.ModelForm):
    class Meta:
        model = Parking_C2
        fields = ("parkingc2_spot", "parkingc2_status")
        labels = {'parkingc2 spot': "", "parkingc2 status": "", }
        widgets = {'parkingc2_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingc2_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingDForm(forms.ModelForm):
    class Meta:
        model = Parking_D
        fields = ("parkingd_spot", "parkingd_status")
        labels = {'parkingd spot': "", "parkingd status": "", }
        widgets = {'parkingd_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingd_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingE1Form(forms.ModelForm):
    class Meta:
        model = Parking_E1
        fields = ("parkinge1_spot", "parkinge1_status")
        labels = {'parkinge1 spot': "", "parkinge1 status": "", }
        widgets = {'parkinge1_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkinge1_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingE2Form(forms.ModelForm):
    class Meta:
        model = Parking_E2
        fields = ("parkinge2_spot", "parkinge2_status")
        labels = {'parkinge2 spot': "", "parkinge2 status": "", }
        widgets = {'parkinge2_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkinge2_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingE3Form(forms.ModelForm):
    class Meta:
        model = Parking_E3
        fields = ("parkinge3_spot", "parkinge3_status")
        labels = {'parkinge3 spot': "", "parkinge3 status": "", }
        widgets = {'parkinge3_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkinge3_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingE4Form(forms.ModelForm):
    class Meta:
        model = Parking_E4
        fields = ("parkinge4_spot", "parkinge4_status")
        labels = {'parkinge4 spot': "", "parkinge4 status": "", }
        widgets = {'parkinge4_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkinge4_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingFForm(forms.ModelForm):
    class Meta:
        model = Parking_F
        fields = ("parkingf_spot", "parkingf_status")
        labels = {'parkingf spot': "", "parkingf status": "", }
        widgets = {'parkingf_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingf_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingGForm(forms.ModelForm):
    class Meta:
        model = Parking_G
        fields = ("parkingg_spot", "parkingg_status")
        labels = {'parkingg spot': "", "parkingg status": "", }
        widgets = {'parkingg_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingg_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingHForm(forms.ModelForm):
    class Meta:
        model = Parking_H
        fields = ("parkingh_spot", "parkingh_status")
        labels = {'parkingh spot': "", "parkingh status": "", }
        widgets = {'parkingh_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingh_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingIForm(forms.ModelForm):
    class Meta:
        model = Parking_I
        fields = ("parkingi_spot", "parkingi_status")
        labels = {'parkingi spot': "", "parkingi status": "", }
        widgets = {'parkingi_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingi_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingJForm(forms.ModelForm):
    class Meta:
        model = Parking_J
        fields = ("parkingj_spot", "parkingj_status")
        labels = {'parkingj spot': "", "parkingj status": "", }
        widgets = {'parkingj_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingj_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingKForm(forms.ModelForm):
    class Meta:
        model = Parking_K
        fields = ("parkingk_spot", "parkingk_status")
        labels = {'parkingk spot': "", "parkingk status": "", }
        widgets = {'parkingk_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingk_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingLForm(forms.ModelForm):
    class Meta:
        model = Parking_L
        fields = ("parkingl_spot", "parkingl_status")
        labels = {'parkingl spot': "", "parkingl status": "", }
        widgets = {'parkingl_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingl_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class ParkingMForm(forms.ModelForm):
    class Meta:
        model = Parking_M
        fields = ("parkingm_spot", "parkingm_status")
        labels = {'parkingm spot': "", "parkingm status": "", }
        widgets = {'parkingm_spot': forms.TextInput(attrs={'class': 'form-control'}),
                   'parkingm_status': forms.RadioSelect(choices=[(True, "Cancel"), (False, "Parked here")])}


class UserInformation(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']
        widgets = {'username': forms.TextInput(attrs={'class': 'form-control'}),
                   'email': forms.TextInput(attrs={'class': 'form-control'}),
                   }
