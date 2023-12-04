import numpy as np
import pandas as pd
import datetime

class Aluno:
    def __init__(self, nome):
        self.nome = nome
        self.perfil_nutricional = {
            'habitos_alimentares': '',
            'restricoes_alimentares': '',
            'objetivos_peso': '',
            'preferencias_alimentares': ''
        }
        self.questionario_preenchido = False

    def preencher_questionario(self):
        print(f"\nQuestionário Inicial para {self.nome}:")
        self.perfil_nutricional['habitos_alimentares'] = input("Hábitos alimentares: ")
        self.perfil_nutricional['restricoes_alimentares'] = input("Restrições alimentares: ")
        self.perfil_nutricional['objetivos_peso'] = input("Objetivos de peso: ")
        self.perfil_nutricional['preferencias_alimentares'] = input("Preferências alimentares: ")
        self.questionario_preenchido = True

    def atualizar_perfil(self, habitos, restricoes, objetivos, preferencias):
        self.perfil_nutricional['habitos_alimentares'] = habitos
        self.perfil_nutricional['restricoes_alimentares'] = restricoes
        self.perfil_nutricional['objetivos_peso'] = objetivos
        self.perfil_nutricional['preferencias_alimentares'] = preferencias

    def exibir_perfil(self):
        print(f"\nPerfil Nutricional de {self.nome}:")
        for chave, valor in self.perfil_nutricional.items():
            print(f"{chave.capitalize()}: {valor}")

    def registrar_dieta_diaria(self):
        if not self.questionario_preenchido:
            print("Preencha o questionário inicial antes de registrar a dieta.")
            return

        print(f"\nRegistrando a Dieta Diária para {self.nome}:")
        entrada_alimentar = input("Descreva sua ingestão alimentar diária: ")
        print(f"Dieta registrada para {self.nome}: {entrada_alimentar}")

    def receber_orientacoes_nutricionais(self):
        if not self.questionario_preenchido:
            print("Preencha o questionário inicial antes de receber orientações.")
            return

        print(f"\nOrientações Nutricionais Personalizadas para {self.nome}:")
        # Lógica para gerar orientações com base nas informações do aluno
        if 'Perder peso' in self.perfil_nutricional['objetivos_peso']:
            print("Sugestão: Ajuste a dieta para reduzir a ingestão calórica e inclua exercícios regulares.")
        else:
            print("Sugestão: Mantenha uma dieta equilibrada e ajuste as porções conforme necessário.")

class PerfilNutricional:
    def __init__(self):
        self.habitos_alimentares = ''
        self.restricoes_alimentares = ''
        self.objetivos_peso = ''
        self.preferencias_alimentares = ''

    def preencher_perfil(self, habitos, restricoes, objetivos, preferencias):
        self.habitos_alimentares = habitos
        self.restricoes_alimentares = restricoes
        self.objetivos_peso = objetivos
        self.preferencias_alimentares = preferencias

    def exibir_perfil(self):
        print("\nPerfil Nutricional:")
        print(f"Hábitos Alimentares: {self.habitos_alimentares}")
        print(f"Restrições Alimentares: {self.restricoes_alimentares}")
        print(f"Objetivos de Peso: {self.objetivos_peso}")
        print(f"Preferências Alimentares: {self.preferencias_alimentares}")

class RegistroDiario:
    def __init__(self):
        self.registros = []

    def adicionar_registro(self, entrada):
        self.registros.append(entrada)

    def exibir_registros(self):
        print("\nRegistros Diários:")
        for i, entrada in enumerate(self.registros, start=1):
            print(f"{i}. {entrada}")

    def analisar_dieta(self):
        if not self.registros:
            print("Nenhum registro diário encontrado.")
            return

        dados_alimentares = np.array([entrada.split(",") for entrada in self.registros])
        df = pd.DataFrame(dados_alimentares, columns=["Refeição", "Lanche", "Quantidade"])
        total_calorias = df['Quantidade'].astype(float).sum()

        print(f"\nAnálise Nutricional:")
        print(f"Total de Calorias Consumidas: {total_calorias} calorias")

class OrientacoesNutricionais:
    def __init__(self, perfil, registro_diario):
        self.perfil = perfil
        self.registro_diario = registro_diario

    def gerar_orientacoes(self):
        if not self.perfil.habitos_alimentares or not self.registro_diario.registros:
            print("Preencha o perfil e registre a dieta para gerar orientações.")
            return

        print("\nOrientações Nutricionais Personalizadas:")
        # Lógica para gerar orientações com base nas informações do perfil e análise nutricional
        if 'Perder peso' in self.perfil.objetivos_peso:
            print("Sugestão: Ajuste a dieta para reduzir a ingestão calórica e inclua exercícios regulares.")
        else:
            print("Sugestão: Mantenha uma dieta equilibrada e ajuste as porções conforme necessário.")

class SistemaAcompanhamento:
    def __init__(self, meta_agua, meta_proteina):
        self.registros_agua = {}
        self.registros_suplementos = {}
        self.meta_agua = meta_agua
        self.meta_proteina = meta_proteina

    def registrar_agua(self, aluno, quantidade):
        if aluno not in self.registros_agua:
            self.registros_agua[aluno] = []
        data_atual = datetime.date.today()
        self.registros_agua[aluno].append({"data": data_atual, "quantidade": quantidade})

    def registrar_suplemento(self, aluno, suplemento):
        if aluno not in self.registros_suplementos:
            self.registros_suplementos[aluno] = []
        data_atual = datetime.date.today()
        self.registros_suplementos[aluno].append({"data": data_atual, "suplemento": suplemento})

    def verificar_hidratacao(self, aluno):
        total_agua = sum(registro["quantidade"] for registro in self.registros_agua.get(aluno, []))
        if total_agua < self.meta_agua:
            return f"{aluno}, beba mais água! Apenas {total_agua} ml hoje."

    def verificar_metas_nutricionais(self, aluno):
        total_proteina = sum(1 for registro in self.registros_suplementos.get(aluno, []) if registro["suplemento"] == "proteina")
        if total_proteina < self.meta_proteina:
            return f"{aluno}, você precisa de mais proteína. Apenas {total_proteina} suplementos de proteína registrados."

class IntegracaoApp:
    def __init__(self):
        self.dados_app = None

    def sincronizar_dados(self, dados):
        # Lógica de sincronização com aplicativos de rastreamento alimentar
        self.dados_app = dados

    def exibir_dados_sincronizados(self):
        print("\nDados Sincronizados com Aplicativos:")
        print(self.dados_app)

class ComunicacaoNutricionista:
    def __init__(self, nome_nutricionista):
        self.nome_nutricionista = nome_nutricionista
        self.mensagens = []

    def enviar_mensagem(self, mensagem):
        self.mensagens.append(f"{self.nome_nutricionista}: {mensagem}")

    def exibir_mensagens(self):
        print("\nMensagens do Nutricionista:")
        for mensagem in self.mensagens:
            print(mensagem)

class SistemaNutricao:
    def __init__(self, perfil, registro_diario, integracao_app, comunicacao_nutricionista):
        self.perfil = perfil
        self.registro_diario = registro_diario
        self.integracao_app = integracao_app
        self.comunicacao_nutricionista = comunicacao_nutricionista

    def integrar_app_rastreamento(self, dados_app):
        self.integracao_app.sincronizar_dados(dados_app)
        self.integracao_app.exibir_dados_sincronizados()

    def fornecer_feedback(self, mensagem):
        self.comunicacao_nutricionista.enviar_mensagem(mensagem)

    def exibir_feedback_nutricionista(self):
        self.comunicacao_nutricionista.exibir_mensagens()

# Exemplo de uso
aluno1 = Aluno("João")
aluno1.preencher_questionario()
aluno1.exibir_perfil()
aluno1.registrar_dieta_diaria()
aluno1.receber_orientacoes_nutricionais()

perfil_aluno = PerfilNutricional()
perfil_aluno.preencher_perfil("Saudáveis", "Nenhuma", "Perder peso", "Vegetariana")

registro_aluno = RegistroDiario()
registro_aluno.adicionar_registro("Café da Manhã, Frutas, 200g")
registro_aluno.adicionar_registro("Almoço, Frango grelhado, 300g")
registro_aluno.adicionar_registro("Lanche, Barrinha de cereal, 1 unidade")

perfil_aluno.exibir_perfil()
registro_aluno.exibir_registros()

registro_aluno.analisar_dieta()

orientacoes_aluno = OrientacoesNutricionais(perfil_aluno, registro_aluno)
orientacoes_aluno.gerar_orientacoes()

sistema = SistemaAcompanhamento(meta_agua=2000, meta_proteina=3)
sistema.registrar_agua("Aluno1", 1500)
sistema.registrar_suplemento("Aluno1", "proteina")

print(sistema.verificar_hidratacao("Aluno1"))
print(sistema.verificar_metas_nutricionais("Aluno1"))

integracao_app = IntegracaoApp()
comunicacao_nutricionista = ComunicacaoNutricionista("Nutricionista1")

sistema_nutricao = SistemaNutricao(perfil_aluno, registro_aluno, integracao_app, comunicacao_nutricionista)
dados_app_rastreamento = {"alimento": "Maçã", "calorias": 50}
sistema_nutricao.integrar_app_rastreamento(dados_app_rastreamento)
sistema_nutricao.fornecer_feedback("Preciso de mais orientações sobre minha dieta.")
sistema_nutricao.exibir_feedback_nutricionista()

