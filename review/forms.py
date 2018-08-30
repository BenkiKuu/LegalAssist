from .models import Profile, Affidavit, LawFirms, DemandLetter
from django import forms



class NewProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        exclude = ['user']
    

class NewAfidavitForm(forms.ModelForm):
    class Meta:
        model = Affidavit
        exclude = ['user', 'doc']

class NewDemandLetterForm(forms.ModelForm):
    class Meta:
        model = DemandLetter
        exclude = ['user', 'doc']


class NewLawFirmForm(forms.ModelForm):
    class Meta:
        model = LawFirms
        exclude = ['user']
