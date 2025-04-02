
```

import psycopg2
import redis
import json
import hvac  # HashiCorp Vault client
import os

# Vault Configuration
VAULT_ADDR = "http://localhost:8200"  # Change this to your Vault address
VAULT_TOKEN = os.getenv("VAULT_TOKEN")  # Set via environment variable for security
VAULT_SECRET_PATH = "secret/data/db/postgres"  # Adjust this based on your Vault path

# Connect to Vault and retrieve the PostgreSQL password
client = hvac.Client(url=VAULT_ADDR, token=VAULT_TOKEN)
vault_response = client.secrets.kv.v2.read_secret_version(path=VAULT_SECRET_PATH)
pg_password = vault_response["data"]["data"]["password"]  # Extract the password

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="demo_db",
    user="postgres",
    password=pg_password,
    host="localhost"
)

# Create a Redis client
redis_client = redis.StrictRedis(host="localhost", port=6379, db=0, decode_responses=True)

def get_user_from_db(user_id):
    """Fetch user details from PostgreSQL."""
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s;", (user_id,))
    user = cur.fetchone()
    cur.close()
    return user

def get_user(user_id):
    """Fetch user details from Redis cache or PostgreSQL."""
    cache_key = f"user:{user_id}"
    cached_user = redis_client.get(cache_key)

    if cached_user:
        print("Fetching from Redis Cache...")
        return json.loads(cached_user)
    else:
        print("Fetching from PostgreSQL...")
        user = get_user_from_db(user_id)
        if user:
            redis_client.setex(cache_key, 600, json.dumps(user))
        return user

# Example: Fetch user with ID 1
user = get_user(1)
if user:
    print(f"User Details: ID = {user[0]}, Name = {user[1]}, Email = {user[2]}")
else:
    print("User not found")

```
