# Generated by Django 4.1.3 on 2022-12-01 04:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('srkapp', '0006_remove_resume_spec'),
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=50)),
                ('blog', models.CharField(default='', max_length=50)),
                ('date', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
