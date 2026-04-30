from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/enviar", methods=["POST"])
def enviar():
    nome = request.form.get("nome", "").strip()
    if not nome:
        return "Você não digitou nem um nome."
    
    return f"Olá, {nome}. O backend recebeu seu formulário! :D"

if __name__ == "__main__":
    app.run(debug=True)