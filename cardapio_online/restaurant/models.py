from django.db import models

# Create your models here.

class Menu(models.Model):
    user = models.ForeignKey('accounts.Usuario', verbose_name='Usuário', related_name='menus', on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length=70)
    description = models.TextField('Descrição',blank=True)
    attachment =  models.FileField('Anexar Cardápio', null=True, blank=True, upload_to='cardapios/')

    def __str__(self):
        return self.name