# Generated by Django 2.2.3 on 2019-08-01 17:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('vehiculo', '0001_initial'),
        ('cliente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('status', models.CharField(choices=[('Adentro', 'Adentro'), ('Afuera', 'Afuera')], default='re', max_length=4)),
                ('total', models.DecimalField(blank=True, decimal_places=2, max_digits=6, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.PositiveIntegerField(default=1)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='factura.Order')),
                ('vehiculo', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='vehiculo.Vehiculo')),
            ],
        ),
        migrations.AddField(
            model_name='order',
            name='vehiculo',
            field=models.ManyToManyField(through='factura.OrderDetail', to='vehiculo.Vehiculo'),
        ),
        migrations.CreateModel(
            name='Invoice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('invoice_number', models.CharField(max_length=12)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('payment', models.CharField(choices=[('efe', 'efectivo'), ('tar', 'tarjeta'), ('cu', 'cupon')], max_length=2)),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='cliente.Customer')),
                ('order', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='factura.Order')),
            ],
        ),
    ]
