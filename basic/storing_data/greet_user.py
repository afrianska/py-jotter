from pathlib import Path
import json

print(f"Welcome back, {json.loads(Path('username.json').read_text())}!")
