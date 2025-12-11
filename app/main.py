from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from app.models import SemesterRequest, SemesterResponse
from app.calculator import calculate_semester_gpa, get_performance_message

app = FastAPI(
    title="Calculadora de Promedio Universitario",
    description="API para calcular el promedio ponderado de un semestre universitario",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configuración de CORS para permitir peticiones desde cualquier origen
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/", tags=["Health"])
async def root():
    """Endpoint de salud para verificar que la API está funcionando"""
    return {"status": "ok", "message": "Calculadora de Promedio Universitario API"}


@app.get("/health", tags=["Health"])
async def health_check():
    """Endpoint de health check para Docker/Kubernetes"""
    return {"status": "healthy"}


@app.post("/calculate", response_model=SemesterResponse, tags=["Calculator"])
async def calculate_gpa(request: SemesterRequest):
    """
    Calcula el promedio ponderado del semestre.
    
    El promedio se calcula usando la fórmula:
    **GPA = Σ(nota × créditos) / Σ(créditos)**
    
    - **subjects**: Lista de materias con nombre, nota (0.0-5.0) y créditos
    
    Retorna el promedio ponderado y detalles de cada materia.
    """
    try:
        results, total_credits, gpa = calculate_semester_gpa(request.subjects)
        message = get_performance_message(gpa)
        
        return SemesterResponse(
            subjects=results,
            total_credits=total_credits,
            semester_gpa=gpa,
            message=message
        )
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
