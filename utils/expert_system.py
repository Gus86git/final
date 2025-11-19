class SafetyExpertSystem:
    """
    Sistema experto para análisis de seguridad en obras de construcción
    Aplica reglas basadas en conocimiento experto para evaluar condiciones de seguridad
    """
    
    def __init__(self):
        # Definición de reglas de seguridad
        self.rules = {
            # REGLA 1: Situación crítica - ningún trabajador con casco
            'no_helmet_critical': {
                'condition': lambda stats: stats['persons'] > 0 and stats['helmets'] == 0,
                'message': "CRÍTICO: Ningún trabajador usa casco de seguridad",
                'level': "ALTA",
                'action': "DETENER actividades inmediatamente y notificar al supervisor de seguridad"
            },
            
            # REGLA 2: Algunos trabajadores sin casco
            'no_helmet_partial': {
                'condition': lambda stats: stats['persons'] > 0 and stats['helmets'] < stats['persons'],
                'message': f"ALTA: {stats['persons'] - stats['helmets']} trabajador(es) sin casco detectado(s)",
                'level': "ALTA", 
                'action': "Aislar el área y proveer EPP inmediatamente. Notificar al jefe de cuadrilla"
            },
            
            # REGLA 3: Ningún trabajador con chaleco
            'no_vest_critical': {
                'condition': lambda stats: stats['persons'] > 0 and stats['vests'] == 0,
                'message': "MEDIA: Ningún trabajador usa chaleco reflectante",
                'level': "MEDIA",
                'action': "Notificar al supervisor y proveer chalecos de seguridad. Revisión en 1 hora"
            },
            
            # REGLA 4: Algunos trabajadores sin chaleco  
            'no_vest_partial': {
                'condition': lambda stats: stats['persons'] > 0 and stats['vests'] < stats['persons'],
                'message': f"MEDIA: {stats['persons'] - stats['vests']} trabajador(es) sin chaleco detectado(s)",
                'level': "MEDIA",
                'action': "Recordar uso obligatorio de chaleco en reunión de seguridad. Monitoreo continuo"
            },
            
            # REGLA 5: Condiciones óptimas de seguridad
            'proper_equipment': {
                'condition': lambda stats: stats['persons'] > 0 and stats['helmets'] >= stats['persons'] and stats['vests'] >= stats['persons'],
                'message': "OK: Todo el personal cuenta con Equipo de Protección Personal completo",
                'level': "OK",
                'action': "Continuar monitoreo y mantener los estándares de seguridad actuales"
            },
            
            # REGLA 6: No hay trabajadores en el área
            'no_persons': {
                'condition': lambda stats: stats['persons'] == 0,
                'message': "OK: No se detectaron trabajadores en el área analizada",
                'level': "OK", 
                'action': "Continuar con el monitoreo rutinario del área"
            }
        }
    
    def analyze_detections(self, detections):
        """
        Analiza las detecciones utilizando el sistema experto de reglas
        
        Args:
            detections (list): Lista de detecciones con class_name, confidence, bbox
            
        Returns:
            dict: Resultado del análisis con nivel de alerta, mensaje y acción recomendada
        """
        
        # PASO 1: Contar detecciones por clase
        person_count = sum(1 for det in detections if det['class_name'] == 'person')
        helmet_count = sum(1 for det in detections if det['class_name'] == 'helmet') 
        vest_count = sum(1 for det in detections if det['class_name'] == 'safety_vest')
        
        # Estadísticas para el sistema experto
        detection_stats = {
            'persons': person_count,
            'helmets': helmet_count,
            'vests': vest_count
        }
        
        # PASO 2: Aplicar reglas en orden de prioridad (de más crítica a menos)
        for rule_name, rule in self.rules.items():
            if rule['condition'](detection_stats):
                # Formatear mensaje dinámico si es necesario
                formatted_message = rule['message']
                if 'stats' in rule['message']:
                    # Reemplazar placeholder con valores reales
                    formatted_message = rule['message'].format(
                        persons=detection_stats['persons'],
                        helmets=detection_stats['helmets'], 
                        vests=detection_stats['vests']
                    )
                
                # Retornar análisis completo
                return {
                    'alert_level': rule['level'],
                    'alert_message': formatted_message,
                    'recommended_action': rule['action'],
                    'statistics': detection_stats
                }
        
        # PASO 3: Retorno por defecto si ninguna regla aplica
        return {
            'alert_level': "OK",
            'alert_message': "Condiciones normales de seguridad detectadas",
            'recommended_action': "Continuar con el monitoreo rutinario",
            'statistics': detection_stats
        }
    
    def get_rules_info(self):
        """
        Obtener información sobre todas las reglas del sistema experto
        Útil para debugging y documentación
        """
        rules_info = []
        for rule_name, rule in self.rules.items():
            rules_info.append({
                'name': rule_name,
                'description': rule['message'],
                'level': rule['level']
            })
        return rules_info
