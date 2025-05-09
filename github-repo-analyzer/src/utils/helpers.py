from datetime import datetime

def validate_github_username(username):
    if not isinstance(username, str) or len(username.strip()) == 0:
        raise ValueError("O nome de usuário do GitHub deve ser uma string não vazia.")
    if " " in username or not username.isalnum():
        raise ValueError("O nome de usuário do GitHub deve conter apenas caracteres alfanuméricos e sem espaços.")
    return username.strip()

def format_date(date_str):
    """Formata uma data ISO 8601 para o formato DD/MM/AAAA."""
    try:
        date_obj = datetime.strptime(date_str, "%Y-%m-%dT%H:%M:%SZ")
        return date_obj.strftime("%d/%m/%Y")
    except (ValueError, TypeError):
        return None  # Retorna None em vez de "Data inválida"

def format_repository_data(repo):
    return {
        "name": repo.get("name"),
        "description": repo.get("description", "Sem descrição"),
        "language": repo.get("language", "Não especificado"),
        "stars": repo.get("stargazers_count", 0),
        "forks": repo.get("forks_count", 0),
        "created_at": repo.get("created_at"),  # Mantém no formato ISO 8601 para cálculos
        "updated_at": repo.get("updated_at"),  # Mantém no formato ISO 8601 para cálculos
    }