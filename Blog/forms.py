from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4, required=True, label="Username", help_text="Your username please", widget=forms.TextInput(attrs={'class':"input"}))
    password = forms.CharField(required=True, label="Password", widget=forms.PasswordInput( attrs={"class":'input'}))
    pass

class SignupForm(forms.Form):
    username = forms.CharField(max_length=100, min_length=4, required=True, label="Username", help_text="Your username please", widget=forms.TextInput(attrs={'class':"input"}))
    password = forms.CharField(required=True, label="Password", help_text="Please enter your password", widget=forms.PasswordInput(attrs={"class":"input"}))
    fullname = forms.CharField(max_length=100, min_length=4, required=True, label="FullName", help_text="Your Fullname please", widget=forms.TextInput(attrs={"class":"input"}))
    pass
