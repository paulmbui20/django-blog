# Generated by Django 5.1.2 on 2024-11-25 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_customuser_bio_customuser_gender_customuser_image_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='website',
            field=models.URLField(blank=True, max_length=65, null=True),
        ),
    ]