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
    
    cursor.execute('DELETE FROM knowledge')
    
    # ПОЛНЫЙ НАУЧНЫЙ МАССИВ ДАННЫХ БЭКЕНДА (USDA ORGANIC / GLOBALGAP 2026)
    data = [
        (
            'hydroponics',
            '💧 1. Гидропоника и Капельный полив',
            '💧 1. Advanced Hydroponics & Drip Irrigation',
            '<b>1. Академический реестр норм pH, EC и макроэлементов (ppm / мг/л):</b><br>'
            '• <i>Орехоплодные (Фисташка, Миндаль, Грецкий орех, Фундук):</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br>'
            '• <i>Косточковые (Черешня, Персик, Слива, Абрикос/Урюк):</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Семечковые и Субтропики (Яблоня, Груша, Гранат, Олива, Инжир, Хурма):</i> pH 6.0–7.2 | EC 1.2–2.5 mS/cm | N:130, P:45, K:200, Ca:150, Mg:50 ppm.<br>'
            '• <i>Ягодники (Клубника Drip/NFT, Голубика, Виноград):</i> pH 5.5–6.2 (Голубика pH 4.2–4.8) | EC 1.2–1.8 mS/cm.<br>'
            '• <i>Овощные (Томат, Перец, Баклажан, Огурец):</i> pH 5.6–6.3 | EC 1.8–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Зеленные и Пряные (Укроп, Петрушка, Базилик, Чеснок, Лук, Кинза):</i> pH 5.8–6.4 | EC 1.0–1.6 mS/cm | N:110, P:30, K:150, Ca:100, Mg:30 ppm.<br><br>'
            '<b>2. Инженерные нормы вылива и нейтрализация буфера:</b><br>'
            '• <i>Вылив в садах:</i> 40–65 л/дерево в сутки при температуре выше +32°C.<br>'
            '• <i>Коррекция бикарбонатов (HCO₃⁻ > 1.5 ммоль/л):</i> Закисление пищевой ортофосфорной (85%) или лимонной кислотой.<br>'
            '• <i>Промывка капельных линий:</i> 0.2% перекись водорода (H₂O₂) под давлением 2.5 бар от солей и биопленок.',
            
            '<b>1. International Standards for pH, EC and Nutrients (ppm / mg/L):</b><br>'
            '• <i>Nuts (Pistachio, Almond, Walnut, Hazelnut):</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br>'
            '• <i>Stone Fruits (Cherry, Peach, Plum, Apricot):</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Pome & Subtropical (Apple, Pear, Pomegranate, Olive, Fig):</i> pH 6.0–7.2 | EC 1.2–2.5 mS/cm.<br>'
            '• <i>Berries (Strawberry Drip/NFT, Blueberry, Grape):</i> pH 5.5–6.2 (Blueberry pH 4.2–4.8) | EC 1.2–1.8 mS/cm.<br>'
            '• <i>Vegetables (Tomato, Pepper, Eggplant, Cucumber):</i> pH 5.6–6.3 | EC 1.8–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Herbs & Alliums (Dill, Parsley, Basil, Garlic, Onion, Cilantro):</i> pH 5.8–6.4 | EC 1.0–1.6 mS/cm.<br><br>'
            '<b>2. Irrigation Engineering & Drip System Flushing:</b><br>'
            '• <i>Orchard Drip Rate:</i> 40–65 L/tree daily during peak summer (>+32°C).<br>'
            '• <i>Bicarbonate Neutralization:</i> Phosphoric (85%) or Citric acid acidification when HCO₃⁻ > 1.5 mmol/L.<br>'
            '• <i>Line Flush:</i> 0.2% Hydrogen Peroxide (H₂O₂) flush at 2.5 bar pressure.'
        ),
        (
            'drones',
            '🛸 2. Дроны и Агро-Мониторинг',
            '🛸 2. Drones & Precision Ag',
            '<b>1. Спектральные вегетационные индексы (Precision Ag 2026):</b><br>'
            '• <i>NDVI (0.7–0.88):</i> Оценка уровня фотосинтетической активности, биомассы и плотности кроны.<br>'
            '• <i>NDRE (Red Edge):</i> Выявление раннего дефицита азота на плотных кронах фруктовых и орехоплодных садов.<br>'
            '• <i>MSAVI2:</i> Исключает влияние почвенного фона при съемке молодых саженцев и всходов чеснока, лука и зелени.<br><br>'
            '<b>2. Ультрамалообъемное распыление (ULV / УМО) Агродронами:</b><br>'
            '• Норма вылива рабочей жидкости: 8–12 л/га (экономия воды до 90%).<br>'
            '• Размер капель (VMD): 130–180 мкм (обеспечивает полное покрытие и сохраняет живые споры биопрепаратов).',
            
            '<b>1. Validated Vegetation Indices (Precision Ag 2026):</b><br>'
            '• <i>NDVI (0.7–0.88):</i> Photosynthetic activity, biomass and canopy density evaluation.<br>'
            '• <i>NDRE (Red Edge):</i> Early nitrogen deficit detection in dense orchard canopies.<br>'
            '• <i>MSAVI2:</i> Minimizes soil background interference in young plantings and herb/garlic sprouts.<br><br>'
            '<b>2. ULV Drone Spraying Protocol:</b><br>'
            '• Flow rate: 8–12 L/ha (up to 90% water saving).<br>'
            '• Droplet size: 130–180 µm ensuring uniform coverage and live spore preservation.'
        ),
        (
            'agrochemistry',
            '🌿 3. Экологическая Агрохимия и Био-Защита',
            '🌿 3. Ecological Protection & Bio-Control',
            '<b>1. Молекулярные регламенты био-защиты (USDA Organic / GlobalGAP):</b><br>'
            '• <i>Бактериальные фунгициды:</i> Bacillus subtilis (26Д) вырабатывает суртины, блокирующие клеточную стенку грибов (Парша, Монилиоз, Оидиум, Пероноспороз). Норма: 2–3 л/га.<br>'
            '• <i>Прикорневые био-микромицеты:</i> Trichoderma harzianum блокирует мицелий Verticillium, Fusarium и Pythium (10–15 кг/га капельно).<br>'
            '• <i>Органические инсектициды:</i> Масло Нима (Азадирахтин 0.8%) + зеленое мыло нарушают гормональный цикл тли, клещей, медяницы и трипса.<br>'
            '• <i>Энтомопатогены:</i> Bacillus thuringiensis (БТБ) выделяет эндотоксин против плодожорок и гусениц.<br><br>'
            '<b>2. Регламент безопасного сбора:</b> Нулевой период ожидания для зеленных культур, чеснока и лука.',
            
            '<b>1. Molecular Bio-Protection Protocols (USDA Organic / GlobalGAP):</b><br>'
            '• <i>Bacterial Fungicides:</i> Bacillus subtilis (26D) produces lipopeptides inhibiting Scab, Monilinia, Powdery/Downy Mildew (2–3 L/ha).<br>'
            '• <i>Root Bio-Fungicides:</i> Trichoderma harzianum suppresses Verticillium, Fusarium and Pythium (10–15 kg/ha drip).<br>'
            '• <i>Organic Insecticides:</i> Cold-pressed Neem Oil (0.8% Azadirachtin) + green soap against mites, aphids, thrips and psylla.<br>'
            '• <i>Entomopathogens:</i> Bacillus thuringiensis (BTB) endotoxin against fruit moths.<br><br>'
            '<b>2. Harvest Waiting Protocol:</b> Zero-days waiting period for herbs, garlic and onions.'
        ),
        (
            'diagnostics',
            '🔬 4. Определитель Болезней и Атлас Симптомов',
            '🔬 4. Diagnostics Atlas & Nutrient Deficiencies',
            '<b>1. Дифференциальная визуальная диагностика:</b><br>'
            '• <i>Краевой ожог листьев:</i> Дефицит Калия (K) или засоление (EC > 3.2 mS/cm). Коррекция: промывка зоны корней + калийный гумат.<br>'
            '• <i>Межжилковый хлороз молодняка:</i> Дефицит Железа (Fe) при pH > 7.6. Коррекция: Хелат Железа (Fe-EDDHA) капельно.<br>'
            '• <i>Верхушечная гниль (Томат, Перец):</i> Блокировка Кальция (Ca). Коррекция: листовой Хелат Кальция + стабилизация EC.<br>'
            '• <i>Вертициллез усыхания ветвей (Сады):</i> Внесение Trichoderma harzianum (15 кг/га) + аминокислоты.<br>'
            '• <i>Растрескивание плодов (Гранат, Черешня):</i> Перепады полива + дефицит Кальция. Коррекция: листовой Хелат Кальция в фазу налива.',
            
            '<b>1. Differential Visual Diagnostics Atlas:</b><br>'
            '• <i>Leaf Margin Necrosis:</i> Potassium (K) deficit or EC > 3.2 mS/cm. Action: root flush + potassium humate.<br>'
            '• <i>Interveinal Chlorosis:</i> Iron (Fe) deficit at pH > 7.6. Action: Fe-EDDHA chelate via drip.<br>'
            '• <i>Blossom End Rot (Tomato/Pepper):</i> Calcium (Ca) uptake breakdown. Action: Foliar Calcium Chelate.<br>'
            '• <i>Verticillium Wilt (Orchards):</i> Trichoderma harzianum root drench (15 kg/ha) + amino acids.<br>'
            '• <i>Fruit Cracking (Pomegranate/Cherry):</i> Moisture fluctuation + Calcium deficit. Action: Foliar Calcium Chelate.'
        ),
        (
            'soil_gardening',
            '🌳 5. Почвоведение и Садоводство',
            '🌳 5. Soil Science & Orchard Agronomy',
            '<b>1. Биология почв и Покровные культуры (2026):</b><br>'
            '• <i>Гумус и Биочар (Biochar):</i> Цель 3.5–5.0% органики. Внесение 10–15 т/га увеличивает влагоемкость почвы на 35%.<br>'
            '• <i>Расчелачивание почв (pH > 8.0):</i> Элементарная сера (S⁰) 200–400 кг/га.<br>'
            '• <i>Азотофиксация бобовыми (Нут, Маш, Люцерна, Клевер, Вика):</i> Связывают из воздуха до 150–180 кг N/га в год.<br><br>'
            '<b>2. Агротехника садов и пряностей:</b><br>'
            '• <i>Фисташка и Миндаль:</i> Chilling Hours 700–1000 ч (<+7°C), GDD 1800–2200°C. Пороговый EC до 6.0 mS/cm.<br>'
            '• <i>Чеснок, Лук и Зелень:</i> Инокуляция микоризой Glomus intraradices для двукратного роста всасывающей поверхности корней.',
            
            '<b>1. Soil Biology & Cover Crops (2026 Standards):</b><br>'
            '• <i>Humus & Biochar:</i> Target 3.5–5.0% organic matter. 10–15 t/ha application boosts water capacity by 35%.<br>'
            '• <i>Alkaline Soil Correction (pH > 8.0):</i> Elemental sulfur (S⁰) 200–400 kg/ha.<br>'
            '• <i>Biological Nitrogen Fixation:</i> Cover crops (Legumes, Clover, Alfalfa, Vetch) fix up to 150–180 kg N/ha annually.<br><br>'
            '<b>2. Orchard & Herb Management:</b><br>'
            '• <i>Pistachio & Almond:</i> Chilling Hours 700–1000 h (<+7°C), GDD 1800–2200°C. EC threshold up to 6.0 mS/cm.<br>'
            '• <i>Garlic, Onion & Herbs:</i> Mycorrhizal inoculation (Glomus intraradices) doubling root absorptive area.'
        )
    ]
    
    cursor.executemany('INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()
    print("Бэкенд БАЗА ДАННЫХ успешно обновлена и наполнена глубокими академическими знаниями!")

if __name__ == '__main__':
    init_and_fill_db()
