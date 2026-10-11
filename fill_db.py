import sqlite3

def init_and_fill_db():
    conn = sqlite3.connect('agro_knowledge.db')
    cursor = conn.cursor()
    
    # Создание структуры таблицы с поддержкой двух языков
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
    
    data = [
        (
            'hydroponics',
            '💧 1. Инженерная Гидропоника и Капельный Полив',
            '💧 1. Advanced Hydroponics & Drip Irrigation',
            '<b>Международные стандарты pH, EC и макроэлементов (ppm / мг/л):</b><br>'
            '• <i>Зеленные и Пряные (Укроп, Петрушка, Базилик, Кинза, Сельдерей):</i> pH 5.8–6.4 | EC 1.0–1.6 mS/cm | N:110, P:30, K:150, Ca:100, Mg:30 ppm.<br>'
            '• <i>Лук и Чеснок (Drip/Грунт):</i> pH 6.0–6.8 | EC 1.2–1.8 mS/cm | N:120, P:40, K:160, Ca:110, Mg:35 ppm.<br>'
            '• <i>Пасленовые (Томат, Перец, Баклажан):</i> pH 5.6–6.3 | EC 2.0–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Косточковые (Черешня, Персик, Слива, Урюк/Абрикос):</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Орехоплодные (Фисташка, Миндаль, Грецкий орех):</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br>'
            '• <i>Ягодники (Клубника NFT/Drip, Малина, Виноград):</i> pH 5.5–6.2 (Голубика pH 4.2–4.8) | EC 1.2–1.6 mS/cm.<br><br>'
            '<b>Экологическая очистка капельных линий:</b> 0.2% перекись водорода (H₂O₂) под давлением 2.5 бар.',
            
            '<b>International Standards for pH, EC and Nutrients (ppm / mg/L):</b><br>'
            '• <i>Herbs & Alliums (Dill, Parsley, Basil, Cilantro, Garlic, Onion):</i> pH 5.8–6.4 | EC 1.0–1.6 mS/cm | N:110, P:30, K:150, Ca:100, Mg:30 ppm.<br>'
            '• <i>Solanaceous (Tomato, Pepper, Eggplant):</i> pH 5.6–6.3 | EC 2.0–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Stone Fruits (Cherry, Peach, Plum, Apricot):</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Nuts (Pistachio, Almond, Walnut):</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br>'
            '• <i>Berries (Strawberry NFT/Drip, Blueberry, Grape):</i> pH 5.5–6.2 (Blueberry pH 4.2–4.8) | EC 1.2–1.6 mS/cm.<br><br>'
            '<b>Eco System Flush:</b> 0.2% Hydrogen Peroxide (H₂O₂) at 2.5 bar pressure.'
        ),
        (
            'drones',
            '🛸 2. Дроны и Агро-Мониторинг (Зелень, Овощи, Сады)',
            '🛸 2. Drones & Precision Ag (Herbs, Vegetables, Orchards)',
            '<b>Научно подтвержденные индексы вегетации (2025–2026):</b><br>'
            '• <i>MSAVI2:</i> Минимизирует влияние почвенного фона на всходах укропа, петрушки, чеснока и лука.<br>'
            '• <i>NDVI (0.7–0.88):</i> Мониторинг биомассы овощных и садовых культур.<br>'
            '• <i>NDRE (Red Edge):</i> Выявление азотного голодания на плотных кронах косточковых и орехоплодных садов.<br><br>'
            '<b>Ультрамалообъемное распыление (ULV/УМО):</b> Расход 8–12 л/га, размер капли 130–180 мкм для биопрепаратов.',
            
            '<b>Validated Vegetation Indices (2025–2026):</b><br>'
            '• <i>MSAVI2:</i> Minimizes soil background interference in dill, parsley, garlic and onion sprouts.<br>'
            '• <i>NDVI (0.7–0.88):</i> Photosynthetic biomass evaluation in vegetables and orchards.<br>'
            '• <i>NDRE (Red Edge):</i> Early nitrogen deficiency detection in fruit and nut canopies.<br><br>'
            '<b>ULV Spraying:</b> 8–12 L/ha, 130–180 µm droplet size preserving live bio-agents.'
        ),
        (
            'agrochemistry',
            '🌿 3. Экологическая Агрохимия и Био-Защита Зелени и Овощей',
            '🌿 3. Ecological Protection for Herbs & Vegetables',
            '<b>Протоколы USDA Organic / GlobalGAP без периода ожидания:</b><br>'
            '• <i>Зеленные культуры (Укроп, Петрушка, Базилик, Кинза):</i> Против пероноспороза и мучнистой росы — Bacillus subtilis (26Д). Против тли и трипса — Масло Нима (0.5%) + калийное мыло (без химии, срезка безопасна).<br>'
            '• <i>Чеснок и Лук:</i> Замочка зубочков и капельный полив Trichoderma harzianum против фузариозной и шейковой гнили.<br>'
            '• <i>Томат, Перец, Огурец:</i> Био-контроль белокрылки и клеща энтомофагами (Encarsia formosa, Phytoseiulus persimilis).<br>'
            '• <i>Косточковые & Орехоплодные сады:</i> Профилактика монилиоза, клястероспориоза и парши бактериальными липопептидами.',
            
            '<b>Zero-Days Waiting USDA Organic Protocols:</b><br>'
            '• <i>Herbs (Dill, Parsley, Basil, Cilantro):</i> Downy mildew control via Bacillus subtilis. Aphids/Thrips control via Cold-pressed Neem Oil (0.5%) + Green Soap.<br>'
            '• <i>Garlic & Onion:</i> Clove soaking and drip fertigation with Trichoderma harzianum against Fusarium and Neck Rot.<br>'
            '• <i>Tomato, Pepper, Cucumber:</i> Biological control of Whitefly and Spider Mites using beneficial insects (Encarsia, Phytoseiulus).<br>'
            '• <i>Orchards:</i> Monilinia, Scab and Bacterial spot suppression via lipopeptide bio-fungicides.'
        ),
        (
            'diagnostics',
            '🔬 4. Определитель Болезней и Атлас Симптомов',
            '🔬 4. Diagnostics Atlas & Nutrient Deficiencies',
            '<b>Диагностика дефицитов и патогенов овощей, зелени и садов:</b><br>'
            '• <i>Верхушечная гниль томата/перца:</i> Нарушение усвоения Кальция (Ca) из-за высокой температуры или скачков EC. Решение: листовой Хелат Кальция + стабилизация полива.<br>'
            '• <i>Пероноспороз (Ложная мучнистая роса лука/чеснока/укропа):</i> Пожелтение и отмирание пера. Решение: опрыскивание Bacillus subtilis + аминокислоты.<br>'
            '• <i>Краевой ожог (Все культуры):</i> Дефицит Калия (K) или EC > 3.2 mS/cm. Решение: промывка линии + калийный гумат.<br>'
            '• <i>Межжилковый хлороз:</i> Дефицит Железа (Fe) при pH > 7.6. Решение: Хелат Железа (Fe-EDDHA) в корень.',
            
            '<b>Nutrient & Pathogen Diagnostics for Herbs, Vegetables & Orchards:</b><br>'
            '• <i>Blossom End Rot (Tomato/Pepper):</i> Calcium (Ca) uptake breakdown caused by heat or EC spikes. Action: Foliar Calcium Chelate + irrigation stabilization.<br>'
            '• <i>Downy Mildew (Onion/Garlic/Dill):</i> Feather yellowing and tip necrosis. Action: Bacillus subtilis spray + amino acids.<br>'
            '• <i>Leaf Margin Necrosis:</i> Potassium (K) deficit or EC > 3.2 mS/cm. Action: Root flush + potassium humate.<br>'
            '• <i>Interveinal Chlorosis:</i> Iron (Fe) deficit at pH > 7.6. Action: Fe-EDDHA chelate via drip.'
        ),
        (
            'soil_gardening',
            '🌳 5. Почвоведение и Агротехника Садоводства и Овощеводства',
            '🌳 5. Soil Science & Herb/Vegetable Crop Management',
            '<b>Технологические карты выращивания (Стандарты 2026):</b><br>'
            '• <i>Чеснок & Лук:</i> Инокуляция микоризой Glomus intraradices для двукратного развития корней. Внесение серы (S) 40–60 кг/га для формирования эфирных масел и остроты.<br>'
            '• <i>Укроп, Петрушка, Базилик:</i> Грядовый посев, регулярный капельный вылив. Внекорневые аминокислотные стимуляторы ускоритель срезки на 5–7 дней.<br>'
            '• <i>Косточковые (Черешня, Персик, Урюк):</i> Чашеобразная формировка кроны. Вылив 40–60 л/дерево в сутки. Капельный азотно-калийный баланс.<br>'
            '• <i>Орехоплодные (Фисташка, Миндаль):</i> Chilling Hours 700–1000 ч, GDD 1800–2200°C. Солеустойчивость до EC 6.0 mS/cm.',
            
            '<b>2026 Crop Production Protocols:</b><br>'
            '• <i>Garlic & Onion:</i> Mycorrhizal inoculation (Glomus intraradices) doubling root absorptive area. Elemental Sulfur (40–60 kg/ha) for pungency.<br>'
            '• <i>Dill, Parsley, Basil:</i> Raised bed drip system. Amino acid foliar biostimulants accelerating harvest readiness by 5–7 days.<br>'
            '• <i>Stone Fruits (Cherry, Peach, Apricot):</i> Open center pruning. Drip fertigation 40–60 L/tree daily. Balanced N-K ratio.<br>'
            '• <i>Nuts (Pistachio, Almond):</i> Chilling Hours 700–1000 h, GDD 1800–2200°C. Salt tolerance up to EC 6.0 mS/cm.'
        )
    ]
    
    cursor.executemany('INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()
    print("Бэкенд БД успешно обновлен! Заложены расширенные модули по Зелени, Овощам и Садам!")

if __name__ == '__main__':
    init_and_fill_db()
