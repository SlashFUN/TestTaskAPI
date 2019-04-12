from django.db import models
from django.urls import reverse
# Create your models here.


class User(models.Model):

    USER_STATUS = (
        ('Active', 'Active'),
        ('Inactive', 'Inactive'),
    )

    username = models.CharField('Nickname', unique=True, max_length=100)
    email = models.EmailField('E-mail', unique=True, default='', error_messages={'invalid': 'example@mail.com'})
    created = models.DateField('Date of created', auto_now_add=True)
    group = models.ForeignKey('Group', verbose_name='Group', null=True, blank=True, on_delete=models.PROTECT)
    status = models.CharField(max_length=10, choices=USER_STATUS, default='Active')

    def __str__(self):
        return self.username
    # def get_absolute_url(self):
    #     return reverse('user_detail', args=[str(self.id)])


class Group(models.Model):
    name = models.TextField('Name', help_text='Enter groupname:')
    description = models.TextField('Description', help_text='Enter description: ', null=True, blank=True)
    editing = models.BooleanField(default=False)
    creating = models.BooleanField(default=False)
    deleting = models.BooleanField(default=False)

    def __str__(self):
        return  self.name
    # def get_absolute_url(self):
    #     return reverse('group_detail', args=[str(self.id)])
