from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", titulo="Início")

@app.route("/teste")
def sobre():
    return render_template("teste.html", titulo="Teste")

if __name__ == "__main__":
    # debug=True é útil em desenvolvimento (recarrega o servidor a cada mudança)
    app.run(debug=True)