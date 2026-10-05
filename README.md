# Inventario Físico — caso de estudio

Aplicación para importar un reporte de existencias, registrar cantidades físicas y obtener un resumen para conciliación. Este repositorio publica documentación nueva, una captura sintética revisada y un ejemplo didáctico. El código operativo permanece privado.

## Problema y solución

Un conteo necesita distinguir artículos pendientes de artículos contados en cero, conservar cambios y evitar que dos personas sobrescriban una revisión. El recorrido vigente es **Subir reporte → Contar → Ver resumen**. El resultado apoya la conciliación externa; no actualiza automáticamente el ERP.

## Funcionalidades observadas

- Vista previa del Excel, incidencias y exclusiones explícitas.
- Asociación de almacén y permisos comprobados en el servidor.
- Búsqueda, filtros y paginación de partidas.
- Cantidades decimales exactas, historial, versión esperada e identificadores de reintento.
- Saldo y diferencia visibles después de guardar; pendientes diferenciados de cero.
- Finalización y exportación del resultado.
- Apariencia Sistema/Claro/Oscuro y diseño adaptable.

## Tecnologías

React, TypeScript, Vite, ASP.NET Core .NET 10, Entity Framework Core, Npgsql, PostgreSQL, ClosedXML y Playwright. La documentación privada registra un piloto con Render y Supabase. No se ha consultado su salud ni intervenido en él durante esta publicación.

## Evidencia

La revisión local del 5 de octubre de 2026 contrastó README, arquitectura, guía de conteo, informes de interfaz/publicación y código de conteo directo. El informe previo de interfaz registra 16 casos únicos Playwright sintéticos aprobados: diez de captura y seis visuales. Se cita como evidencia histórica; no se volvió a ejecutar esa suite para este caso documental.

![Inicio con sesión y API sintéticas](docs/images/inicio-sintetico.png)

Captura de la interfaz real en una prueba con API simulada, sin conteos operativos. No demuestra disponibilidad ni rendimiento del piloto.

## Ejecutar el ejemplo independiente

Requiere Python 3 y biblioteca estándar. Desde la raíz:

```text
python examples/verify.py
```

Comprueba diferencias exactas, cero y ausencia de conteo en cinco artículos inventados. No es una implementación de la API, permisos ni concurrencia del sistema original.

## Documentación

- [Arquitectura](docs/architecture.md).
- [Caso de estudio](docs/case-study.md).
- [Verificación y límites](docs/verification.md).
- [Ejemplo ficticio](examples/scenario.json).

## Pendientes

Recuperación remota, identidades simultáneas, dispositivos físicos, aceptación del área y autorización de operación. No hay captura offline garantizada. Licencia y responsabilidades históricas pendientes de decisión expresa; no se asigna licencia al código privado.
