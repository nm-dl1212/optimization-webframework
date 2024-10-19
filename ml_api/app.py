from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    # リクエストから入力値を取得
    data = request.get_json()
    feature_range = data.get("feature", [0.2, 0.2])

    # 予測を実行(仮で2次関数を計算)
    prediction = (feature_range[0] - 0.5) ** 2 + feature_range[1]

    return jsonify({"prediction": prediction})


if __name__ == "__main__":
    app.run(port=5000, debug=True)
