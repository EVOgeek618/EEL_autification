import eel
import os
import hashlib
import pandas as pd

@eel.expose
def register(login, email, password, password_2):
    df = pd.read_csv("web\\database.csv")

    if not login and not email and not password and not password_2:
        return "Введите все значения"

    if password != password_2:
        return "Пароли не совпадают"

    if not df[df["login"]==login].empty:
        return "Пользователь с таким логином уже есть"

    if not df[df["email"]==email].empty:
        return "Пользователь с такой почтой уже есть"


    salt = os.urandom(8)
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
    hash_password = salt + key
    print(salt, key, hash_password)
    df = pd.read_csv("web\\database.csv")
    df.loc[len(df.index)] = [login, email, hash_password]
    df.to_csv("web\\database.csv", index=False)

    return "Done"

@eel.expose
def check(login, password):
    df = pd.read_csv("web\\database.csv")

    login_user = df[df["login"] == login]
    if login_user.empty:
        return "Пользователь с таким логином не зарегистрирован в системе"

    password_user = login_user.iloc[0]["password"][2:-1]
    password_user = password_user.encode('raw_unicode_escape').decode('unicode_escape').encode('raw_unicode_escape')

    salt = password_user[:8]
    key = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, 1000)
    hash_password = salt + key

    if hash_password != password_user:
        return "Неверный логин или пароль"
    return "Done", login

# Exposing the random_python function to javascript
@eel.expose
def hello(login):
    eel.show("result.html")



if __name__ =="__main__":
    eel.init("web")
    eel.start("index.html")
