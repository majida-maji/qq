# Generated by Django 3.2.16 on 2022-12-29 07:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myschoolapp', '0005_studymaterial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mark',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('s1', models.CharField(max_length=200)),
                ('s2', models.CharField(max_length=200)),
                ('s3', models.CharField(max_length=200)),
                ('s4', models.CharField(max_length=200)),
                ('s5', models.CharField(max_length=200)),
                ('s6', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschoolapp.course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschoolapp.studentlogin')),
            ],
        ),
    ]
