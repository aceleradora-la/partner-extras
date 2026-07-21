# Partner Fantasy Name / Nombre de Fantasía

Agrega el campo **Nombre de Fantasía** (`fantasy_name`) a clientes y proveedores
(`res.partner`) y lo integra en todas las búsquedas y reportes relevantes.

Compatible con Odoo **Community** y **Enterprise**.

## Funcionalidad

- **Ficha de contacto**: nuevo campo *Nombre de Fantasía* en el formulario de
  clientes/proveedores (debajo del NIF/CUIT/RUT).
- **Búsqueda global de contactos**: al buscar un contacto por nombre, también
  se busca por su nombre de fantasía (`_rec_names_search`). Esto aplica a
  *cualquier* lugar donde se seleccione un cliente o proveedor:
  - Campo *Cliente* en pedidos de venta (igual que el nombre o la dirección
    de entrega).
  - Campo *Cliente/Proveedor* en facturas.
  - Cualquier otro campo many2one hacia contactos.
- **Pedidos de venta**: búsqueda por nombre de fantasía en la vista de lista.
- **Facturas**: búsqueda por nombre de fantasía en la vista de lista.
- **Análisis de ventas** (`sale.report`): columna *Nombre de Fantasía*
  disponible para búsqueda y como agrupación en la tabla dinámica (pivot) y
  gráficos.
- **Análisis de facturación** (`account.invoice.report`): ídem.

## Instalación

Copiar la carpeta `partner_fantasy_name` a su directorio de addons,
actualizar la lista de aplicaciones e instalar **Partner Fantasy Name**.

Al actualizar el módulo se reconstruyen automáticamente las vistas SQL de los
reportes de ventas y facturación.

## Ramas

| Rama | Versión de Odoo |
|------|-----------------|
| `17.0` | Odoo 17 Community / Enterprise |
| `18.0` | Odoo 18 Community / Enterprise |
| `19.0` | Odoo 19 Community / Enterprise |

## Licencia

LGPL-3.0
