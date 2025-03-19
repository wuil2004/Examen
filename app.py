from flask import Flask, render_template, request
from puzzle import ejecutar_metodo  # Importamos la lógica del puzzle

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultados = None

    if request.method == "POST":
        estado_inicial = list(map(int, request.form["estado_inicial"].split()))
        solucion = list(map(int, request.form["solucion"].split()))
        resultados = {}

        for metodo in ["BFS", "DFS", "DFS_REC"]:
            resultado = ejecutar_metodo(metodo, estado_inicial, solucion)
            resultados[metodo] = resultado  # ✅ Guardamos correctamente la salida
        
        print(resultados)  # 🔍 Verifica en la terminal que los resultados no son None
    
    return render_template("index.html", resultados=resultados)

if __name__ == "__main__":
    app.run(debug=True)
