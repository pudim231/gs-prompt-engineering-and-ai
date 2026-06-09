"""Módulo de regras de decisão e thresholds em Python."""


def avaliar(dados):
    """Verifica limites críticos de telemetria e retorna alertas ativos."""
    alertas = []

    # Regra 1: Temperatura do Sensor Térmico crítica (risco de superaquecimento ou queima)
    if dados.get("sensor_termico", 0) > 75:
        alertas.append("CRÍTICO: Temperatura do sensor térmico alarmante! Risco de danos ao hardware.")

    # Regra 2: Bateria baixa (Ativa resposta automatizada de modo economia)
    if dados.get("energia_disponivel", 100) < 20:
        alertas.append("ALERTA: Bateria abaixo de 20%. Sistema em MODO ECONOMIA automático.")

    # Regra 3: Buffer de imagens muito cheio (falha ou atraso de downlink)
    if dados.get("buffer_imagens", 0) > 40:
        alertas.append("MODERADO: Buffer de imagens próximo do limite técnico. Janela de transmissão necessária.")

    return alertas
