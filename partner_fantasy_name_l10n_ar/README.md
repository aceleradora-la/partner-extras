# Partner Fantasy Name - Argentina

Imprime datos adicionales en el PDF de la factura de la localización argentina
(`l10n_ar`), de forma **configurable por compañía**:

- **Nombre de Fantasía** del cliente: línea propia debajo de la Razón Social,
  junto a los datos fiscales (Cond. IVA, CUIT). *Activado por defecto.*
- **Dirección de Entrega**: al final del bloque de datos del cliente, solo en
  documentos de venta (facturas, notas de crédito, recibos) y cuando difiere
  de la dirección de facturación. *Desactivado por defecto.*

Ambas opciones se configuran en el **formulario de la compañía**
(Ajustes → Usuarios y compañías → Compañías → pestaña *Información general*,
grupo *Facturas Argentinas*), por compañía.

## Instalación

Se **auto-instala** cuando `partner_fantasy_name` y `l10n_ar` están
instalados (tras actualizar la lista de aplicaciones). Compatible con Odoo
Community y Enterprise.

## Licencia

LGPL-3.0
