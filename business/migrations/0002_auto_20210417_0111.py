# Generated by Django 3.1.7 on 2021-04-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('business', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dashboard',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('img', models.ImageField(upload_to='images/')),
                ('price', models.IntegerField(default=0)),
                ('dprice', models.IntegerField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]
