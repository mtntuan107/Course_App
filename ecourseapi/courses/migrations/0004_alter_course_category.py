# Generated by Django 5.0.3 on 2024-03-05 08:05

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0003_course_category_alter_category_create_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.category'),
        ),
    ]
