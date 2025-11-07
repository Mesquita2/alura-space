from django import forms 

class LoginForms(forms.Form):
    nome_login=forms.CharField(
        label = "Nome do usuário",
        max_length=100, 
        required=True
    )
    
    senha = forms.CharField(
        label = "Senha ...",
        max_length= 70, 
        required= True,
        widget=forms.PasswordInput()
    ) 