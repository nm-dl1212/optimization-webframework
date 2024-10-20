import requests


MODEL_API_URL = "http://ml-api:5000/predict"


def call_model_api(feature_value):
    """モデルAPIへリクエストを送り、予測結果を取得する
    """
    response = requests.post(
        MODEL_API_URL,
        json={'feature': feature_value.tolist()}
    )
    result = response.json()
    return result['prediction']
