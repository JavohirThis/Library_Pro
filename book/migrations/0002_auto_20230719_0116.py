# Generated by Django 3.2.20 on 2023-07-19 01:16

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('author', '0001_initial'),
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookmodel',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='author.authormodel'),
        ),
        migrations.AlterModelTable(
            name='bookcategorymodel',
            table='book_category',
        ),
        migrations.DeleteModel(
            name='AuthorModel',
        ),
    ]
