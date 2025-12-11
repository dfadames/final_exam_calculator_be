from pydantic import BaseModel, Field
from typing import List


class Subject(BaseModel):
    """Modelo para representar una materia del semestre"""
    name: str = Field(..., description="Nombre de la materia", example="Cálculo I")
    grade: float = Field(..., ge=0.0, le=5.0, description="Nota obtenida (0.0 - 5.0)", example=4.5)
    credits: int = Field(..., gt=0, description="Número de créditos de la materia", example=4)


class SemesterRequest(BaseModel):
    """Modelo para la solicitud de cálculo del promedio del semestre"""
    subjects: List[Subject] = Field(..., min_length=1, description="Lista de materias del semestre")


class SubjectResult(BaseModel):
    """Modelo para el resultado de cada materia"""
    name: str
    grade: float
    credits: int
    weighted_grade: float = Field(..., description="Nota multiplicada por los créditos")


class SemesterResponse(BaseModel):
    """Modelo para la respuesta del cálculo del promedio"""
    subjects: List[SubjectResult]
    total_credits: int = Field(..., description="Total de créditos del semestre")
    semester_gpa: float = Field(..., description="Promedio ponderado del semestre")
    message: str = Field(..., description="Mensaje descriptivo del resultado")
