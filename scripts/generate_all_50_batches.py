import json
import os

BASE_DIR = '/home/antigravity/leorruas/puc'
BANK_DIR = os.path.join(BASE_DIR, 'banco-de-questoes')

def make_alts(a_txt, b_txt, c_txt, d_txt, corr_idx, da, db, dc, dd):
    letters = ['A', 'B', 'C', 'D']
    texts = [a_txt, b_txt, c_txt, d_txt]
    diags = [da, db, dc, dd]
    alts = []
    distrators = {}
    for i in range(4):
        is_corr = (i == corr_idx)
        alts.append({
            'letra': letters[i],
            'texto': texts[i],
            'correta': is_corr,
            'diagnostico': diags[i]
        })
        if not is_corr:
            distrators[letters[i]] = diags[i]
    return alts, distrators

def create_discipline_pack(disc_id, disc_name, prefix, ref_folder, raw_items):
    questions = []
    for idx, item in enumerate(raw_items, 1):
        alts, distrators = make_alts(
            item['a'], item['b'], item['c'], item['d'],
            item['corr'], item['da'], item['db'], item['dc'], item['dd']
        )
        q_obj = {
            'id': f"{prefix}-{idx:03d}",
            'disciplina_id': disc_id,
            'disciplina': disc_name,
            'topico': item['topico'],
            'artigo_origem': item['artigo'],
            'dificuldade': item.get('dif', 'medio'),
            'enunciado': item['enunc'],
            'alternativas': alts,
            'explicacao': {
                'modelo_mental': item['feynman'],
                'analise_correta': item['analise'],
                'distratores': distrators,
                'referencia_vault': f"{ref_folder}/{item['artigo']}"
            }
        }
        questions.append(q_obj)
    return questions

print("Módulo de automação de lotes pronto.")
