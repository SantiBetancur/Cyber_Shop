from django import forms
from Clients.models import ClientInfo,clientPhones,Corporation,Person

class ClientForm(forms.ModelForm):
    class Meta:
        model = ClientInfo
        fields = "__all__"

class CorporationForm(forms.ModelForm):
    class Meta:
        model = Corporation
        fields = "__all__"

class PersonForm(forms.ModelForm):
    class Meta:
        model = Person
        fields = "__all__"

class PhonesForm(forms.ModelForm):
    class Meta:
        model = clientPhones
        fields = "__all__"
