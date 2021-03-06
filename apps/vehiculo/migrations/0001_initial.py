# Generated by Django 2.2.3 on 2019-08-01 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Asign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('start_hour', models.TimeField()),
                ('end_hour', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Parqueo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parking_spot', models.CharField(choices=[('A', 'A'), ('B', 'B'), ('C', 'C'), ('D', 'D'), ('E', 'E'), ('F', 'F'), ('G', 'G'), ('H', 'H'), ('I', 'I'), ('J', 'J')], max_length=4)),
            ],
        ),
        migrations.CreateModel(
            name='Vehiculo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Vehicle_type', models.TextField(max_length=20)),
                ('plate', models.CharField(max_length=10)),
                ('spot', models.ManyToManyField(through='vehiculo.Asign', to='vehiculo.Parqueo')),
            ],
        ),
        migrations.AddField(
            model_name='asign',
            name='spot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.Parqueo'),
        ),
        migrations.AddField(
            model_name='asign',
            name='vehicle',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='vehiculo.Vehiculo'),
        ),
    ]
