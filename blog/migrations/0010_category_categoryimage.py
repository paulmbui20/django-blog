# Generated by Django 5.1.2 on 2024-11-24 20:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_category_description_alter_category_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='categoryImage',
            field=models.ImageField(blank=True, null=True, upload_to='category_images/'),
        ),
    ]
