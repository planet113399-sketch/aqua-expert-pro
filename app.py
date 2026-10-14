import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_NAME = 'agro_knowledge.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ЭНДПОИНТ ИЗВЛЕЧЕНИЯ ДАННЫХ ИЗ БАЗЫ
@app.route('/api/get_knowledge', methods=['GET'])
def get_knowledge():
    category = request.args.get('category', 'hydroponics')
    lang = request.args.get('lang', 'ru')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM knowledge WHERE category = ? ORDER BY id DESC LIMIT 1', (category,)).fetchone()
    conn.close()

    if row:
        title = row['title_ru'] if lang == 'ru' else row['title_en']
        content = row['content_ru'] if lang == 'ru' else row['content_en']
        return jsonify({'title': title, 'content': content})
    else:
        return jsonify({
            'title': 'База знаний' if lang == 'ru' else 'Knowledge Base',
            'content': '<p>Данные подгружаются из локального резерва...</p>'
        })

# ЭНДПОИНТ АВТО-СОХРАНЕНИЯ НОВЫХ ИИ-ОТВЕТОВ И ФОТО-ДИАГНОЗОВ В БЭКЕНД
@app.route('/api/save_knowledge', methods=['POST'])
def save_knowledge():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400

    category = data.get('category', 'diagnostics')
    title = data.get('title', 'Новая запись ИИ')
    content = data.get('content', '')
    lang = data.get('lang', 'ru')

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Автоматическая дозапись новой статьи в бэкенд без стирания старых
    if lang == 'ru':
        cursor.execute(
            'INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)',
            (category, title, title + " (EN)", content, content)
        )
    else:
        cursor.execute(
            'INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)',
            (category, title + " (RU)", title, content, content)
        )
        
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success', 'message': 'Успешно сохранено в бэкенд БД!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)import sqlite3
from flask import Flask, request, jsonify

app = Flask(__name__)

DB_NAME = 'agro_knowledge.db'

def get_db_connection():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn

# ЭНДПОИНТ ИЗВЛЕЧЕНИЯ ДАННЫХ ИЗ БАЗЫ
@app.route('/api/get_knowledge', methods=['GET'])
def get_knowledge():
    category = request.args.get('category', 'hydroponics')
    lang = request.args.get('lang', 'ru')
    
    conn = get_db_connection()
    cursor = conn.cursor()
    row = cursor.execute('SELECT * FROM knowledge WHERE category = ? ORDER BY id DESC LIMIT 1', (category,)).fetchone()
    conn.close()

    if row:
        title = row['title_ru'] if lang == 'ru' else row['title_en']
        content = row['content_ru'] if lang == 'ru' else row['content_en']
        return jsonify({'title': title, 'content': content})
    else:
        return jsonify({
            'title': 'База знаний' if lang == 'ru' else 'Knowledge Base',
            'content': '<p>Данные подгружаются из локального резерва...</p>'
        })

# ЭНДПОИНТ АВТО-СОХРАНЕНИЯ НОВЫХ ИИ-ОТВЕТОВ И ФОТО-ДИАГНОЗОВ В БЭКЕНД
@app.route('/api/save_knowledge', methods=['POST'])
def save_knowledge():
    data = request.get_json()
    if not data:
        return jsonify({'status': 'error', 'message': 'No data provided'}), 400

    category = data.get('category', 'diagnostics')
    title = data.get('title', 'Новая запись ИИ')
    content = data.get('content', '')
    lang = data.get('lang', 'ru')

    conn = get_db_connection()
    cursor = conn.cursor()
    
    # Автоматическая дозапись новой статьи в бэкенд без стирания старых
    if lang == 'ru':
        cursor.execute(
            'INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)',
            (category, title, title + " (EN)", content, content)
        )
    else:
        cursor.execute(
            'INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)',
            (category, title + " (RU)", title, content, content)
        )
        
    conn.commit()
    conn.close()
    
    return jsonify({'status': 'success', 'message': 'Успешно сохранено в бэкенд БД!'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
