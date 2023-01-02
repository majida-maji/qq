# Generated by Django 3.2.16 on 2022-12-30 04:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myschoolapp', '0006_mark'),
    ]

    operations = [
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('date', models.DateField(auto_now=True)),
                ('subject', models.CharField(max_length=200)),
                ('note', models.FileField(upload_to='studymaterial')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschoolapp.course')),
            ],
        ),
    ]
