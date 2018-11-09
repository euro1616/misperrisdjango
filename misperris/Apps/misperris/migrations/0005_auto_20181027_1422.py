# Generated by Django 2.1.2 on 2018-10-27 17:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0004_auto_20181027_1420'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.CharField(choices=[('Rescatado', 'Rescatado'), ('Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], default='Rescatado', help_text='Seleccione estado de la Mascota', max_length=10),
        ),
    ]