"""Módulo de simulação de dados de telemetria do satélite."""
import random

def coletar():
    """Gera parâmetros reais baseados na trilha Envirosat do enunciado."""
    return {
        "sensor_termico": random.randint(15, 85),          # Detecção de focos de incêndio
        "sensor_optico_rgb_nir": random.randint(80, 100),  # Qualidade do sensor óptico
        "buffer_imagens": random.randint(0, 50),           # Imagens acumuladas não transmitidas
        "precisao_geolocalizacao": round(random.uniform(0.1, 5.0), 2), # Drift em metros
        "energia_disponivel": random.randint(12, 100)      # % da bateria dos painéis solares
    }
