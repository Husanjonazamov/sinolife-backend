# Generated by Django 5.1.3 on 2025-07-31 19:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='lang',
            field=models.CharField(choices=[('uz', 'Uzbek'), ('en', 'English'), ('ru', 'Russian')], default='uz', verbose_name='Lang'),
        ),
        migrations.AddField(
            model_name='user',
            name='tg_id',
            field=models.BigIntegerField(blank=True, null=True),
        ),
    ]
