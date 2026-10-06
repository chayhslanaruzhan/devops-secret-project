import os

def get_secret_status():
    secret = os.getenv("APP_SECRET")

    if secret:
        return "Secret is configured"
    return "Secret is missing"


if __name__ == "__main__":
    print(get_secret_status())
