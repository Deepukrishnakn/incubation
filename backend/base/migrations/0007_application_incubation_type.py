# Generated by Django 4.0.6 on 2022-07-28 06:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0006_alter_slotbooking_company'),
    ]

    operations = [
        migrations.AddField(
            model_name='application',
            name='incubation_type',
            field=models.CharField(choices=[('Physicalincubation', 'Physicalincubation'), ('Virtualincubation', 'Virtualincubation')], default='Physicalincubation', max_length=300, null=True),
        ),
    ]
