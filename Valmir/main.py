from datetime import datetime

class Academia:
    def __init__(self):
        self.alunos = {}

    def cadastrar_aluno(self):
        nome = input("Digite o nome do aluno: ")
        idade = int(input("Digite a idade do aluno: "))
        peso = float(input("Digite o peso do aluno (kg): "))
        altura = float(input("Digite a altura do aluno (m): "))
        condicao_medica = input("Informe alguma condição médica relevante (ou deixe em branco): ")

        metas = {}
        metas['perda_peso'] = float(input("Meta de perda de peso (kg): "))
        metas['ganho_massa'] = float(input("Meta de ganho de massa muscular (kg): "))
        metas['melhoria_resistencia'] = float(input("Meta de melhoria da resistência: "))

        aluno = {
            'nome': nome,
            'idade': idade,
            'peso': peso,
            'altura': altura,
            'condicao_medica': condicao_medica,
            'metas': metas,
            'avaliacoes': [],
            'mensagens': [],
            'treino': []
        }

        self.alunos[nome] = aluno
        print(f"Aluno {nome} cadastrado com sucesso!\n")

    def realizar_avaliacao(self, aluno_nome):
        if aluno_nome in self.alunos:
            data_avaliacao = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            avaliacao = {
                'data': data_avaliacao,
                'teste_fisico': input("Resultado do teste físico: "),
                'medicao_peso': float(input("Medição de peso (kg): ")),
                'desempenho_exercicio': input("Análise de desempenho em exercícios específicos: ")
            }

            self.alunos[aluno_nome]['avaliacoes'].append(avaliacao)
            print(f"Avaliação para {aluno_nome} realizada com sucesso!\n")
        else:
            print(f"Aluno {aluno_nome} não encontrado.\n")

    def exibir_alunos(self):
        print("\nLista de Alunos:")
        for nome, aluno in self.alunos.items():
            print(f"\nNome: {aluno['nome']}")
            print(f"Idade: {aluno['idade']}")
            print(f"Peso: {aluno['peso']} kg")
            print(f"Altura: {aluno['altura']} m")
            print(f"Condição Médica: {aluno['condicao_medica']}")
            print("Metas:")
            for meta, valor in aluno['metas'].items():
                print(f"  {meta.capitalize()}: {valor}")
            print("\n")

    def exibir_avaliacoes(self, aluno_nome):
        if aluno_nome in self.alunos:
            print(f"\nAvaliações de {aluno_nome}:")
            for avaliacao in self.alunos[aluno_nome]['avaliacoes']:
                print(f"\nData: {avaliacao['data']}")
                print(f"Teste Físico: {avaliacao['teste_fisico']}")
                print(f"Medição de Peso: {avaliacao['medicao_peso']} kg")
                print(f"Desempenho em Exercícios: {avaliacao['desempenho_exercicio']}")
                print("\n")
        else:
            print(f"Aluno {aluno_nome} não encontrado.\n")

    def enviar_mensagem(self, remetente, destinatario, mensagem):
        if destinatario in self.alunos:
            data_envio = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            mensagem = {
                'remetente': remetente,
                'data_envio': data_envio,
                'mensagem': mensagem
            }
            self.alunos[destinatario]['mensagens'].append(mensagem)
            print(f"Mensagem enviada para {destinatario}.\n")
        else:
            print(f"Destinatário {destinatario} não encontrado.\n")

    def exibir_mensagens(self, aluno_nome):
        if aluno_nome in self.alunos:
            print(f"\nMensagens para {aluno_nome}:")
            for mensagem in self.alunos[aluno_nome]['mensagens']:
                print(f"\nRemetente: {mensagem['remetente']}")
                print(f"Data de Envio: {mensagem['data_envio']}")
                print(f"Mensagem: {mensagem['mensagem']}")
                print("\n")
        else:
            print(f"Aluno {aluno_nome} não encontrado.\n")

    def gerar_relatorio_progresso(self, aluno_nome):
        if aluno_nome in self.alunos:
            aluno = self.alunos[aluno_nome]
            ultima_avaliacao = aluno['avaliacoes'][-1] if aluno['avaliacoes'] else None
            metas = aluno['metas']

            relatorio = f"Relatório de Progresso para {aluno_nome}:\n"

            if ultima_avaliacao:
                relatorio += f"\nÚltima Avaliação (Data: {ultima_avaliacao['data']}):\n"
                relatorio += f"  - Teste Físico: {ultima_avaliacao['teste_fisico']}\n"
                relatorio += f"  - Medição de Peso: {ultima_avaliacao['medicao_peso']} kg\n"
                relatorio += f"  - Desempenho em Exercícios: {ultima_avaliacao['desempenho_exercicio']}\n"
            else:
                relatorio += "\nNenhuma avaliação realizada ainda.\n"

            relatorio += "\nMetas:\n"
            for meta, valor in metas.items():
                relatorio += f"  - {meta.capitalize()}: {valor}\n"

            print(relatorio)
        else:
            print(f"Aluno {aluno_nome} não encontrado.\n")

    def personalizar_treino_automatizado(self, aluno_nome):
        if aluno_nome in self.alunos:
            aluno = self.alunos[aluno_nome]
            ultima_avaliacao = aluno['avaliacoes'][-1] if aluno['avaliacoes'] else None
            metas = aluno['metas']

            if ultima_avaliacao:
                novo_treino = f"Treino Personalizado para {aluno_nome} (Sugestão Automática):\n"
                novo_treino += "Ajustes sugeridos com base na última avaliação e metas:\n"

                if ultima_avaliacao['desempenho_exercicio'] == 'Melhorou':
                    novo_treino += "Aumentar a intensidade dos exercícios.\n"

                aluno['treino'].append(novo_treino)
                print("Treino personalizado sugerido automaticamente e armazenado.\n")
            else:
                print("Não é possível personalizar o treino automaticamente. Nenhuma avaliação disponível.\n")
        else:
            print(f"Aluno {aluno_nome} não encontrado.\n")

    def exibir_historico_acompanhamento(self, aluno_nome):
        if aluno_nome in self.alunos:
            aluno = self.alunos[aluno_nome]
            
            print(f"Histórico de Acompanhamento para {aluno_nome}:\n")
            for avaliacao in aluno['avaliacoes']:
                print(f"Data: {avaliacao['data']}")
                print(f"Teste Físico: {avaliacao['teste_fisico']}")
                print(f"Medição de Peso: {avaliacao['medicao_peso']} kg")
                print(f"Desempenho em Exercícios: {avaliacao['desempenho_exercicio']}")
                print("\n")
            
            for treino in aluno['treino']:
                print(treino)
            
            print("\n")
        else:
            print(f"Aluno {aluno_nome} não encontrado.\n")

    def menu(self):
        while True:
            print("==== Menu ====")
            print("1. Cadastrar Aluno")
            print("2. Realizar Avaliação")
            print("3. Exibir Alunos")
            print("4. Exibir Avaliações de um Aluno")
            print("5. Enviar Mensagem")
            print("6. Exibir Mensagens de um Aluno")
            print("7. Gerar Relatório de Progresso")
            print("8. Personalizar Treino Automatizado")
            print("9. Exibir Histórico de Acompanhamento")
            print("10. Sair")

            escolha = input("Escolha uma opção (1/2/3/4/5/6/7/8/9/10): ")

            if escolha == '1':
                self.cadastrar_aluno()
            elif escolha == '2':
                aluno_nome = input("Digite o nome do aluno para a avaliação: ")
                self.realizar_avaliacao(aluno_nome)
            elif escolha == '3':
                self.exibir_alunos()
            elif escolha == '4':
                aluno_nome = input("Digite o nome do aluno para exibir as avaliações: ")
                self.exibir_avaliacoes(aluno_nome)
            elif escolha == '5':
                remetente = input("Digite o seu nome: ")
                destinatario = input("Digite o nome do destinatário: ")
                mensagem = input("Digite a mensagem: ")
                self.enviar_mensagem(remetente, destinatario, mensagem)
            elif escolha == '6':
                aluno_nome = input("Digite o nome do aluno para exibir as mensagens: ")
                self.exibir_mensagens(aluno_nome)
            elif escolha == '7':
                aluno_nome = input("Digite o nome do aluno para gerar o relatório de progresso: ")
                self.gerar_relatorio_progresso(aluno_nome)
            elif escolha == '8':
                aluno_nome = input("Digite o nome do aluno para personalizar o treino automaticamente: ")
                self.personalizar_treino_automatizado(aluno_nome)
            elif escolha == '9':
                aluno_nome = input("Digite o nome do aluno para exibir o histórico de acompanhamento: ")
                self.exibir_historico_acompanhamento(aluno_nome)
            elif escolha == '10':
                print("Saindo do programa. Até logo!")
                break
            else:
                print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    academia = Academia()
    academia.menu()
