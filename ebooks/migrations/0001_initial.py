# Generated by Django 3.0.2 on 2020-01-30 21:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AbooMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=100)),
                ('imgUrl', models.CharField(max_length=100)),
                ('fileUrl', models.CharField(max_length=100)),
            ],
        ),
    ]
