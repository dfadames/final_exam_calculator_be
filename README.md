# Calculadora de Promedio Universitario - API

API REST desarrollada con FastAPI para calcular el promedio ponderado de un semestre universitario.

## 📁 Estructura del Proyecto

```
final_exam_calculator_be/
├── app/
│   ├── __init__.py
│   ├── main.py          # Aplicación principal FastAPI
│   ├── models.py        # Modelos Pydantic
│   └── calculator.py    # Lógica de cálculo del promedio
├── Dockerfile
├── .dockerignore
├── requirements.txt
└── README.md
```

## 🚀 Instalación y Ejecución

### Opción 1: Ejecución Local

1. Crear un entorno virtual:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Instalar dependencias:
```bash
pip install -r requirements.txt
```

3. Ejecutar la aplicación:
```bash
uvicorn app.main:app --reload
```

### Opción 2: Docker

1. Construir la imagen:
```bash
docker build -t gpa-calculator-api .
```

2. Ejecutar el contenedor:
```bash
docker run -d -p 8000:8000 --name gpa-api gpa-calculator-api
```

## 📖 Documentación de la API

Una vez ejecutada la aplicación, accede a:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

## 🔌 Endpoints

### GET /
Health check básico

### GET /health
Health check para Docker/Kubernetes

### POST /calculate
Calcula el promedio ponderado del semestre.

**Request Body:**
```json
{
  "subjects": [
    {
      "name": "Cálculo I",
      "grade": 4.5,
      "credits": 4
    },
    {
      "name": "Física I",
      "grade": 4.0,
      "credits": 4
    },
    {
      "name": "Programación",
      "grade": 5.0,
      "credits": 3
    }
  ]
}
```

**Response:**
```json
{
  "subjects": [
    {
      "name": "Cálculo I",
      "grade": 4.5,
      "credits": 4,
      "weighted_grade": 18.0
    },
    {
      "name": "Física I",
      "grade": 4.0,
      "credits": 4,
      "weighted_grade": 16.0
    },
    {
      "name": "Programación",
      "grade": 5.0,
      "credits": 3,
      "weighted_grade": 15.0
    }
  ],
  "total_credits": 11,
  "semester_gpa": 4.45,
  "message": "¡Muy buen rendimiento! Sigue así."
}
```

## 📐 Fórmula del Promedio

El promedio ponderado se calcula con la siguiente fórmula:

$$GPA = \frac{\sum_{i=1}^{n} (nota_i \times creditos_i)}{\sum_{i=1}^{n} creditos_i}$$

## 🛠️ Tecnologías

- **Python 3.11**
- **FastAPI**
- **Pydantic**
- **Uvicorn**
- **Docker**
