from openpyxl import Workbook

def write_repositories_to_excel(repositories, filename='repositories.xlsx'):
    wb = Workbook()
    ws = wb.active
    ws.title = "GitHub Repositories"

    # Definindo os cabeçalhos das colunas
    headers = ["Nome", "Descrição", "Linguagem", "Estrelas", "Forks", "Data de Criação", "Data da Última Atualização"]
    ws.append(headers)

    # Adicionando os dados dos repositórios
    for repo in repositories:
        ws.append([
            repo.get('name'),
            repo.get('description'),
            repo.get('language'),
            repo.get('stargazers_count'),
            repo.get('forks_count'),
            repo.get('created_at'),
            repo.get('updated_at')
        ])

    # Salvando o arquivo Excel
    wb.save(filename)