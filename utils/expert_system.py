class SafetyExpertSystem:
    def __init__(self):
        self.rules = {
            'no_helmet_critical': {
                'condition': lambda det: det['persons'] > 0 and det['helmets'] == 0,
                'message': "CRÍTICO: Ningún trabajador usa casco de seguridad",
                'level': "ALTA",
                'action': "DETENER actividades y notificar supervisor inmediatamente"
            },
            'no_helmet_partial': {
                'condition': lambda det: det['persons'] > 0 and det['helmets'] < det['persons'],
                'message': "ALTA: Trabajadores detectados sin casco de seguridad",
                'level': "ALTA",
                'action': "Aislar área y proveer EPP inmediatamente"
            },
            'no_vest_critical': {
                'condition': lambda det: det['persons'] > 0 and det['vests'] == 0,
                'message': "MEDIA: Ningún trabajador usa chaleco reflectante",
                'level': "MEDIA",
                'action': "Notificar a supervisor y proveer chalecos"
            },
            'no_vest_partial': {
                'condition': lambda det: det['persons'] > 0 and det['vests'] < det['persons'],
                'message': "MEDIA: Trabajadores detectados sin chaleco reflectante",
                'level': "MEDIA",
                'action': "Recordar uso de chaleco en reunión de seguridad"
            },
            'proper_equipment': {
                'condition': lambda det: det['persons'] > 0 and det['helmets'] >= det['persons'] and det['vests'] >= det['persons'],
                'message': "OK: Todo el personal con EPP adecuado",
                'level': "OK",
                'action': "Continuar monitoreo y mantener estándares"
            },
            'no_persons': {
                'condition': lambda det: det['persons'] == 0,
                'message': "OK: No se detectaron trabajadores en el área",
                'level': "OK",
                'action': "Monitoreo continuo del área"
            }
        }
    
    def analyze_detections(self, detections):
        """Analiza las detecciones usando el sistema experto de reglas"""
        
        # Contar detecciones por clase
        person_count = sum(1 for det in detections if det['class_name'] == 'person')
        helmet_count = sum(1 for det in detections if det['class_name'] == 'helmet') 
        vest_count = sum(1 for det in detections if det['class_name'] == 'safety_vest')
        
        stats = {
            'persons': person_count,
            'helmets': helmet_count,
            'vests': vest_count
        }
        
        # Aplicar reglas en orden de prioridad
        for rule_name, rule in self.rules.items():
            if rule['condition'](stats):
                return {
                    'alert_level': rule['level'],
                    'alert_message': rule['message'],
                    'recommended_action': rule['action'],
                    'statistics': stats
                }
        
        # Default return
        return {
            'alert_level': "OK",
            'alert_message': "Condiciones normales de seguridad",
            'recommended_action': "Monitoreo continuo",
            'statistics': stats
        }
