from secrets import token_urlsafe


def generate_code():
    return token_urlsafe(6)

