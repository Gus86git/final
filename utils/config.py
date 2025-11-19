# Configuraciones del sistema SafeBuild

CLASS_NAMES = {
    'person': 'Trabajador',
    'helmet': 'Casco de Seguridad', 
    'safety_vest': 'Chaleco Reflectante'
}

ALERT_LEVELS = {
    'ALTA': {
        'color': '#DC2626',
        'icon': '🚨',
        'priority': 1
    },
    'MEDIA': {
        'color': '#D97706',
        'icon': '⚠️',
        'priority': 2
    },
    'OK': {
        'color': '#059669',
        'icon': '✅',
        'priority': 3
    }
}

SAFETY_RULES = {
    'helmet_required': True,
    'vest_required': True,
    'min_workers_for_alert': 1
}
