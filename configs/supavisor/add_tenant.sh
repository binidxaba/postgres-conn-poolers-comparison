#!/bin/bash

curl -X PUT \
  'http://localhost:4000/api/tenants/dev_tenant' \
  --header 'Accept: application/json' \
  --header 'Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJvbGUiOiJhbm9uIiwiaWF0IjoxNjQ1MTkyODI0LCJleHAiOjE5NjA3Njg4MjR9.M9jrxyvPLkUxWgOYSf5dNdJ8v_eRrq810ShFRT8N-6M' \
  --header 'Content-Type: application/json' \
  --data-raw '{
  "tenant": {
    "db_host": "10.182.0.3",
    "db_port": 5432,
    "db_database": "postgres",
    "ip_version": "auto",
    "require_user": true,
    "default_max_clients": 3000,
    "default_pool_size": 100,
    "users": [
      {
        "db_user": "postgres",
        "db_password": "hello123",
        "mode_type": "transaction",
        "pool_checkout_timeout": 30000,
	"pool_size": 100
      }
    ]
  }
}'
