# Generated by Django 5.1.3 on 2025-07-22 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0015_alter_bannermodel_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('phone', models.CharField(max_length=200, verbose_name='Telefon')),
                ('address', models.TextField(verbose_name='Manzil')),
                ('telegram', models.URLField(help_text='Misol: https://t.me/username', verbose_name='Telegram')),
            ],
            options={
                'verbose_name': 'ContactModel',
                'verbose_name_plural': 'ContactModels',
                'db_table': 'contact',
            },
        ),
        migrations.CreateModel(
            name='MessagesModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('first_anme', models.CharField(max_length=255, verbose_name='Ism')),
                ('phone', models.CharField(max_length=200, verbose_name='Telefon')),
                ('message', models.TextField(max_length=200, verbose_name='Xabar')),
            ],
            options={
                'verbose_name': 'MessagesModel',
                'verbose_name_plural': 'MessagesModels',
                'db_table': 'messages',
            },
        ),
    ]
