from django import forms

class Login_form(forms.Form):
    username = forms.TextInput(attrs={'class':'login_input','placeholder':'username/email','max_length':45})
    password = forms.PasswordInput(attrs={'class':'login_input', 'placeholder':'password','max_length':8})