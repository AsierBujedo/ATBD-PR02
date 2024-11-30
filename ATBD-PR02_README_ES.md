
# ATBD-PR02

**ATBD-PR02** es un proyecto para la asignatura de Big Data del Máster en Computación y Sistemas Inteligentes. Este repositorio se centra en la implementación de una solución de base de datos NoSQL para gestionar datos estructurados de jugadoras de fútbol utilizando MongoDB, Python y Docker.

---

## Tabla de Contenidos

- [Resumen](#resumen)
- [Características](#características)
- [Instalación](#instalación)
- [Uso](#uso)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Flujo de Datos](#flujo-de-datos)
- [Contribuciones](#contribuciones)
- [Solución de Problemas](#solución-de-problemas)
- [Contacto](#contacto)

---

## Resumen

El proyecto ATBD-PR02 simula un caso de uso real para gestionar y consultar estadísticas de jugadoras de fútbol utilizando bases de datos NoSQL. El objetivo principal es evaluar la flexibilidad, capacidad de indexación y rendimiento de MongoDB para almacenar estructuras de datos jerárquicas.

### Objetivos Clave:
1. Implementar un esquema de MongoDB adecuado para datos de jugadoras de fútbol, incluyendo estadísticas, información personal y equipos.
2. Automatizar el procesamiento e inserción de datos para hasta 100 registros de jugadoras.
3. Ejecutar consultas avanzadas y analizar los tiempos de ejecución para optimizar el esquema y el rendimiento de la base de datos.
4. Proporcionar un flujo de trabajo amigable para la ingesta, procesamiento y consulta de datos.

---

## Características

- **Integración con MongoDB**: Utiliza MongoDB para almacenar datos estructurados en documentos JSON.
- **Transformación de Datos**: `transform.py` procesa datos CSV en un formato estructurado para MongoDB.
- **Inserciones Masivas**: Inserta múltiples registros de manera eficiente usando `pymongo`.
- **Ejecución de Consultas Personalizadas**: `queries.py` implementa y mide el rendimiento de consultas avanzadas en MongoDB.
- **Modificación de Registros**: `modifyRegistries.py` automatiza la actualización de registros, como cambiar nombres de jugadoras a mayúsculas.
- **Soporte Docker**: Proporciona un entorno Dockerizado para MongoDB, simplificando la implementación.
- **Análisis de Rendimiento**: Mide tiempos de ejecución para identificar oportunidades de optimización.
- **Código Modular**: Scripts organizados para una ejecución flexible y modular.

---

## Instalación

### Requisitos Previos:
- Python 3.8 o superior
- MongoDB instalado localmente o accesible de forma remota
- Docker (opcional para despliegues con contenedores)

### Pasos de Instalación:

1. **Clonar el Repositorio**:
   ```bash
   git clone https://github.com/AsierBujedo/ATBD-PR02.git
   ```

2. **Acceder al Directorio del Proyecto**:
   ```bash
   cd ATBD-PR02
   ```

3. **Crear un Entorno Virtual de Python**:
   ```bash
   python -m venv venv
   source venv/bin/activate  # En Windows, usa venv\Scripts\activate
   ```

4. **Instalar Dependencias de Python**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Configurar Variables de Entorno**:
   - Crear un archivo `.env` en el directorio raíz.
   - Agregar las siguientes variables:
     ```
     SERVER=tu_host_de_base_de_datos
     PORT=tu_puerto_de_base_de_datos
     USR=tu_usuario_de_base_de_datos
     PWD=tu_contraseña_de_base_de_datos
     ```

6. **Opcional: Usar Docker para MongoDB**:
   - Iniciar el contenedor Docker:
     ```bash
     docker-compose --profile mongo up
     ```

---

## Uso

### Flujo General

1. **Ejecutar el Script Principal**:
   - Este script procesa e inserta datos en MongoDB.
   ```bash
   python main.py
   ```

2. **Ejecutar Scripts de Consultas**:
   - Ejecuta consultas específicas y mide su rendimiento:
     ```bash
     python queries.py
     ```

3. **Modificar Registros**:
   - Actualiza registros existentes en la base de datos:
     ```bash
     python modifyRegistries.py
     ```

### Comandos de Ejemplo:

- **Transformación de Datos**:
  ```bash
  python transform.py
  ```

- **Insertar Datos en MongoDB**:
  ```bash
  python main.py
  ```

- **Modificar Registros de Jugadoras**:
  ```bash
  python modifyRegistries.py
  ```

- **Consultar Datos**:
  ```bash
  python queries.py
  ```

---

## Estructura del Proyecto

```
ATBD-PR02/
├── data/
│   ├── raw/             # Datos originales (archivos CSV, etc.)
│   └── processed/       # Datos procesados para MongoDB
├── docker/              # Archivos de configuración Docker
├── results/             # Resultados y logs de salida
├── .env                 # Configuración de entorno
├── .gitignore           # Reglas de exclusión de Git
├── big_data_e2.pdf      # Documentación del proyecto
├── main.py              # Script principal de ejecución
├── modifyRegistries.py  # Script para modificar registros
├── queries.py           # Script para ejecutar consultas
├── requirements.txt     # Dependencias de Python
├── transform.py         # Script de transformación de datos
└── README.md            # README del proyecto
```

---

## Flujo de Datos

1. **Preparación de Datos**:
   - Usa `transform.py` para limpiar y organizar datos originales en formato CSV.

2. **Inserción de Datos**:
   - Inserta 100 registros en MongoDB usando `main.py`. Este paso incluye la creación de índices para mejorar el rendimiento.

3. **Consultas de Datos**:
   - Ejecuta consultas para filtrar jugadoras según condiciones como `EstimatedStartYear` o nombres de equipos que comiencen con "Manchester."

4. **Actualización de Registros**:
   - Modifica datos específicos (por ejemplo, nombres en mayúsculas) con `modifyRegistries.py`.

---

## Contribuciones

¡Las contribuciones son bienvenidas! Sigue estos pasos para colaborar:

1. Haz un fork del repositorio.
2. Crea una rama para tu mejora:
   ```bash
   git checkout -b feature/nombre-de-tu-mejora
   ```
3. Haz commits con tus cambios:
   ```bash
   git commit -m "Agrega tu mejora"
   ```
4. Sube tu rama a tu fork:
   ```bash
   git push origin feature/nombre-de-tu-mejora
   ```
5. Abre un pull request al repositorio principal.

---

## Solución de Problemas

- **Problemas con Dependencias**:
  - Asegúrate de usar la versión correcta de Python (ver `requirements.txt`).
  - Usa un entorno virtual para gestionar las dependencias de forma aislada.

- **Conectividad con la Base de Datos**:
  - Verifica que el archivo `.env` contiene las credenciales correctas para MongoDB.
  - Prueba la conexión manualmente con un cliente de MongoDB o la herramienta `mongo`.

- **Problemas con Docker**:
  - Asegúrate de que Docker está instalado y en ejecución en tu máquina.
  - Valida que el archivo `docker-compose.yml` esté correctamente configurado.

---

## Contacto

Para preguntas, sugerencias o soporte, contacta a [Asier Bujedo](mailto:asier.bujedo@opendeusto.es) o abre un issue en este repositorio.

---
