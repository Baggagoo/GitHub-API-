from datetime import datetime

def analyze_repository_data(repositories):
    if not repositories:
        return None

    # Análise do repositório com mais estrelas
    most_stars = max(repositories, key=lambda x: x['stars'])
    
    # Análise do repositório com mais forks
    most_forks = max(repositories, key=lambda x: x['forks'])
    
    # Descobrir as linguagens mais utilizadas
    language_count = {}
    for repo in repositories:
        language = repo['language']
        if language:
            language_count[language] = language_count.get(language, 0) + 1
    
    most_used_language = max(language_count, key=language_count.get) if language_count else None
    
    # Calcular o tempo médio entre a criação e a última atualização
    total_time = 0
    for repo in repositories:
        created_at = datetime.strptime(repo['created_at'], "%Y-%m-%dT%H:%M:%SZ")
        updated_at = datetime.strptime(repo['updated_at'], "%Y-%m-%dT%H:%M:%SZ")
        time_diff = (updated_at - created_at).total_seconds()
        total_time += time_diff
    
    average_time = total_time / len(repositories) if repositories else 0

    return {
        'most_stars': most_stars,
        'most_forks': most_forks,
        'most_used_language': most_used_language,
        'average_time_between_updates': average_time
    }