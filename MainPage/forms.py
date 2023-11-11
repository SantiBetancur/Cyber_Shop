from django import forms

class Login_form(forms.Form):
    
    username = forms.CharField(label="",widget=forms.TextInput(attrs={'placeholder':'Enter username/email','autocomplete':'new-username'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Enter password','autocomplete':'new-password'}))

class Register_form(forms.Form):
    
    username = forms.CharField(label="", widget=forms.TextInput(attrs={'placeholder':'New usename','autocomplete':'new-username'}))
    email = forms.CharField(label="",    widget=forms.TextInput(attrs={'placeholder':'New email','autocomplete':'new-email'}))
    password = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'New password','autocomplete':'new-password'}))
    password_confirmation = forms.CharField(label="", widget=forms.PasswordInput(attrs={'placeholder':'Password confirmation','autocomplete':'new-password'}))
        
