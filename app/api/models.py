from django.db import models

# Create your models here.
class Books(models.Model):
    codigoISBN  = models.CharField(max_length=20)
    autor = models.CharField(max_length=25)
    titulo = models.CharField(max_length=25)
    editorial = models.CharField(max_length=20)
    year = models.CharField(max_length=4)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
    
    class Meta:
        ordering = ['-created_at']
