import json
import os
import re

base_dir = '/home/antigravity/leorruas/puc'
bq_dir = os.path.join(base_dir, 'banco-de-questoes')

files = [
    '01.programacao-modular.json',
    '02.modelagem-de-dados.json',
    '03.manipulacao-de-dados-sql.json',
    '04.algoritmos-e-estruturas-de-dados.json',
    '05.desenvolvimento-web-back-end.json',
    '06.projeto-aplicacao-interativa.json',
    '07.engenharia-de-requisitos.json',
    '08.design-de-interacao.json',
    '09.redes-de-computadores.json',
    '10.lideranca-e-competencias.json',
    '11.desafios-contemporaneos.json'
]

# Emoji regex covering common unicode emoji ranges
emoji_pattern = re.compile(
    "["
    "\U0001F600-\U0001F64F"
    "\U0001F300-\U0001F5FF"
    "\U0001F680-\U0001F6FF"
    "\U0001F1E0-\U0001F1FF"
    "\U0001F900-\U0001F9FF"
    "\U0001FA00-\U0001FA6F"
    "\U0001FA70-\U0001FAFF"
    "\u2600-\u26FF"
    "\u2700-\u27BF"
    "]+",
    flags=re.UNICODE
)

all_questions = []
seen_ids = set()
missing_refs = []
emoji_hits = []

for fname in files:
    fpath = os.path.join(bq_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        raw_text = f.read()
        data = json.loads(raw_text)
    
    assert len(data) == 50, f"{fname} has {len(data)} questions instead of 50!"
    
    # Check emojis in raw text
    m = emoji_pattern.findall(raw_text)
    if m:
        emoji_hits.append((fname, m))
        
    for q in data:
        qid = q['id']
        assert qid not in seen_ids, f"Duplicate ID: {qid}"
        seen_ids.add(qid)
        
        assert q['dificuldade'] in ('facil', 'medio', 'dificil'), f"Invalid dificuldade in {qid}: {q['dificuldade']}"
        alts = q['alternativas']
        assert len(alts) == 4, f"{qid} does not have 4 alternatives"
        letters = [a['letra'] for a in alts]
        assert letters == ['A', 'B', 'C', 'D'], f"{qid} letters invalid: {letters}"
        corr_count = sum(1 for a in alts if a['correta'] is True)
        assert corr_count == 1, f"{qid} has {corr_count} correct answers"
        
        exp = q['explicacao']
        assert exp.get('modelo_mental'), f"{qid} missing modelo_mental"
        assert exp.get('analise_correta'), f"{qid} missing analise_correta"
        assert len(exp.get('distratores', {})) == 3, f"{qid} distratores len != 3"
        
        ref_vault = exp.get('referencia_vault', '')
        full_ref = os.path.join(base_dir, ref_vault)
        if not os.path.exists(full_ref):
            missing_refs.append((qid, ref_vault))
            
        all_questions.append(q)

print(f"Total questions validated across {len(files)} files: {len(all_questions)}")
print(f"Emoji hits: {emoji_hits}")
print(f"Missing vault references ({len(missing_refs)}):")
for qid, ref in missing_refs:
    print(f"  {qid}: {ref}")

if not missing_refs and not emoji_hits and len(all_questions) == 550:
    unified_path = os.path.join(bq_dir, 'questoes.json')
    with open(unified_path, 'w', encoding='utf-8') as f:
        json.dump(all_questions, f, ensure_ascii=False, indent=2)
    print(f"Successfully wrote 550 questions to {unified_path}")
