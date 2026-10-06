import sqlite3
from flask import Flask, jsonify, render_template, request

app = Flask(__name__, template_folder='.')

def get_db_connection():
    conn = sqlite3.connect("agro_knowledge.db")
    # Настраиваем текстовое декодирование
    conn.text_factory = str
    conn.row_factory = sqlite3.Row
    return conn

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/api/search")
def search():
    query = request.args.get("q", "").strip()
    conn = get_db_connection()
    cursor = conn.cursor()

    # Извлекаем все данные из базы
    rows = cursor.execute("SELECT * FROM knowledge").fetchall()
    conn.close()

    results = []
    for row in rows:
        item = dict(row)
        
        name_ru = str(item.get("name_ru") or "")
        name_en = str(item.get("name_en") or "")
        desc_ru = str(item.get("description_ru") or "")
        desc_en = str(item.get("description_en") or "")
        cat = str(item.get("category") or "")

        # Если поиск пустой ИЛИ слово есть в любом из полей (без учета регистра Python)
        q_low = query.lower()
        if not query or (q_low in name_ru.lower() or q_low in name_en.lower() or q_low in desc_ru.lower() or q_low in desc_en.lower() or q_low in cat.lower()):
            results.append({
                "title": name_ru if name_ru else name_en,
                "title_en": name_en if name_en else name_ru,
                "content": desc_ru if desc_ru else desc_en,
                "content_en": desc_en if desc_en else desc_ru,
                "category": cat if cat else "Агрономия",
                "eppo_code": item.get("code_eppo", ""),
                "dosage": item.get("tank_mix_rule_ru", "")
            })

    return jsonify(results)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)