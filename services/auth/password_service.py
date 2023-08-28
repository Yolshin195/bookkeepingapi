from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password):
    return pwd_context.hash(password)


if __name__ == "__main__":
    hashed_admin_password = get_password_hash("admin")
    print(hashed_admin_password)
    print(verify_password("admin", hashed_admin_password))
