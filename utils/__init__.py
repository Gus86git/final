"""
Paquete utils para SafeBuild
Contiene módulos auxiliares para el sistema
"""

__version__ = "1.0.0"
__author__ = "Equipo SafeBuild"
__description__ = "Módulos auxiliares para el sistema de monitoreo de seguridad"

# Importaciones para facilitar el acceso
from .expert_system import SafetyExpertSystem
from .config import CLASS_NAMES, ALERT_LEVELS, SAFETY_RULES

__all__ = [
    'SafetyExpertSystem',
    'CLASS_NAMES', 
    'ALERT_LEVELS',
    'SAFETY_RULES'
]
