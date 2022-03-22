# Generated by Django 3.1.6 on 2022-02-22 09:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('slug', models.SlugField()),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_delivery', models.CharField(max_length=55, unique=True)),
                ('date_delivery', models.DateField()),
                ('slug', models.SlugField()),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Employees',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, unique=True)),
                ('lastname', models.CharField(max_length=45, unique=True)),
                ('slug', models.SlugField()),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='LineDelivery',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_delivery', models.IntegerField()),
                ('price_delivery', models.IntegerField()),
                ('observation_delivery', models.CharField(max_length=50)),
                ('used', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.delivery')),
            ],
        ),
        migrations.CreateModel(
            name='LineOutput',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_output', models.IntegerField()),
                ('observation_output', models.CharField(max_length=50)),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('line_delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.linedelivery')),
            ],
        ),
        migrations.CreateModel(
            name='Measure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40, unique=True)),
                ('slug', models.SlugField()),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=80, unique=True)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('threshold', models.IntegerField()),
                ('slug', models.SlugField()),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('category', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.category')),
            ],
        ),
        migrations.CreateModel(
            name='Provider',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, unique=True)),
                ('description', models.CharField(max_length=255)),
                ('tel', models.CharField(max_length=30)),
                ('address', models.CharField(max_length=50)),
                ('slug', models.SlugField()),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=45, unique=True)),
                ('slug', models.SlugField()),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='StockMovement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_movement', models.DateField()),
                ('quantity', models.IntegerField()),
                ('type', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('line_delivery', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.linedelivery')),
                ('line_output', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.lineoutput')),
                ('measure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.measure')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.product')),
            ],
        ),
        migrations.CreateModel(
            name='Output',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_output', models.CharField(max_length=60, unique=True)),
                ('date_output', models.DateField()),
                ('slug', models.SlugField()),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.employees')),
            ],
        ),
        migrations.CreateModel(
            name='Ordered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_ordered', models.CharField(max_length=50, unique=True)),
                ('date_ordered', models.DateField()),
                ('slug', models.SlugField()),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('employee', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.employees')),
            ],
        ),
        migrations.AddField(
            model_name='lineoutput',
            name='measure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.measure'),
        ),
        migrations.AddField(
            model_name='lineoutput',
            name='output',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.output'),
        ),
        migrations.AddField(
            model_name='lineoutput',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.product'),
        ),
        migrations.CreateModel(
            name='LineOrdered',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity_ordered', models.IntegerField()),
                ('observation_ordered', models.CharField(max_length=50)),
                ('livery', models.BooleanField(default=False)),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('measure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.measure')),
                ('ordered', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.ordered')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.product')),
            ],
        ),
        migrations.AddField(
            model_name='linedelivery',
            name='line_ordered',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.lineordered'),
        ),
        migrations.AddField(
            model_name='linedelivery',
            name='measure',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.measure'),
        ),
        migrations.AddField(
            model_name='linedelivery',
            name='product',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.product'),
        ),
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('reference_inventory', models.CharField(max_length=50, unique=True)),
                ('date_inventory', models.DateField()),
                ('quantity_inventory', models.IntegerField()),
                ('slug', models.SlugField()),
                ('deleted', models.BooleanField(default=False)),
                ('date_modified', models.DateTimeField(auto_now=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('measure', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.measure')),
                ('product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.product')),
            ],
        ),
        migrations.AddField(
            model_name='employees',
            name='service',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.service'),
        ),
        migrations.AddField(
            model_name='delivery',
            name='provider',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='stock_bureau.provider'),
        ),
    ]