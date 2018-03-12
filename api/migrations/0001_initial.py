# Generated by Django 2.0.3 on 2018-03-10 15:49

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('address_id', models.AutoField(primary_key=True, serialize=False)),
                ('state', models.CharField(choices=[('AC', 'Acre'), ('AL', 'Alagoas'), ('AP', 'Amapá'), ('AM', 'Amazonas'), ('BA', 'Bahia'), ('CE', 'Ceará'), ('DF', 'Distrito Federal'), ('ES', 'Espírito Santo'), ('GO', 'Goiás'), ('MA', 'Maranhão'), ('MT', 'Mato Grosso'), ('MS', 'Mato Grosso do Sul'), ('MG', 'Minas Gerais'), ('PA', 'Pará'), ('PB', 'Paraíba'), ('PR', 'Paraná'), ('PE', 'Pernambuco'), ('PI', 'Piauí'), ('RJ', 'Rio de Janeiro'), ('RN', 'Rio Grande do Norte'), ('RS', 'Rio Grande do Sul'), ('RO', 'Rondônia'), ('RR', 'Roraima'), ('SC', 'Santa Catarina'), ('SP', 'São Paulo'), ('SE', 'Sergipe'), ('TO', 'Tocantins')], max_length=2)),
                ('city', models.CharField(max_length=80)),
                ('number', models.IntegerField()),
                ('complement', models.CharField(max_length=40, null=True)),
                ('invoice', models.BooleanField()),
                ('delivery', models.BooleanField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-address_id'],
                'db_table': 'address',
            },
        ),
        migrations.CreateModel(
            name='App',
            fields=[
                ('app_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_id', models.IntegerField(choices=[(1, 'root'), (2, 'director'), (3, 'client')], db_index=True)),
                ('apikey', models.CharField(max_length=40, unique=True)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('describe', models.TextField()),
                ('active', models.BooleanField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'app',
            },
        ),
        migrations.CreateModel(
            name='Delivery',
            fields=[
                ('delivery_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=80, unique=True)),
                ('description', models.TextField(null=True)),
                ('rate', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.IntegerField(choices=[(1, 'Ativo'), (2, 'Inativo')])),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-delivery_id'],
                'db_table': 'delivery',
            },
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('order_id', models.AutoField(primary_key=True, serialize=False)),
                ('status', models.IntegerField(choices=[(1, 'Aberto'), (2, 'Cancelado'), (3, 'Aguardando pagamento'), (4, 'Pagamento recusado'), (5, 'Pago'), (6, 'Despachado'), (7, 'Entregue'), (8, 'Estornado'), (9, 'Devolvido')])),
                ('coupon', models.CharField(max_length=30)),
                ('date_expired', models.DateTimeField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Address')),
            ],
            options={
                'db_table': 'order',
            },
        ),
        migrations.CreateModel(
            name='OrderProduct',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.IntegerField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Order')),
            ],
            options={
                'db_table': 'order_product',
            },
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('person_id', models.AutoField(primary_key=True, serialize=False)),
                ('profile_id', models.IntegerField(choices=[(1, 'root'), (2, 'director'), (3, 'client')], db_index=True)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('cpf', models.CharField(max_length=11, null=True, unique=True)),
                ('cnpj', models.CharField(max_length=14, null=True, unique=True)),
                ('email', models.EmailField(max_length=150, unique=True)),
                ('phone1', models.CharField(max_length=15)),
                ('phone2', models.CharField(max_length=15, null=True)),
                ('username', models.CharField(max_length=150, unique=True, validators=[django.core.validators.MinLengthValidator(6, message='Min 6 caracteres')])),
                ('password', models.CharField(db_index=True, max_length=8, validators=[django.core.validators.MinLengthValidator(8, message='Min 8 caracteres')])),
                ('verified', models.BooleanField()),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-person_id'],
                'db_table': 'person',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('product_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=150, unique=True)),
                ('description', models.TextField()),
                ('code', models.CharField(max_length=150, unique=True)),
                ('compound', models.NullBooleanField()),
                ('unit_weight', models.IntegerField(choices=[(1, 'kg (Kilograma)'), (2, 'L (Litros)'), (3, 'Kb (Kilobytes)')])),
                ('weight', models.FloatField(null=True)),
                ('width', models.FloatField(null=True)),
                ('length', models.FloatField(null=True)),
                ('height', models.FloatField(null=True)),
                ('origin', models.IntegerField(choices=[(1, 'Própria'), (2, 'Terceirizado'), (3, 'Importado')])),
                ('gtin', models.CharField(db_index=True, max_length=150, null=True)),
                ('quantity', models.IntegerField()),
                ('published', models.BooleanField(db_index=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'ordering': ['-product_id'],
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='Token',
            fields=[
                ('token_id', models.AutoField(primary_key=True, serialize=False)),
                ('token', models.CharField(max_length=40, unique=True)),
                ('ip', models.GenericIPAddressField(db_index=True)),
                ('date_expire', models.DateTimeField(db_index=True, null=True)),
                ('date_create', models.DateTimeField(auto_now_add=True)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.App')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Person')),
            ],
            options={
                'db_table': 'token',
            },
        ),
        migrations.AddField(
            model_name='orderproduct',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Product'),
        ),
        migrations.AddField(
            model_name='order',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Person'),
        ),
        migrations.AddField(
            model_name='address',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.Person'),
        ),
        migrations.AlterUniqueTogether(
            name='orderproduct',
            unique_together={('order', 'product')},
        ),
    ]
