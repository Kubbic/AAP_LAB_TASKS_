import functools

current_user = {"username": "admin", "role": "superuser"}

# TODO: Implementacja dekoratora @require_role
def require_role(role):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            if current_user.get("role") != role:
                raise PermissionError(f"Odmowa dostępu! Wymagana rola: '{role}'")
            return func(*args, **kwargs)
        return wrapper
    return decorator

#Testowe funkcje
@require_role("superuser")
def test_superuser():
    print("Test superuser")

@require_role("user")
def test_user():
    print("Test user")

test_superuser()
test_user()