# Automatización de registro de facturas de gastos de viaje

## Descripción general del proyecto

Este proyecto consiste en una automatización desarrollada con **GitHub Actions** y **Python** para apoyar el proceso de reembolso de gastos de viaje de empleados.

Actualmente, cuando un empleado viaja por trabajo, debe tomar fotos de las facturas de sus gastos y enviarlas al correo de la empresa para solicitar el reembolso. Este proceso normalmente es manual, lento y depende de que el área administrativa revise cada factura, descargue los archivos, registre la información y apruebe el pago.

Con esta solución se propone una mejora del proceso: cuando una imagen de una factura se sube a una carpeta del repositorio, **GitHub Actions ejecuta automáticamente un flujo de trabajo** que procesa la imagen, extrae el texto con OCR y registra la información en un archivo CSV.

---

## Problema que se busca resolver

El proceso manual de reembolso de gastos presenta varios problemas:

- Demoras de varios días en la revisión y aprobación
- Dependencia de trabajo manual del área administrativa
- Riesgo de pérdida o desorganización de facturas
- Errores al transcribir información a Excel o a otros registros
- Falta de trazabilidad clara del estado de cada factura

Este proyecto busca demostrar cómo una automatización puede reducir tiempos y mejorar el control del proceso.

---

## Objetivo del proyecto

Automatizar el registro inicial de facturas de gastos de viaje para reducir trabajo manual, mejorar la organización de la información y agilizar el proceso de revisión administrativa.

---

## Tecnologías utilizadas

- **GitHub**: repositorio del proyecto
- **GitHub Actions**: automatización del flujo de trabajo
- **Python**: procesamiento de archivos
- **Tesseract OCR**: lectura de texto dentro de imágenes
- **Pillow (PIL)**: manejo de imágenes
- **CSV**: almacenamiento de los datos procesados

---

## Funcionamiento general

El flujo del sistema es el siguiente:

1. Un usuario sube una foto de una factura a la carpeta `receipts/`
2. GitHub detecta el cambio en el repositorio
3. GitHub Actions ejecuta automáticamente el workflow
4. El script en Python abre la imagen
5. Se aplica OCR para extraer el texto de la factura
6. El sistema identifica un monto total probable
7. Los datos se guardan en `data/expenses.csv`
8. La factura se mueve a la carpeta `processed/`

---

## Estructura del proyecto

```bash
automatizacion_gastos/
│
├── receipts/
│   └── Carpeta donde se suben las facturas nuevas
│
├── processed/
│   └── Carpeta donde se guardan las facturas ya procesadas
│
├── scripts/
│   └── process_receipt.py
│
├── data/
│   └── expenses.csv
│
└── .github/
    └── workflows/
        └── receipts.yml
