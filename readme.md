# 🖥️ Sistema de Control de Uso de Computadores

> Aplicación web para monitorear el uso de computadores por parte de los campers en las instalaciones de Cajasan. Captura información del sistema operativo Ubuntu, la almacena y la visualiza mediante una interfaz web.

---

## 📋 Tabla de Contenido

- [Problemática](#problemática)
- [Solución](#solución)
- [Levantamiento de Requerimientos](#levantamiento-de-requerimientos)
- [Flujo del Sistema](#flujo-del-sistema)
- [Historias de Usuario](#historias-de-usuario)
- [Metodología de Trabajo](#metodología-de-trabajo)
- [Frontend](#frontend)
- [Backend](#backend)
- [Diagramas UML](#diagramas-uml)
- [Tecnologías Utilizadas](#tecnologías-utilizadas)
- [Base de Datos](#base-de-datos)
- [Seguridad](#seguridad)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Cómo Ejecutar](#cómo-ejecutar)
- [Conclusión](#conclusión)

---

## ❗ Problemática

Actualmente no se cuenta con un sistema que permita llevar el control del uso de los computadores utilizados por los campers, lo que dificulta conocer:

- Tiempo de uso
- Usuarios conectados
- Actividad de los equipos

---

## ✅ Solución

Se desarrolló un aplicativo web que permite registrar y visualizar el uso de los computadores mediante la captura de datos del sistema operativo, utilizando un script en Python que envía la información a un backend.

---

## 📝 Levantamiento de Requerimientos

### Preguntas al cliente

- ¿Qué información desea registrar de los computadores?
- ¿Se requiere identificar a los usuarios?
- ¿Quién tendrá acceso a los datos?
- ¿Se necesita visualización en tiempo real?

### Requerimientos identificados

- Registro de uso de computadores
- Identificación de usuarios
- Visualización de datos
- Almacenamiento de información

---

## 🔄 Flujo del Sistema

1. El usuario utiliza el computador
2. El script captura información del sistema
3. Se envían los datos al backend
4. El backend almacena la información
5. El frontend permite visualizar los registros

---

## 👤 Historias de Usuario

- Como **administrador**, quiero ver el tiempo de uso de cada computador para llevar control.
- Como **administrador**, quiero identificar qué usuario utilizó un equipo para tener trazabilidad.
- Como **administrador**, quiero visualizar los registros en una interfaz web.

---

## 🗂️ Metodología de Trabajo

### Product Backlog

- Captura de datos del sistema
- Desarrollo del backend
- Desarrollo del frontend
- Visualización de registros

### Sprints

| Sprint | Descripción |
|--------|-------------|
| Sprint 1 | Desarrollo del script de monitoreo |
| Sprint 2 | Desarrollo del backend (Flask) |
| Sprint 3 | Desarrollo del frontend |

### Tablero Kanban

| 🔲 Pendiente | 🔄 En proceso | ✅ Terminado |
|-------------|--------------|-------------|
| Diseño      | Backend      | Script      |
| Frontend    |              |             |

---

## 🎨 Frontend

Interfaz web desarrollada con HTML, CSS y JavaScript para visualizar los registros en forma de tabla.

### Wireframe (baja fidelidad)

```
[ Botón: Cargar datos ]

-------------------------------
| PC | Usuario | Tiempo | Fecha |
-------------------------------
```

### Mockup (media fidelidad)

Representación visual mejorada del sistema con estructura de tabla y estilos básicos.

### Prototipo (alta fidelidad)

El prototipo funcional corresponde al archivo `index.html` desarrollado.

---

## ⚙️ Backend

Desarrollado en **Python** con el framework **Flask**. Permite recibir datos mediante peticiones HTTP, almacenarlos y proporcionarlos al frontend.

---

## 📐 Diagramas UML

### Diagrama de Clases

```
+------------------+
|    Registro      |
+------------------+
| pc               |
| usuarios         |
| uptime           |
| timestamp        |
+------------------+
```

### Diagrama de Secuencia

```
Script          Backend         Frontend
  |                |                |
  |-- GET datos -->|                |
  |<-- sistema ----|                |
  |-- POST datos ->|                |
  |                |-- almacena --->|
  |                |<-- GET datos --|
  |                |-- respuesta -->|
```

1. El script obtiene datos del sistema
2. El script envía datos al backend (`POST`)
3. El backend almacena la información
4. El frontend solicita datos (`GET`)
5. El backend responde con los registros

### Casos de Uso

**Actor:** Administrador

- Consultar registros
- Visualizar uso de computadores

---

## 🛠️ Tecnologías Utilizadas

| Tecnología | Uso |
|------------|-----|
| Python | Script de monitoreo y backend |
| Flask | Framework web del backend |
| HTML | Estructura del frontend |
| CSS | Estilos del frontend |
| JavaScript | Lógica del frontend |

---

## 🗄️ Base de Datos

Debido al alcance académico del proyecto, se utilizó almacenamiento en formato **JSON** en lugar de un sistema gestor de bases de datos.

### DDL

```sql
CREATE TABLE registros (
    pc        TEXT,
    usuarios  TEXT,
    uptime    TEXT,
    timestamp TEXT
);
```

### DML

```sql
INSERT INTO registros VALUES (...);
```

### DQL

```sql
SELECT * FROM registros;
```

> **Nota:** No se implementaron triggers, eventos ni procedimientos almacenados debido a la naturaleza del almacenamiento utilizado.

---

## 🔒 Seguridad

- Validación básica de datos en el backend
- Uso en entorno local
- Acceso limitado al sistema

---

## 📁 Estructura del Proyecto

```
control_pc/
│
├── backend/
│   ├── app.py
│   └── data.json
│
├── scripts/
│   └── monitor.py
│
├── frontend/
│   └── index.html
│
└── README.md
```

---

## 🚀 Cómo Ejecutar

### 1. Ejecutar el backend

```bash
cd backend
python3 app.py
```

### 2. Ejecutar el script de monitoreo

```bash
cd scripts
python3 monitor.py
```

### 3. Abrir el frontend

Abrir el archivo directamente en el navegador:

```
frontend/index.html
```

---

## 📌 Conclusión

El sistema desarrollado permite llevar un control básico del uso de los computadores mediante la captura de datos del sistema operativo, cumpliendo con los requerimientos planteados y adaptándose a las limitaciones del entorno, como la imposibilidad de instalar software adicional en los equipos.