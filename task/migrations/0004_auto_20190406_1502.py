# Generated by Django 2.2 on 2019-04-06 12:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_auto_20190406_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='status',
            field=models.CharField(choices=[('a', 'Active'), ('i', 'Inactive')], default='a', max_length=1),
        ),
        migrations.AlterField(
            model_name='user',
            name='created',
            field=models.DateField(auto_now_add=True, verbose_name='Date of created'),
        ),
        migrations.AlterField(
            model_name='user',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='task.Group', verbose_name='Group'),
        ),
    ]
