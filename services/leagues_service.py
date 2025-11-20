def list_leagues():
    leagues = []

    base_path = Path("data")
    for item in base_path.iterdir():
        if item.is_dir() and not item.name.startswith("."):
            leagues.append({
                "league_id": item.name.lower(),
                "name": item.name
            })

    return leagues
