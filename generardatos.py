import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta
import random

fake = Faker('es_CL')
Faker.seed(42)
random.seed(42)
np.random.seed(42)

print("Generando datos para Store Chile...")

# ============== 1. DATASET DE VENTAS ==============
print("Generando ventas...")
ventas = []
productos = [
    ('Laptop Dell XPS', 899000), ('iPhone 14', 799000), ('Samsung Galaxy S23', 699000),
    ('iPad Pro', 649000), ('MacBook Air', 1199000), ('AirPods Pro', 199000),
    ('Monitor Samsung 27"', 249000), ('Teclado Mecánico', 89000), ('Mouse Gaming', 49000),
    ('Disco SSD 1TB', 129000), ('Memoria RAM 16GB', 79000), ('Webcam HD', 59000),
    ('Audífonos Sony', 149000), ('Smartwatch', 299000), ('Tablet Samsung', 399000),
    ('Cargador Portátil', 29000), ('Cable HDMI', 15000), ('Hub USB-C', 45000),
    ('Impresora HP', 179000), ('Router WiFi 6', 89000)
]

ciudades = ['Santiago', 'Valparaíso', 'Concepción', 'La Serena', 'Antofagasta', 
            'Temuco', 'Puerto Montt', 'Iquique', 'Rancagua', 'Talca']

metodos_pago = ['Tarjeta Crédito', 'Tarjeta Débito', 'Transferencia', 'Webpay', 'PayPal']

start_date = datetime(2022, 1, 1)
end_date = datetime(2024, 12, 31)

for i in range(500000):
    random_days = random.randint(0, (end_date - start_date).days)
    fecha = start_date + timedelta(days=random_days)
    
    producto, precio_base = random.choice(productos)
    cantidad = random.randint(1, 5)
    descuento = random.choice([0, 0, 0, 5, 10, 15, 20])
    precio_final = precio_base * (1 - descuento/100)
    total = precio_final * cantidad
    
    venta = {
        'id_venta': f'V{i+1:06d}',
        'fecha': fecha.strftime('%Y-%m-%d'),
        'producto': producto,
        'categoria': 'Tecnología',
        'cantidad': cantidad,
        'precio_unitario': int(precio_base),
        'descuento': descuento,
        'precio_final': int(precio_final),
        'total': int(total),
        'metodo_pago': random.choice(metodos_pago),
        'ciudad': random.choice(ciudades),
        'region': 'Chile'
    }
    ventas.append(venta)
    
    if (i + 1) % 100000 == 0:
        print(f"  Ventas generadas: {i+1}/500000")

df_ventas = pd.DataFrame(ventas)
df_ventas.to_csv('ventas.csv', index=False)
print(f"✓ Archivo ventas.csv creado: {len(df_ventas)} registros")

# ============== 2. DATASET DE NAVEGACIÓN WEB ==============
print("\nGenerando navegación web...")
navegacion = []
acciones = ['click', 'busqueda', 'vista_producto', 'agregar_carrito', 'vista_categoria']
dispositivos = ['desktop', 'mobile', 'tablet']

for i in range(1000000):
    fecha = start_date + timedelta(days=random.randint(0, (end_date - start_date).days),
                                   hours=random.randint(0, 23),
                                   minutes=random.randint(0, 59))
    
    nav = {
        'id_sesion': f'S{i+1:07d}',
        'fecha_hora': fecha.strftime('%Y-%m-%d %H:%M:%S'),
        'id_cliente': f'C{random.randint(1, 50000):05d}',
        'accion': random.choice(acciones),
        'pagina': random.choice(['home', 'catalogo', 'producto', 'carrito', 'checkout']),
        'tiempo_sesion_seg': random.randint(10, 3600),
        'dispositivo': random.choice(dispositivos),
        'navegador': random.choice(['Chrome', 'Firefox', 'Safari', 'Edge']),
        'clicks': random.randint(1, 50)
    }
    navegacion.append(nav)
    
    if (i + 1) % 200000 == 0:
        print(f"  Navegación generada: {i+1}/1000000")

df_navegacion = pd.DataFrame(navegacion)
df_navegacion.to_csv('navegacion.csv', index=False)
print(f"✓ Archivo navegacion.csv creado: {len(df_navegacion)} registros")

# ============== 3. DATASET DE INVENTARIO ==============
print("\nGenerando inventario...")
inventario = []
bodegas = ['Bodega Central Santiago', 'Bodega Valparaíso', 'Bodega Concepción', 
           'Bodega Norte', 'Bodega Sur']

for i in range(200000):
    producto, precio = random.choice(productos)
    
    inv = {
        'id_inventario': f'I{i+1:06d}',
        'fecha_registro': (start_date + timedelta(days=random.randint(0, 1095))).strftime('%Y-%m-%d'),
        'producto': producto,
        'sku': f'SKU{random.randint(1000, 9999)}',
        'bodega': random.choice(bodegas),
        'stock_actual': random.randint(0, 500),
        'stock_minimo': random.randint(10, 50),
        'stock_maximo': random.randint(200, 1000),
        'rotacion_mensual': random.randint(5, 100),
        'estado': random.choice(['disponible', 'disponible', 'disponible', 'agotado', 'en_reposicion'])
    }
    inventario.append(inv)
    
    if (i + 1) % 50000 == 0:
        print(f"  Inventario generado: {i+1}/200000")

df_inventario = pd.DataFrame(inventario)
df_inventario.to_csv('inventario.csv', index=False)
print(f"✓ Archivo inventario.csv creado: {len(df_inventario)} registros")

# ============== 4. DATASET DE CLIENTES ==============
print("\nGenerando clientes...")
clientes = []

for i in range(50000):
    fecha_registro = start_date + timedelta(days=random.randint(0, 1000))
    
    cliente = {
        'id_cliente': f'C{i+1:05d}',
        'nombre': fake.first_name(),
        'apellido': fake.last_name(),
        'email': fake.email(),
        'telefono': fake.phone_number(),
        'ciudad': random.choice(ciudades),
        'fecha_registro': fecha_registro.strftime('%Y-%m-%d'),
        'edad': random.randint(18, 70),
        'genero': random.choice(['M', 'F', 'Otro']),
        'segmento': random.choice(['Premium', 'Regular', 'Nuevo', 'VIP']),
        'total_compras': random.randint(0, 50),
        'valor_total_historico': random.randint(0, 5000000)
    }
    clientes.append(cliente)
    
    if (i + 1) % 10000 == 0:
        print(f"  Clientes generados: {i+1}/50000")

df_clientes = pd.DataFrame(clientes)
df_clientes.to_csv('clientes.csv', index=False)
print(f"✓ Archivo clientes.csv creado: {len(df_clientes)} registros")

# ============== RESUMEN ==============
print("\n" + "="*60)
print("RESUMEN DE DATOS GENERADOS")
print("="*60)
print(f"✓ ventas.csv: {len(df_ventas):,} registros")
print(f"✓ navegacion.csv: {len(df_navegacion):,} registros")
print(f"✓ inventario.csv: {len(df_inventario):,} registros")
print(f"✓ clientes.csv: {len(df_clientes):,} registros")
print(f"\nTOTAL: {len(df_ventas) + len(df_navegacion) + len(df_inventario) + len(df_clientes):,} registros")
print("="*60)
print("\nArchivos guardados en:", os.getcwd())
