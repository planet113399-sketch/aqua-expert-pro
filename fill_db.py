import sqlite3

def init_and_fill_db():
    conn = sqlite3.connect('agro_knowledge.db')
    cursor = conn.cursor()
    
    # Структура базы данных с поддержкой двух языков
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
    
    # Очистка таблицы перед перезаписью актуального массива
    cursor.execute('DELETE FROM knowledge')
    
    # ПОЛНЫЙ НАУЧНЫЙ МАССИВ ПО 5 БАЗОВЫМ НИШАМ (USDA ORGANIC / GLOBALGAP 2026)
    data = [
        (
            'hydroponics',
            '💧 1. Гидропоника и Капельный полив',
            '💧 1. Advanced Hydroponics & Drip Irrigation',
            '<b>1. Академический реестр норм pH, EC и макроэлементов (ppm / мг/л):</b><br>'
            '• <i>Орехоплодные (Фисташка, Миндаль, Грецкий орех, Фундук):</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br>'
            '• <i>Косточковые (Черешня, Персик, Слива, Абрикос/Урюк):</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Семечковые и Субтропики (Яблоня, Груша, Гранат, Олива, Инжир):</i> pH 6.0–7.2 | EC 1.2–2.5 mS/cm.<br>'
            '• <i>Ягодники (Клубника Drip/NFT, Голубика, Виноград):</i> pH 5.5–6.2 (Голубика pH 4.2–4.8) | EC 1.2–1.8 mS/cm.<br>'
            '• <i>Овощные (Томат, Перец, Баклажан, Огурец):</i> pH 5.6–6.3 | EC 1.8–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Зеленные и Пряные (Укроп, Петрушка, Базилик, Чеснок, Лук):</i> pH 5.8–6.4 | EC 1.0–1.6 mS/cm.<br><br>'
            '<b>2. Инженерные нормы вылива и обслуживание:</b><br>'
            '• <i>Вылив в садах:</i> 40–65 л/дерево в сутки при температуре выше +32°C.<br>'
            '• <i>Очистка капельниц:</i> Промывка 0.2% раствором перекиси водорода (H₂O₂) под давлением 2.5 бар.',
            
            '<b>1. International Standards for pH, EC and Nutrients (ppm / mg/L):</b><br>'
            '• <i>Nuts (Pistachio, Almond, Walnut, Hazelnut):</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br>'
            '• <i>Stone Fruits (Cherry, Peach, Plum, Apricot):</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Pome & Subtropical (Apple, Pear, Pomegranate, Olive, Fig):</i> pH 6.0–7.2 | EC 1.2–2.5 mS/cm.<br>'
            '• <i>Berries (Strawberry Drip/NFT, Blueberry, Grape):</i> pH 5.5–6.2 (Blueberry pH 4.2–4.8) | EC 1.2–1.8 mS/cm.<br>'
            '• <i>Vegetables (Tomato, Pepper, Eggplant, Cucumber):</i> pH 5.6–6.3 | EC 1.8–3.2 mS/cm.<br>'
            '• <i>Herbs & Alliums (Dill, Parsley, Basil, Garlic, Onion):</i> pH 5.8–6.4 | EC 1.0–1.6 mS/cm.<br><br>'
            '<b>2. Irrigation Flow Rates & Maintenance:</b><br>'
            '• <i>Orchard Drip Rate:</i> 40–65 L/tree daily during peak heat (>+32°C).<br>'
            '• <i>Drip Line Flushing:</i> 0.2% Hydrogen Peroxide (H₂O₂) flush at 2.5 bar pressure.'
        ),
        (
            'drones',
            '🛸 2. Дроны и Агро-Мониторинг',
            '🛸 2. Drones & Precision Ag',
            '<b>1. Спектральные вегетационные индексы (Precision Ag 2026):</b><br>'
            '• <i>NDVI (0.7–0.88):</i> Оценка уровня фотосинтетической активности и биомассы.<br>'
            '• <i>NDRE (Red Edge):</i> Выявление дефицита азота на густых кронах садов (фисташка, черешня, яблоня).<br>'
            '• <i>MSAVI2:</i> Исключает почвенный фон при съемке всходов чеснока, лука и зеленных культур.<br><br>'
            '<b>2. Ультрамалообъемное опрыскивание (ULV / УМО):</b><br>'
            '• Норма вылива рабочей жидкости: 8–12 л/га.<br>'
            '• Размер капель (VMD): 130–180 мкм (сохраняет жизнеспособность спор биопрепаратов).',
            
            '<b>1. Validated Vegetation Indices (Precision Ag 2026):</b><br>'
            '• <i>NDVI (0.7–0.88):</i> Photosynthetic activity and canopy density evaluation.<br>'
            '• <i>NDRE (Red Edge):</i> Early nitrogen deficit detection in dense tree canopies.<br>'
            '• <i>MSAVI2:</i> Minimizes soil background interference in young crops and garlic/herb sprouts.<br><br>'
            '<b>2. ULV Drone Spraying Protocol:</b><br>'
            '• Flow rate: 8–12 L/ha.<br>'
            '• Droplet size: 130–180 µm preserving live bio-agents.'
        ),
        (
            'agrochemistry',
            '🌿 3. Экологическая Агрохимия и Био-Защита',
            '🌿 3. Ecological Protection & Bio-Control',
            '<b>1. Регламенты биологической защиты (USDA Organic / GlobalGAP):</b><br>'
            '• <i>Грибковые болезни (Парша, Монилиоз, Оидиум, Пероноспороз):</i> Bacillus subtilis (26Д) / 2–3 л/га.<br>'
            '• <i>Корневые гнили и Вертициллез:</i> Trichoderma harzianum (10–15 кг/га капельно в корень).<br>'
            '• <i>Тля, Клещи, Медяница, Трипс:</i> Холодный отжим масла Нима (Азадирахтин 0.8%) + зеленое калийное мыло.<br>'
            '• <i>Плодожорки и Листовертки:</i> Инсектицид Bacillus thuringiensis (БТБ) + выпуск трихограммы.<br><br>'
            '<b>2. Особенности по культурам:</b><br>'
            '• <i>Зелень и Чеснок:</i> Нулевой период ожидания перед сбором урожая.<br>'
            '• <i>Гранат:</i> Профилактика растрескивания внекорневым Хелатом Кальция (Ca) + стабилизация полива.',
            
            '<b>1. Bio-Protection Protocols (USDA Organic / GlobalGAP):</b><br>'
            '• <i>Fungal Pathogens (Scab, Monilinia, Powdery/Downy Mildew):</i> Bacillus subtilis (26D) at 2–3 L/ha.<br>'
            '• <i>Root Rots & Verticillium Wilt:</i> Trichoderma harzianum fertigation (10–15 kg/ha).<br>'
            '• <i>Mites, Aphids, Thrips:</i> Cold-pressed Neem Oil (0.8% Azadirachtin) + green soap.<br>'
            '• <i>Fruit Moths:</i> Bacillus thuringiensis (BTB) + Trichogramma releases.<br><br>'
            '<b>2. Crop Specific Protocols:</b><br>'
            '• <i>Herbs & Garlic:</i> Zero-days waiting period before harvest.<br>'
            '• <i>Pomegranate:</i> Fruit split prevention via foliar Calcium Chelate + irrigation stabilization.'
        ),
        (
            'diagnostics',
            '🔬 4. Определитель Болезней и Атлас Симптомов',
            '🔬 4. Diagnostics Atlas & Nutrient Deficiencies',
            '<b>1. Дифференциальный атлас визуальной диагностики:</b><br>'
            '• <i>Краевой ожог (Все культуры):</i> Дефицит Калия (K) или засоление (EC > 3.2 mS/cm). Коррекция: промывка зоны корней + калийный гумат.<br>'
            '• <i>Межжилковый хлороз молодняка:</i> Дефицит Железа (Fe) при pH > 7.6. Коррекция: Хелат Железа (Fe-EDDHA) в корень.<br>'
            '• <i>Верхушечная гниль (Томат, Перец):</i> Блокировка Кальция (Ca). Коррекция: листовой Хелат Кальция.<br>'
            '• <i>Вертициллез усыхания ветвей (Сады):</i> Внесение Trichoderma harzianum (15 кг/га) + аминокислоты.<br>'
            '• <i>Растрескивание плодов (Гранат, Черешня):</i> Перепады влажности + дефицит Кальция.',
            
            '<b>1. Differential Visual Diagnostics Atlas:</b><br>'
            '• <i>Leaf Margin Necrosis:</i> Potassium (K) deficit or EC > 3.2 mS/cm. Action: root flush + potassium humate.<br>'
            '• <i>Interveinal Chlorosis:</i> Iron (Fe) deficit at pH > 7.6. Action: Fe-EDDHA chelate via drip.<br>'
            '• <i>Blossom End Rot (Tomato/Pepper):</i> Calcium (Ca) uptake breakdown. Action: Foliar Calcium Chelate.<br>'
            '• <i>Verticillium Wilt (Orchards):</i> Trichoderma harzianum root drench (15 kg/ha) + amino acids.<br>'
            '• <i>Fruit Cracking (Pomegranate/Cherry):</i> Moisture fluctuation + Calcium deficit.'
        ),
        (
            'soil_gardening',
            '🌳 5. Почвоведение и Садоводство',
            '🌳 5. Soil Science & Orchard Agronomy',
            '<b>1. Биология почв и Покровные культуры (2026):</b><br>'
            '• <i>Гумус и Биочар (Biochar):</i> Цель 3.5–5.0% органики. Внесение 10–15 т/га увеличивает влагоемкость почвы на 35%.<br>'
            '• <i>Расчелачивание почв (pH > 8.0):</i> Элементарная сера (S⁰) 200–400 кг/га.<br>'
            '• <i>Азотофиксация бобовыми (Нут, Маш, Люцерна, Клевер):</i> Связывают из воздуха до 150–180 кг N/га.<br><br>'
            '<b>2. Климатические нормы садов:</b><br>'
            '• <i>Фисташка и Миндаль:</i> Chilling Hours 700–1000 ч (<+7°C), GDD 1800–2200°C. Пороговый EC до 6.0 mS/cm.<br>'
            '• <i>Чеснок и Зелень:</i> Инокуляция микоризой Glomus intraradices для роста корневой системы в 2 раза.',
            
            '<b>1. Soil Biology & Cover Crops (2026 Standards):</b><br>'
            '• <i>Humus & Biochar:</i> Target 3.5–5.0% organic matter. 10–15 t/ha application boosts water capacity by 35%.<br>'
            '• <i>Alkaline Soil Correction (pH > 8.0):</i> Elemental sulfur (S⁰) 200–400 kg/ha.<br>'
            '• <i>Biological Nitrogen Fixation:</i> Cover crops (Legumes, Clover, Alfalfa) fix up to 150–180 kg N/ha.<br><br>'
            '<b>2. Orchard Climate Standards:</b><br>'
            '• <i>Pistachio & Almond:</i> Chilling Hours 700–1000 h (<+7°C), GDD 1800–2200°C. EC threshold up to 6.0 mS/cm.<br>'
            '• <i>Garlic & Herbs:</i> Mycorrhizal inoculation (Glomus intraradices) doubling root absorption.'
        )
    ]
    
    cursor.executemany('INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()
    print("Бэкенд обновлен! Все 5 ниш восстановлены и наполнены полными знаниями.")

if __name__ == '__main__':
    init_and_fill_db()
