# 環境構築
DBの初期化
```bash
. initial_db.sh 
```

djangoサーバーを実行
```
python manage.py runserver
```

# 操作
新規ユーザーを作成
```bash
curl -X POST http://127.0.0.1:8000/api/users/ \
-H "Content-Type: application/json" \
-d '{
    "username": "new_user",
    "password": "password123",
    "email": "new_user@example.com"
}'
```

上記のユーザーに対してトークンを発行し、環境変数にセットする。
```bash
export TOKEN=$(curl -X POST http://127.0.0.1:8000/auth/ \
-H "Content-Type: application/json" \
-d '{
    "username": "new_user",
    "password": "password123"
}' \
 | jq -r .token)
```

最適化ケースを新規作成
```bash
curl -X POST http://127.0.0.1:8000/api/cases/ \
-H "Content-Type: application/json" \
-H "Authorization: Token ${TOKEN}" \
-d '{
    "remarks": "First optimization",
    "max_trial_number": 3,
    "sampling_method": "latin",
    "objective_function": "Program_A"
}'
```


実行した最適化ケースの確認
```bash
curl http://127.0.0.1:8000/api/cases/ \
-H "Content-Type: application/json" \
-H "Authorization: Token ${TOKEN}" | jq
```

最適化ケースIDを指定して，個別の実行結果を確認
```bash
curl http://127.0.0.1:8000/api/results/?case_id=1 \
-H "Content-Type: application/json" \
-H "Authorization: Token ${TOKEN}" | jq
```

```bash
curl "http://127.0.0.1:8000/api/results/?case_id=1&include_details=true" \
-H "Content-Type: application/json" \
-H "Authorization: Token ${TOKEN}" | jq
```


# 管理
python manage.py createsuperuser
