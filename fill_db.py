import sqlite3

def init_and_fill_db():
    conn = sqlite3.connect('agro_knowledge.db')
    cursor = conn.cursor()
    
    # Структура базы данных с поддержкой двуязычия (RU / EN)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS knowledge (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            category TEXT NOT NULL,
            title_ru TEXT NOT NULL,
            title_en TEXT NOT NULL,
            content_ru TEXT NOT NULL,
            content_en TEXT NOT NULL
        )
    ''')
    
    cursor.execute('DELETE FROM knowledge')
    
    # НАУЧНО ПОДТВЕРЖДЕННЫЕ СТАНДАРТЫ (USDA ORGANIC / GLOBALGAP / EPPO 2025-2026)
    data = [
        (
            'hydroponics',
            '💧 1. Инженерная Гидропоника и Капельный Полив',
            '💧 1. Advanced Hydroponics & Drip Irrigation',
            '<b>Международные стандарты pH, EC и макроэлементов (ppm):</b><br>'
            '• <i>Косточковые (Черешня, Персик, Слива, Урюк/Абрикос):</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Орехоплодные (Фисташка, Миндаль, Грецкий орех, Фундук):</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br>'
            '• <i>Субтропические (Гранат, Олива, Инжир, Хурма):</i> pH 6.2–7.2 | EC 1.8–2.5 mS/cm | N:130, P:50, K:220, Ca:150, Mg:55 ppm.<br>'
            '• <i>Ягодники (Клубника NFT/Drip, Малина, Виноград):</i> pH 5.5–6.2 (Голубика pH 4.2–4.8) | EC 1.2–1.6 mS/cm.<br>'
            '• <i>Зеленные и Пряные (Укроп, Петрушка, Базилик, Чеснок, Лук):</i> pH 5.8–6.4 | EC 1.0–1.6 mS/cm.<br><br>'
            '<b>Очистка систем без химии:</b> Промывка 0.2% пероксидом водорода (H₂O₂) под давлением 2.5 бар для разрушения биопленок.',
            
            '<b>International Standards for pH, EC and Nutrients (ppm):</b><br>'
            '• <i>Stone Fruits (Cherry, Peach, Plum, Apricot):</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Nuts (Pistachio, Almond, Walnut, Hazelnut):</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br>'
            '• <i>Subtropical (Pomegranate, Olive, Fig, Persimmon):</i> pH 6.2–7.2 | EC 1.8–2.5 mS/cm.<br>'
            '• <i>Berries (Strawberry NFT/Drip, Raspberry, Grape):</i> pH 5.5–6.2 (Blueberry pH 4.2–4.8) | EC 1.2–1.6 mS/cm.<br>'
            '• <i>Herbs & Alliums (Dill, Parsley, Basil, Garlic, Onion):</i> pH 5.8–6.4 | EC 1.0–1.6 mS/cm.<br><br>'
            '<b>Eco System Cleaning:</b> 0.2% Hydrogen Peroxide (H₂O₂) flush at 2.5 bar pressure to remove biofilm.'
        ),
        (
            'drones',
            '🛸 2. Дроны и Точное Земледелие (Precision Ag)',
            '🛸 2. Drones & Precision Agriculture',
            '<b>Научно подтвержденные индексы вегетации:</b><br>'
            '• <i>NDVI (Normalized Difference Vegetation Index):</i> Диагностика облика биомассы (0.7–0.88 — норма активного фотосинтеза).<br>'
            '• <i>NDRE (Red Edge):</i> Выявление азотного голодания на плотных кронах деревьев (Фисташка, Черешня, Яблоня).<br>'
            '• <i>MSAVI2:</i> Исключает влияние почвенного фона на молодых посадках чеснока, зелени и саженцев.<br><br>'
            '<b>Ультрамалообъемное распыление (ULV/УМО):</b> Расход 8–12 л/га, размер капли 130–180 мкм для внесения живых биопрепаратов без сноса ветром.',
            
            '<b>Scientifically Validated Vegetation Indices:</b><br>'
            '• <i>NDVI:</i> Biomass photosynthetic activity evaluation (0.7–0.88 optimal range).<br>'
            '• <i>NDRE (Red Edge):</i> Nitrogen deficiency detection in dense tree canopies (Pistachio, Cherry, Apple).<br>'
            '• <i>MSAVI2:</i> Minimizes soil background interference in young crops and garlic/herb sprouts.<br><br>'
            '<b>ULV Drone Spraying:</b> 8–12 L/ha flow rate, 130–180 µm droplet size for live bio-agent preservation.'
        ),
        (
            'agrochemistry',
            '🌿 3. Экологическая Агрохимия и Молекулярная Био-Защита',
            '🌿 3. Ecological Agrochemistry & Bio-Control',
            '<b>Современный протокол USDA Organic / GlobalGAP:</b><br>'
            '• <i>Бактериальные фунгициды:</i> Bacillus subtilis (26Д) синтезирует липопептиды (суртины), разрушающие мицелий Парши, Монилиоза и Мучнистой росы.<br>'
            '• <i>Био-фунгициды корней:</i> Trichoderma harzianum блокирует Verticillium, Fusarium и Pythium (10–15 кг/га капельно).<br>'
            '• <i>Органические инсектициды:</i> Азадирахтин (Масло Нима 0.8%) + Зеленое мыло блокирует гормональный цикл клещей, тли и медяницы.<br>'
            '• <i>Энтомопатогены:</i> Bacillus thuringiensis (БТБ) выделяет дельта-эндотоксин против плодожорок и листоверток.',
            
            '<b>Modern USDA Organic / GlobalGAP Protocol:</b><br>'
            '• <i>Bacterial Fungicides:</i> Bacillus subtilis (26D) produces lipopeptides inhibiting Scab, Monilinia and Powdery Mildew.<br>'
            '• <i>Root Bio-Fungicides:</i> Trichoderma harzianum suppresses Verticillium, Fusarium and Pythium (10–15 kg/ha drip).<br>'
            '• <i>Organic Insecticides:</i> Cold-pressed Neem Oil (0.8% Azadirachtin) + Green Soap against mites, aphids and psylla.<br>'
            '• <i>Entomopathogens:</i> Bacillus thuringiensis (BTB) delta-endotoxin against fruit moths.'
        ),
        (
            'diagnostics',
            '🔬 4. Атлас Симптомов и Дефицитов Питания',
            '🔬 4. Symptom Atlas & Nutrient Deficiencies',
            '<b>Дифференциальная диагностика современных агрохолдингов:</b><br>'
            '• <i>Краевой ожог листьев:</i> Дефицит Калия (K) или EC > 3.2 mS/cm. Решение: промывка линии + калийный гумат.<br>'
            '• <i>Межжилковый хлороз:</i> Дефицит Железа (Fe) при pH > 7.6. Решение: Хелат Железа (Fe-EDDHA) капельно.<br>'
            '• <i>Вертициллезное увядание садов:</i> Полив Trichoderma harzianum (15 кг/га) + аминокислотный комплекс.<br>'
            '• <i>Растрескивание плодов (Гранат, Черешня):</i> Перепады полива + дефицит Кальция (Ca). Решение: листовой Хелат Кальция.',
            
            '<b>Modern Agronomy Differential Diagnostics:</b><br>'
            '• <i>Leaf Margin Necrosis:</i> Potassium (K) deficiency or EC > 3.2 mS/cm. Action: root flush + potassium humate.<br>'
            '• <i>Interveinal Chlorosis:</i> Iron (Fe) deficiency at pH > 7.6. Action: Drip Fe-EDDHA Chelate application.<br>'
            '• <i>Verticillium Wilt:</i> Root application of Trichoderma harzianum (15 kg/ha) + amino acids.<br>'
            '• <i>Fruit Cracking (Pomegranate, Cherry):</i> Irrigation fluctuation + Calcium (Ca) deficit. Action: Foliar Calcium Chelate.'
        ),
        (
            'soil_gardening',
            '🌳 5. Почвоведение и Агротехника Садоводства',
            '🌳 5. Soil Science & Commercial Orchard Management',
            '<b>Агрофизика и биология почв 2025–2026:</b><br>'
            '• <i>Гумус и Биочар (Biochar):</i> Цель 3.5–5.0% органики. Внесение 10–15 т/га увеличивает влагоемкость почвы на 35%.<br>'
            '• <i>Расчелачивание ($pH > 8.0$):</i> Элементарная сера ($S^0$) 200–400 кг/га. Окисление Thiobacillus снижает pH до 6.8.<br>'
            '• <i>Естественный азот:</i> Сидераты (Клевер, Люцерна, Вика) связывают из воздуха до 150–180 кг чистого N/га.<br>'
            '• <i>Фисташка & Миндаль:</i> Chilling Hours 700–1000 ч ($<+7^\\circ C$), GDD 1800–2200°C. Солеустойчивость до EC 6.0 mS/cm.',
            
            '<b>2025–2026 Soil Physics & Biology Standards:</b><br>'
            '• <i>Humus & Biochar:</i> Target 3.5–5.0% organic matter. 10–15 t/ha application boosts water holding capacity by 35%.<br>'
            '• <i>Alkaline Soil Correction ($pH > 8.0$):</i> Elemental sulfur ($S^0$) 200–400 kg/ha via Thiobacillus oxidation lowers pH to 6.8.<br>'
            '• <i>Natural Nitrogen:</i> Cover crops (Clover, Alfalfa, Vetch) fix up to 150–180 kg pure N/ha annually.<br>'
            '• <i>Pistachio & Almond:</i> Chilling Hours 700–1000 h ($<+7^\\circ C$), GDD 1800–2200°C. Salt tolerance up to EC 6.0 mS/cm.'
        )
    ]
    
    cursor.executemany('INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()
    print("Бэкенд БД успешно заполнен на 2-х языках (RU/EN) по стандартам 2026 года!")

if __name__ == '__main__':
    init_and_fill_db()
