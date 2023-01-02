# Generated by Django 3.2.16 on 2022-12-23 04:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myschoolapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommunityGroup',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('department', models.CharField(max_length=200)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myschoolapp.course')),
            ],
        ),
    ]