from typing import List
from app.models import Subject, SubjectResult


def calculate_semester_gpa(subjects: List[Subject]) -> tuple[List[SubjectResult], int, float]:
    """
    Calcula el promedio ponderado del semestre.
    
    El promedio se calcula como:
    GPA = Σ(nota × créditos) / Σ(créditos)
    
    Args:
        subjects: Lista de materias con sus notas y créditos
        
    Returns:
        tuple: (resultados por materia, total de créditos, promedio ponderado)
    """
    results = []
    total_credits = 0
    weighted_sum = 0.0
    
    for subject in subjects:
        weighted_grade = subject.grade * subject.credits
        weighted_sum += weighted_grade
        total_credits += subject.credits
        
        results.append(SubjectResult(
            name=subject.name,
            grade=subject.grade,
            credits=subject.credits,
            weighted_grade=round(weighted_grade, 2)
        ))
    
    gpa = weighted_sum / total_credits if total_credits > 0 else 0.0
    
    return results, total_credits, round(gpa, 2)


def get_performance_message(gpa: float) -> str:
    """
    Genera un mensaje según el promedio obtenido.
    
    Args:
        gpa: Promedio ponderado del semestre
        
    Returns:
        str: Mensaje descriptivo del rendimiento
    """
    if gpa >= 4.5:
        return "¡Excelente rendimiento! Felicitaciones."
    elif gpa >= 4.0:
        return "¡Muy buen rendimiento! Sigue así."
    elif gpa >= 3.5:
        return "Buen rendimiento. Puedes mejorar aún más."
    elif gpa >= 3.0:
        return "Rendimiento aceptable. Hay espacio para mejorar."
    else:
        return "Rendimiento bajo. Te recomendamos buscar apoyo académico."
