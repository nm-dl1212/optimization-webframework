# 操作
新規ユーザーを作成
```
curl -X POST http://127.0.0.1:8000/api/users/ \
-H "Content-Type: application/json" \
-d '{
    "username": "new_user",
    "password": "password123",
    "email": "new_user@example.com"
}'
```

上記のユーザーに対してトークンを発行
```
curl -X POST http://127.0.0.1:8000/auth/ \
-H "Content-Type: application/json" \
-d '{
    "username": "new_user",
    "password": "password123"
}'
```

最適化ケースを新規作成
```
curl -X POST http://127.0.0.1:8000/api/optim/ \
-H "Content-Type: application/json" \
-H "Authorization: Token 4fe2af6ab996a6bc062028e25369992519d7a7db" \
-d '{
    "remarks": "First optimization",
    "max_attempt_number": 3,
    "initial_sampling_metod": "latin",
    "objective_function": "Program_A"
}'
```