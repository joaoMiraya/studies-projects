from services.requestsService import get_user, get_user_repositories
from formatters.formatter import format_repositories, format_user_data

def main():
    username = input("Enter GitHub username: ")
    try:
        user_data = get_user(username)
        repos = get_user_repositories(username)

        print(format_user_data(user_data))
        print(format_repositories(repos))

    except Exception as err:
        print(f"Error getting data {err}")

if __name__ == "__main__":
    main()