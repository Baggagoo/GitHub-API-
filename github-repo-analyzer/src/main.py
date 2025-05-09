# main.py

from github_api import get_repositories
from excel_writer import write_repositories_to_excel as write_to_excel
from data_analysis import analyze_repository_data as analyze_data
from utils.helpers import validate_github_username

def main():
    try:
        username = input("Digite o nome de usuário do GitHub: ")
        username = validate_github_username(username)  # Validação do nome de usuário
        repositories = get_repositories(username)

        if repositories:
            write_to_excel(repositories)
            analysis = analyze_data(repositories)
            if analysis:
                print("Análise concluída com sucesso!")
                print(analysis)
            else:
                print("Nenhum dado disponível para análise.")
        else:
            print("Nenhum repositório encontrado ou ocorreu um erro ao buscar os dados.")
    except ValueError as e:
        print(f"Erro: {e}")
    except Exception as e:
        print(f"Ocorreu um erro inesperado: {e}")

if __name__ == "__main__":
    main()