# Generated by Django 5.0.3 on 2024-03-05 07:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('active', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=50)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='courses/%Y/%m/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
