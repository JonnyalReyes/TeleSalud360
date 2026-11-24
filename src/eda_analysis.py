"""
Módulo de Análisis Exploratorio de Datos (EDA) y Pruebas Estadísticas
Proyecto: AstraMed - Samsung Innovation Campus (SIC)
"""

import pandas as pd
import numpy as np
from scipy import stats
from typing import Dict, Any


def compute_kpis(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Calcula los Indicadores Clave de Desempeño (KPIs) clínicos y operacionales.
    """
    total = len(df)
    satisfaccion_promedio = df["patient_satisfaction"].mean()
    tasa_alta_satisfaccion = (df["patient_satisfaction"] >= 4).mean() * 100
    tasa_baja_satisfaccion = (df["patient_satisfaction"] <= 2).mean() * 100
    duracion_promedio = df["duration_minutes"].mean()
    tasa_receta = (df["prescription_given"] == "Yes").mean() * 100
    tasa_seguimiento = (df["follow_up_required"] == "Yes").mean() * 100

    return {
        "total_consultas": total,
        "satisfaccion_promedio": round(satisfaccion_promedio, 2),
        "tasa_alta_satisfaccion_pct": round(tasa_alta_satisfaccion, 2),
        "tasa_baja_satisfaccion_pct": round(tasa_baja_satisfaccion, 2),
        "duracion_promedio_min": round(duracion_promedio, 2),
        "tasa_prescripcion_pct": round(tasa_receta, 2),
        "tasa_seguimiento_pct": round(tasa_seguimiento, 2),
    }


def analyze_specialties(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analiza métricas de rendimiento agrupadas por especialidad médica.
    """
    resumen = df.groupby("specialty").agg(
        total_consultas=("consultation_id", "count"),
        duracion_media=("duration_minutes", "mean"),
        satisfaccion_media=("patient_satisfaction", "mean"),
        tasa_seguimiento_pct=("follow_up_binary", lambda x: round(x.mean() * 100, 2)),
        tasa_receta_pct=("prescription_binary", lambda x: round(x.mean() * 100, 2)),
    ).reset_index()

    resumen["porcentaje_volumen"] = round((resumen["total_consultas"] / len(df)) * 100, 2)
    resumen["duracion_media"] = resumen["duracion_media"].round(2)
    resumen["satisfaccion_media"] = resumen["satisfaccion_media"].round(2)

    return resumen.sort_values(by="total_consultas", ascending=False)


def analyze_consultation_modes(df: pd.DataFrame) -> pd.DataFrame:
    """
    Analiza el rendimiento y satisfacción por modalidad (Video, Audio, Chat).
    """
    resumen = df.groupby("consultation_mode").agg(
        total_consultas=("consultation_id", "count"),
        duracion_media=("duration_minutes", "mean"),
        duracion_mediana=("duration_minutes", "median"),
        satisfaccion_media=("patient_satisfaction", "mean"),
        alta_satisfaccion_pct=("is_high_satisfaction", lambda x: round(x.mean() * 100, 2)),
        baja_satisfaccion_pct=("is_low_satisfaction", lambda x: round(x.mean() * 100, 2)),
    ).reset_index()

    resumen["porcentaje_uso"] = round((resumen["total_consultas"] / len(df)) * 100, 2)
    resumen["duracion_media"] = resumen["duracion_media"].round(2)
    resumen["satisfaccion_media"] = resumen["satisfaccion_media"].round(2)

    return resumen.sort_values(by="total_consultas", ascending=False)


def run_statistical_hypothesis_tests(df: pd.DataFrame) -> Dict[str, Any]:
    """
    Ejecuta pruebas estadísticas formales para validar hipótesis de telemedicina.
    - Test Chi-cuadrado: ¿Existe relación entre la Modalidad de Consulta y el Nivel de Satisfacción?
    - Test Chi-cuadrado: ¿Existe relación entre la Especialidad y el Requerimiento de Seguimiento?
    - ANOVA de una vía: ¿Difiere la duración según la modalidad de atención?
    """
    # 1. Chi-cuadrado: Modalidad vs Satisfacción
    contingency_mode_sat = pd.crosstab(df["consultation_mode"], df["satisfaction_category"])
    chi2_sat, p_sat, dof_sat, _ = stats.chi2_contingency(contingency_mode_sat)

    # 2. Chi-cuadrado: Especialidad vs Seguimiento
    contingency_spec_follow = pd.crosstab(df["specialty"], df["follow_up_required"])
    chi2_follow, p_follow, dof_follow, _ = stats.chi2_contingency(contingency_spec_follow)

    # 3. ANOVA: Duración entre Modalidades
    modes = df["consultation_mode"].unique()
    durations_by_mode = [df[df["consultation_mode"] == m]["duration_minutes"] for m in modes]
    f_stat, p_anova = stats.f_oneway(*durations_by_mode)

    return {
        "test_modalidad_satisfaccion": {
            "chi2_stat": round(chi2_sat, 4),
            "p_valor": round(p_sat, 4),
            "grados_libertad": dof_sat,
            "conclusion": (
                "No hay evidencia estadística suficiente de dependencia (p >= 0.05); "
                "la satisfacción se distribuye de manera equilibrada entre canales."
                if p_sat >= 0.05
                else "Existe asociación estadísticamente significativa entre el canal y la satisfacción (p < 0.05)."
            ),
        },
        "test_especialidad_seguimiento": {
            "chi2_stat": round(chi2_follow, 4),
            "p_valor": round(p_follow, 4),
            "grados_libertad": dof_follow,
            "conclusion": (
                "La necesidad de seguimiento no difiere significativamente por especialidad en la muestra (p >= 0.05)."
                if p_follow >= 0.05
                else "La tasa de seguimiento varía significativamente según la especialidad (p < 0.05)."
            ),
        },
        "anova_duracion_modalidad": {
            "f_stat": round(f_stat, 4),
            "p_valor": round(p_anova, 4),
            "conclusion": (
                "La duración media de consulta es consistente entre Audio, Video y Chat (p >= 0.05)."
                if p_anova >= 0.05
                else "Existen diferencias significativas en duración entre las modalidades (p < 0.05)."
            ),
        },
    }
