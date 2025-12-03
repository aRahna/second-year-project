from flask import Flask, render_template, request, jsonify
from MarkovChains import Chains


app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])  # главная страница
def main():
    return render_template("Главная.html")

@app.route("/_back_p", methods=["GET", "POST"])
def background_process():
    try:
        order = float(request.args.get("order"))
        chains = Chains(order=int(order),
                        filename="poems Baijron_clean.txt",
                        length=50)
        output = chains.getPoem(rest=False)
        return jsonify(result=output)
    except:
        pass


@app.route("/api/v1/poem", methods=["GET"])
def api_all():
    try:
        if "order" in request.args:
            order = int(request.args["order"])
        else:
            return "Ошибка"
        chains = Chains(order=order,
                        filename="poems Baijron_clean.txt",
                        length=50)
        output = chains.getPoem(rest=True)
        return jsonify(result=output)
    except:
        pass


if __name__ == "__main__":
    app.run(debug = True)
