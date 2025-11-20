from pathlib import Path

# Diretório base do projeto (onde está este arquivo)
BASE_DIR = Path(__file__).resolve().parent

# Pasta onde ficam as ligas (cada liga é uma pasta dentro de data/)
# Exemplo:
#   data/Laliga_Espanha/Barcelona.csv
#   data/Premier_League/Arsenal.csv
DATA_DIR = BASE_DIR / "data"
