from pathlib import Path

def list_leagues():
    base_path = Path(__file__).resolve().parent.parent / "data"
    leagues = []

    if not base_path.exists():
        return {"error": "data folder not found", "path": str(base_path)}

    for item in base_path.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            leagues.append({
                "league_id": item.name,
                "name": item.name.replace("_", " ")
            })

    return leagues
