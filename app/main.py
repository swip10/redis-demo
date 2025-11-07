from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import redis
import os, time

REDIS_URL = os.getenv("REDIS_URL", "redis://redis:6379/0")
r = redis.Redis.from_url(REDIS_URL, decode_responses=True)

app = FastAPI(title="Redis Key-Value Demo")

@app.get("/")
def home(request: Request):
    """Compteur de visites et cache IP"""
    visits = r.incr("visits:global")  # incrément atomique
    r.set("last_ip", request.client.host, ex=300)  # TTL 5 min
    r.lpush("events:visits", f"{int(time.time())}:{request.client.host}")
    r.ltrim("events:visits", 0, 49)  # garder les 50 dernières
    return JSONResponse({
        "message": "Bienvenue dans la démo Redis !",
        "visits_global": visits,
        "last_ip": r.get("last_ip"),
    })

@app.get("/stats")
def stats():
    """Afficher les dernières visites"""
    recent = r.lrange("events:visits", 0, 9)
    return {"recent_visits": recent}
