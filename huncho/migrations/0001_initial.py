# Generated by Django 2.2 on 2019-05-07 06:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('age', models.IntegerField()),
                ('nationality', models.CharField(max_length=40)),
                ('primary', models.CharField(max_length=40)),
                ('secondary', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('occupation', models.CharField(max_length=40)),
                ('slogan', models.CharField(max_length=50)),
                ('residence', models.CharField(max_length=40)),
                ('photo', models.ImageField(upload_to='')),
                ('campus', models.CharField(max_length=40)),
                ('course', models.CharField(max_length=40)),
                ('hobby', models.CharField(max_length=40)),
                ('is_male', models.BooleanField(default=True)),
            ],
        ),
    ]
