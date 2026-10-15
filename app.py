from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = "123"

CPF = "12345678900"
SENHA = "euamominhanamorada"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        cpf = request.form["cpf"]
        senha = request.form["senha"]

        if cpf == CPF and senha == SENHA:
            session["usuario"] = cpf
            return redirect("/painel")

        return render_template("login.html", erro="CPF ou senha inválidos")

    return render_template("login.html")

@app.route("/painel")
def painel():
    if "usuario" not in session:
        return redirect("/login")

    return render_template("painel.html", usuario=session["usuario"])

@app.route("/sair")
def sair():
    session.clear()
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)