# Generated by Django 2.1.2 on 2018-10-27 17:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('misperris', '0003_auto_20181027_1404'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='estado',
            field=models.CharField(choices=[('Rescatado', 'Rescatado'), ('2Disponible', 'Disponible'), ('Adoptado', 'Adoptado')], default='Rescatado', help_text='Seleccione estado de la Mascota', max_length=2),
        ),
    ]
