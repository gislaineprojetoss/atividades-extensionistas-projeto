# Sistema simples de registro e acompanhamento para oficinas de autocuidado

# Estruturas de dados para armazenar informações
participantes = {}  # Dicionário: {nome: ru}
oficinas = []  # Lista de nomes de oficinas
presencas = []  # Lista de tuplas: [(nome_participante, nome_oficina)]


def cadastrar_participante(nome, ru):
    """Cadastra um novo participante."""
    if nome in participantes:
        print(f"⚠️ Participante {nome} já cadastrado!")
        return
    participantes[nome] = ru
    print(f"✅ Participante {nome} cadastrado!")


def cadastrar_oficina(nome_oficina):
    """Cadastra uma nova oficina."""
    if nome_oficina in oficinas:
        print(f"⚠️ Oficina '{nome_oficina}' já cadastrada!")
        return
    oficinas.append(nome_oficina)
    print(f"✅ Oficina '{nome_oficina}' cadastrada!")


def registrar_presenca(nome_participante, nome_oficina):
    """Registra a presença de um participante em uma oficina."""
    if nome_participante not in participantes:
        print(f"❌ Erro: Participante {nome_participante} não encontrado.")
        return
    if nome_oficina not in oficinas:
        print(f"❌ Erro: Oficina '{nome_oficina}' não encontrada.")
        return

    registro = (nome_participante, nome_oficina)
    if registro in presencas:
        print(f"⚠️ Presença de {nome_participante} em {nome_oficina} já registrada!")
        return

    presencas.append(registro)
    print(f"✅ Presença registrada: {nome_participante} em {nome_oficina}!")


def gerar_relatorio_presencas():
    """Gera um relatório simples de presenças."""
    print("\n📋 Relatório de presenças:\n")
    if not presencas:
        print("Nenhuma presença registrada ainda.")
        return

    for nome, oficina in presencas:
        print(f"{nome} participou da oficina '{oficina}'")


# --- Simulação de Uso do Sistema ---

# Cadastrar participantes
cadastrar_participante("Maria", "1001")
cadastrar_participante("João", "1002")

# Cadastrar oficinas
cadastrar_oficina("Oficina de Culinária")
cadastrar_oficina("Oficina de Exercícios")

# Registrar presenças
registrar_presenca("Maria", "Oficina de Culinária")
registrar_presenca("João", "Oficina de Exercícios")

# Gerar relatório
gerar_relatorio_presencas()