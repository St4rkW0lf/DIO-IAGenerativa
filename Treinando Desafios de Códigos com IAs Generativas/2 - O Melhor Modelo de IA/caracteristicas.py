.class ModeloIA:
    def _init_(self, nome, desempenho, velocidade, custo, capacidades):
        self.nome = nome
        self.desempenho = desempenho
        self.velocidade = velocidade
        self.custo = custo
        self.capacidades = capacidades
    
    def _str_(self):
        return self.nome

# Função para recomendar o modelo de IA com base nas características fornecidas
def recomendar_modelo(caracteristicas):
    modelos = [
        ModeloIA("Claude 3 Opus", 9, 10, 5, ["Pesquisa", "Desenvolvimento acelerado"]),
        ModeloIA("Claude 3 Sonnet", 8, 5, 7, ["Codificação", "Recuperação de informações"]),
        ModeloIA("Claude 3 Haiku", 7, 9, 6, ["Velocidade", "Resumo de dados não estruturados"])
    ]

    modelo_recomendado = None

    capacidades_usuario = [capacidade.lower() for capacidade in caracteristicas['Capacidades']]

    for modelo in modelos:
        capacidades_modelo = [capacidade.lower() for capacidade in modelo.capacidades]
        
        if all(capacidade in capacidades_usuario for capacidade in capacidades_modelo):
            if modelo_recomendado is None or modelo.desempenho > modelo_recomendado.desempenho:
                modelo_recomendado = modelo

    return modelo_recomendado if modelo_recomendado else "Nenhum modelo encontrado."

# Função para gerar uma explicação para o modelo recomendado
def gerar_explicacao(modelo, caracteristicas):
    if isinstance(modelo, ModeloIA):
        explicacao = f"O {modelo.nome} é o modelo recomendado."
        return explicacao
    else:
        return modelo

# Função para obter as características desejadas do usuário
def obter_caracteristicas():
    caracteristicas = {}
    caracteristicas['Desempenho'] = int(input())
    caracteristicas['Velocidade'] = int(input())
    caracteristicas['Custo'] = int(input())
    capacidades = input().split(',')
    caracteristicas['Capacidades'] = [capacidade.strip() for capacidade in capacidades]
    return caracteristicas

# Obter características de entrada
caracteristicas_entrada = obter_caracteristicas()

# Recomendar o modelo com base nas características
melhor_modelo = recomendar_modelo(caracteristicas_entrada)

# Gerar explicação para o modelo recomendado
explicacao = gerar_explicacao(melhor_modelo, caracteristicas_entrada)

# Imprimir a explicação
print(explicacao)
