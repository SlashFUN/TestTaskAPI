# Generated by Django 2.2 on 2019-04-06 15:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0010_auto_20190406_1724'),
    ]

    operations = [
        migrations.CreateModel(
            name='PaginatorElements',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('element_amount', models.IntegerField(choices=[('10', 10), ('15', 15), ('20', 20)], default='10')),
            ],
        ),
        migrations.AlterField(
            model_name='group',
            name='create',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='group',
            name='delete',
            field=models.BooleanField(default=False),
        ),
    ]
