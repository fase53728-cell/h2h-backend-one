from pathlib import Path

def list_leagues():
    leagues = []

    base_path = Path("data")   # <-- CERTO AQUI
    for item in base_path.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            leagues.append({
                "league_id": item.name,
                "name": item.name.replace("_", " ")
            })

    return leagues
