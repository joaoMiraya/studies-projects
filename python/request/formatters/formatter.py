def format_user_data(user_data: dict) -> str:
    return (
        f"\n👤 {user_data.get('name', 'Not Found')} ({user_data['login']})\n"
        f"📍 Localization: {user_data.get('location', 'Not Found')}\n"
        f"📝 Bio: {user_data.get('bio', 'Sem bio')}\n"
        f"👥 Followers: {user_data['followers']} | Following: {user_data['following']}\n"
        f"📦 Public Repositories: {user_data['public_repos']}\n"
    )


def format_repositories(repos: list[dict]) -> str:
    if not repos:
        return "repositories not founded"

    formatted = "\n📂 Repositories:\n"
    for repo in repos:
        formatted += (
            f" - {repo['name']} ⭐ {repo['stargazers_count']} | "
            f"Language: {repo.get('language', 'Not Found')}\n"
        )
    return formatted
