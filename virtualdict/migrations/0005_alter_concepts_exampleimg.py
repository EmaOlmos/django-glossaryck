# Generated by Django 4.2.5 on 2023-09-16 06:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('virtualdict', '0004_alter_concepts_exampleimg'),
    ]

    operations = [
        migrations.AlterField(
            model_name='concepts',
            name='exampleImg',
            field=models.ImageField(blank=True, null=True, upload_to='virtualdict/files/examples'),
        ),
    ]
