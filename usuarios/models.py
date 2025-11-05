from django.db import models

def senha_hash(senha):
    import hashlib
    return hashlib.sha256(senha.encode()).hexdigest()

# Create your models here.
class Usuario(models.Model):
    nome = models.CharField(max_length=100),
    email = models.EmailField(unique=True),
    senha = models.CharField(max_length=100),
    
    
    def __str__ (self):
        return self.email
    