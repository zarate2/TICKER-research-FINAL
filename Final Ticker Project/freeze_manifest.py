"""Write current file checksums. This is a build manifest, not a historical AI-off precommit."""
from datetime import datetime,timezone
import hashlib
import json
from pathlib import Path
ROOT=Path(__file__).resolve().parent
items=[]
for path in sorted(ROOT.rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts or path.name in ['MANIFEST.json','.DS_Store'] or '.venv' in path.parts:
        continue
    items.append({'file':str(path.relative_to(ROOT)),'bytes':path.stat().st_size,'sha256':hashlib.sha256(path.read_bytes()).hexdigest()})
manifest={'generated_utc':datetime.now(timezone.utc).isoformat(),'type':'AI-assisted final build manifest, not a human AI-off prediction','files':items}
(ROOT/'MANIFEST.json').write_text(json.dumps(manifest,indent=2)+'\n')
print(f'Wrote MANIFEST.json with {len(items)} files.')
