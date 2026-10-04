import json
from pathlib import Path

pasta = Path(__file__).parent
modelo = (pasta / 'dash_tpl.html').read_text(encoding='utf-8')
dados = json.loads((pasta / 'dashboard_dados.json').read_text(encoding='utf-8'))
html = modelo.replace('__DATA__', json.dumps(dados, ensure_ascii=False, separators=(',', ':')))
(pasta / 'dashboard.html').write_text(html, encoding='utf-8')
print('dashboard.html gerado:', len(html) // 1024, 'KB')
