# H2H Backend - CSV por time

Estrutura pronta para integrar com seu painel H2H.

## Estrutura

- `data/` → cada liga é uma pasta
  - `Laliga_Espanha/` → aqui dentro vão os CSVs dos times (Barcelona.csv, Real_Madrid.csv, etc.)
- `services/leagues_service.py` → leitura das ligas e times
- `main.py` → rotas FastAPI

## Como rodar local

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```

Depois acesse:

- `GET /` → status da API
- `GET /leagues`
- `GET /leagues/{league_id}/teams`
- `GET /leagues/{league_id}/team/{team_id}`
```
