# Generated by Django 4.1.3 on 2023-04-29 05:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book_details', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='book',
            old_name='publisher',
            new_name='publisher_name',
        ),
        migrations.AddField(
            model_name='book',
            name='page_no',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='book',
            name='publisher_age',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='book',
            name='publication_date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='book',
            name='serial_number',
            field=models.AutoField(default=0, primary_key=True, serialize=False),
        ),
    ]