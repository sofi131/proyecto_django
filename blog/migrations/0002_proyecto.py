# Generated by Django 3.2.25 on 2024-04-10 15:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Proyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('descripcion', models.TextField()),
                ('imagen', models.ImageField(upload_to='proyectos/')),
                ('enlace', models.URLField()),
            ],
        ),
    ]
