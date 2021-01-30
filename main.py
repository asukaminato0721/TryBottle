from bottle import redirect, run, request, view, get, post


username = password = ""
# username password
userinfo = {
    "a": "a",
    "b": "b",
    "c": "c",
    "d": "d",
}


@get("/login")
@view("login")
def login():
    return {"username": username, "password": password}


@post("/login")
def do_login():
    global username, password
    username = request.forms.get("username")
    password = request.forms.get("password")
    if check_login(username, password):
        return redirect("/userpage")
    else:
        return "<p>Login failed.</p>"


@get("/userpage")
@view("userpage")
def userpage():
    return {"username": username, "password": password, "userinfo": userinfo}


@get("/register")
@view("register")
def register_page():
    return {"username": username, "password": password}


@post("/register")
def dont_care():
    global username, password
    username = request.forms.get("username")
    password = request.forms.get("password")
    if username in userinfo:
        return "<p>用户名被占用</p>"
    else:
        userinfo.update({str(username): str(password)})
        redirect("/userpage")


@get("/")
def auto_redirect():
    return redirect("/login")


def check_login(username: str, password: str):
    return username in userinfo and password == userinfo[username]


run(debug=True, port=4000, host="127.0.0.1", reloader=True)
