from django.db import models
from django.urls import reverse

# Create your models here.
class Customer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    birth_date = models.DateField()
    area_code = models.CharField(max_length=3)
    phone_number = models.CharField(max_length=9)
    country = models.CharField(max_length=30) 
    state = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    create_date = models.DateTimeField(auto_now_add=True) #Registra a data de criação do objeto no banco de dados    
    update_date = models.DateTimeField(auto_now=True) #Registra a data da alteração na tabela no banco de dados    
    active = models.BooleanField(default=True) #desativa o cliente sem deletar todo o histórico de informações do cliente.

    def __str__(self):
        return f"First Name: {self.first_name} - Last Name: {self.last_name}"

    def get_absolute_url(self):
        return reverse('customer:customer-update', kwargs={'id': self.id})

    def get_delete_url(self):
        return reverse('customer:customer-delete', kwargs={'id': self.id})

    class Meta:
        db_table = 'customer'
