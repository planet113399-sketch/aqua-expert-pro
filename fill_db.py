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
            'herbs_alliums',
            '🥬 Зеленные, Пряные и Луковичные культуры (Укроп, Петрушка, Базилик, Чеснок, Лук)',
            '🥬 Herbs, Spices & Allium Crops (Dill, Parsley, Basil, Garlic, Onion)',
            '<b>1. Питательный режим и параметры (Drip / NFT / Грунт):</b><br>'
            '• <i>Укроп, Петрушка, Кинза, Сельдерей:</i> pH 5.8–6.4 | EC 1.0–1.5 mS/cm | N:110, P:30, K:150, Ca:100, Mg:30 ppm.<br>'
            '• <i>Базилик (зеленый/фиолетовый):</i> pH 5.8–6.2 | EC 1.2–1.6 mS/cm | Критичен к температуре раствора (не ниже +18°C).<br>'
            '• <i>Чеснок (озимый/яровой) и Лук:</i> pH 6.0–6.8 | EC 1.2–1.8 mS/cm | N:120, P:40, K:160, Ca:110, Mg:35 ppm.<br><br>'
            '<b>2. Агротехника и Био-стимуляция:</b><br>'
            '• <i>Инокуляция чеснока и лука:</i> Обработка микоризой (Glomus intraradices) перед посадкой увеличивает площадь всасывания корней в 2–2.5 раза.<br>'
            '• <i>Ускорение срезки зелени:</i> Листовые подкормки L-аминокислотами и экстрактом водорослей Ascophyllum nodosum ускоряют созревание на 5–7 дней.<br><br>'
            '<b>3. Биологическая защита без периода ожидания (USDA Organic):</b><br>'
            '• <i>Пероноспороз (Ложная мучнистая роса) и Альтернариоз:</i> Опрыскивание Bacillus subtilis (26Д) — 2–3 л/га.<br>'
            '• <i>Тля, Луковая муха и Трипс:</i> Эмульсия масла Нима (0.5%) + калийное зеленое мыло. Безопасно для сбора в день обработки.',
            
            '<b>1. Nutrient Regimes & Parameters (Drip / NFT / Soil):</b><br>'
            '• <i>Dill, Parsley, Cilantro, Celery:</i> pH 5.8–6.4 | EC 1.0–1.5 mS/cm | N:110, P:30, K:150, Ca:100, Mg:30 ppm.<br>'
            '• <i>Basil (Green/Purple):</i> pH 5.8–6.2 | EC 1.2–1.6 mS/cm | Requires root solution temp > +18°C.<br>'
            '• <i>Garlic & Onion:</i> pH 6.0–6.8 | EC 1.2–1.8 mS/cm | N:120, P:40, K:160, Ca:110, Mg:35 ppm.<br><br>'
            '<b>2. Agronomy & Bio-Stimulation:</b><br>'
            '• <i>Mycorrhizal Inoculation:</i> Treating garlic cloves with Glomus intraradices expands root absorption area by 2–2.5x.<br>'
            '• <i>Herb Growth Acceleration:</i> Foliar L-amino acids + Ascophyllum nodosum seaweed extract advance harvest readiness by 5–7 days.<br><br>'
            '<b>3. Zero-Days Harvest Waiting Bio-Protection (USDA Organic):</b><br>'
            '• <i>Downy Mildew & Alternaria:</i> Spraying Bacillus subtilis (26D) at 2–3 L/ha.<br>'
            '• <i>Aphids, Onion Fly & Thrips:</i> Cold-pressed Neem Oil emulsion (0.5%) + potassium green soap.'
        ),
        (
            'stone_fruits',
            '🍒 Косточковые сады (Черешня, Персик, Нектарин, Слива, Урюк/Абрикос)',
            '🍒 Stone Fruit Orchards (Cherry, Peach, Nectarine, Plum, Apricot)',
            '<b>1. Гидродинамика и Питание по фазам вегетации:</b><br>'
            '• <i>Питательный профиль:</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Фаза цветения и завязывания:</i> Внекорневой Хелат Бора (B) + Цинк (Zn) против осыпания завязи.<br>'
            '• <i>Налив плодов:</i> Увеличение доли Калия (K) в соотношении N:K = 1:1.8 для накопления сахаров и плотности мякоти.<br>'
            '• <i>Норма вылива капельниц:</i> 40–60 л/дерево в сутки при температуре выше +32°C.<br><br>'
            '<b>2. Молекулярная Био-Защита (USDA Organic / GlobalGAP):</b><br>'
            '• <i>Монилиоз (Монилинная гниль ветвей и плодов):</i> Профилактические обработки Bacillus subtilis в фазы «розовый бутон» и «падение лепестков».<br>'
            '• <i>Клястероспориоз (Дырчатая пятнистость) и Коккомикоз:</i> Капельное внесение Trichoderma harzianum в прикорневую зону.<br>'
            '• <i>Вишневая муха и Тля:</i> Бактериальный инсектицид Bacillus thuringiensis (БТБ) + заселение энтомофагов.',
            
            '<b>1. Irrigation Dynamics & Growth Stage Nutrition:</b><br>'
            '• <i>Nutrient Profile:</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Flowering & Fruit Set:</i> Foliar Boron (B) + Zinc (Zn) chelates to prevent blossom drop.<br>'
            '• <i>Fruit Enlargement:</i> Increase Potassium (K) ratio to N:K = 1:1.8 for sugar accumulation and firmness.<br>'
            '• <i>Drip Flow Rate:</i> 40–60 L/tree daily during peak summer (> +32°C).<br><br>'
            '<b>2. Organic Bio-Protection (USDA Organic / GlobalGAP):</b><br>'
            '• <i>Monilinia Blossom Blight & Fruit Rot:</i> Bacillus subtilis sprays at pink bud and petal fall stages.<br>'
            '• <i>Shot Hole (Clasterosporium) & Blight:</i> Trichoderma harzianum fertigation to root zone.<br>'
            '• <i>Cherry Fruit Fly & Aphids:</i> Bacillus thuringiensis (BTB) + beneficial insect releases.'
        ),
        (
            'nuts_orchards',
            '🌰 Орехоплодные сады (Фисташка, Миндаль, Грецкий орех, Фундук)',
            '🌰 Nut Orchards (Pistachio, Almond, Walnut, Hazelnut)',
            '<b>1. Климатические нормативы и Почвенные допуски:</b><br>'
            '• <i>Часы холода (Chilling Hours):</i> 700–1000 часов при температуре ниже +7°C для прохождения периода покоя.<br>'
            '• <i>Сумма эффективных температур (GDD):</i> 1800–2200°C для полного налива ядра и естественного раскрытия скорлупы.<br>'
            '• <i>Солеустойчивость:</i> Пороговый EC почвенной вытяжки до 6.0 mS/cm (высокая адаптивность фисташки к засоленным почвам).<br>'
            '• <i>Питательный профиль:</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br><br>'
            '<b>2. Офлайн Атлас Болезней и Био-Контроль:</b><br>'
            '• <i>Вертициллезное увядание (Verticillium dahliae):</i> Капельный пролив Trichoderma harzianum (10–15 кг/га) при прогреве почвы до +15°C.<br>'
            '• <i>Фисташковая медяница и Тля:</i> Холодный отжим масла Нима (0.8%) + опрыскивание био-инсектицидом БТБ.<br>'
            '• <i>Альтернариоз и Септориоз:</i> Листовые обработки Bacillus subtilis (штамм 26Д) с добавлением калийного гумата.',
            
            '<b>1. Climate Thresholds & Soil Tolerances:</b><br>'
            '• <i>Chilling Hours:</i> 700–1000 hours below +7°C to break bud dormancy.<br>'
            '• <i>Growing Degree Days (GDD):</i> 1800–2200°C required for full kernel fill and shell splitting.<br>'
            '• <i>Salinity Tolerance:</i> Soil extract EC threshold up to 6.0 mS/cm.<br>'
            '• <i>Nutrient Profile:</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br><br>'
            '<b>2. Disease Atlas & Bio-Control Protocol:</b><br>'
            '• <i>Verticillium Wilt (Verticillium dahliae):</i> Trichoderma harzianum fertigation (10–15 kg/ha) when soil reaches +15°C.<br>'
            '• <i>Pistachio Psylla & Aphids:</i> Cold-pressed Neem Oil (0.8%) + Bacillus thuringiensis spray.<br>'
            '• <i>Alternaria & Septoria Leaf Spot:</i> Foliar Bacillus subtilis (26D) + potassium humate.'
        ),
        (
            'subtropical_fruits',
            '🍊 Субтропические культуры (Гранат, Олива, Инжир, Хурма)',
            '🍊 Subtropical Crops (Pomegranate, Olive, Fig, Persimmon)',
            '<b>1. Полив и Предотвращение Растрескивания:</b><br>'
            '• <i>Гранат:</i> Потребность в GDD > 3000°C. Критически важен строго равномерный капельный полив (без резких сухих перерывов).<br>'
            '• <i>Профилактика растрескивания плодов:</i> Корневое внесение Хелата Кальция (Ca-EDTA) + внекорневые обработки кальцием с аминокислотами в период июль–август.<br>'
            '• <i>Питательный профиль:</i> pH 6.2–7.2 | EC 1.8–2.5 mS/cm | N:130, P:50, K:220, Ca:150, Mg:55 ppm.<br><br>'
            '<b>2. Экологическая Защита:</b><br>'
            '• <i>Гранатовая плодожорка и Чвец:</i> Выпуск трихограммы (Trichogramma) + бактериальный инсектицид БТБ.<br>'
            '• <i>Антракноз и Пятнистость Оливы:</i> Биологический фунгицид Bacillus subtilis + экстракт морских водорослей.',
            
            '<b>1. Irrigation & Cracking Prevention:</b><br>'
            '• <i>Pomegranate:</i> Requires GDD > 3000°C. Continuous, steady drip irrigation is required.<br>'
            '• <i>Fruit Split Prevention:</i> Root Calcium Chelate (Ca-EDTA) + foliar Calcium with amino acids in July–August.<br>'
            '• <i>Nutrient Profile:</i> pH 6.2–7.2 | EC 1.8–2.5 mS/cm | N:130, P:50, K:220, Ca:150, Mg:55 ppm.<br><br>'
            '<b>2. Ecological Protection:</b><br>'
            '• <i>Pomegranate Moth & Scale Insects:</i> Trichogramma releases + Bacillus thuringiensis (BTB) sprays.<br>'
            '• <i>Anthracnose & Olive Leaf Spot:</i> Bio-fungicide Bacillus subtilis + Ascophyllum nodosum extract.'
        ),
        (
            'berries_grapes',
            '🍇 Ягодные культуры и Виноград (Клубника, Голубика, Малина, Виноград)',
            '🍇 Berry Crops & Vineyards (Strawberry, Blueberry, Raspberry, Grape)',
            '<b>1. Стандарты Выращивания (Drip / NFT / Субстрат):</b><br>'
            '• <i>Клубника (Земляника садовая):</i> pH 5.5–6.2 | EC 1.2–1.6 mS/cm | Чувствительна к избытку натрия ($Na < 1.0$ ммоль/л).<br>'
            '• <i>Голубика высокорослая (Кислолюбивая):</i> pH 4.2–4.8 | EC 1.0–1.4 mS/cm | Корректоры: подкисление элементарной серой или ортофосфорной кислотой.<br>'
            '• <i>Виноград столовый и винный:</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | Техника регулируемого дефицита полива (RDI) перед сбором.<br><br>'
            '<b>2. Защита от Оидиума, Милдью и Серой Гнили:</b><br>'
            '• <i>Оидиум Винограда (Мучнистая роса):</i> Био-агент Ampelomyces quisqualis / калийное мыло.<br>'
            '• <i>Милдью Винограда:</i> Опрыскивание Bacillus amyloliquefaciens.<br>'
            '• <i>Серая гниль (Botrytis cinerea на Клубнике/Винограде):</i> Обработка Trichoderma harzianum по цветкам и ягодам.',
            
            '<b>1. Production Standards (Drip / NFT / Substrate):</b><br>'
            '• <i>Strawberry:</i> pH 5.5–6.2 | EC 1.2–1.6 mS/cm | Highly sensitive to Sodium ($Na < 1.0$ mmol/L).<br>'
            '• <i>Highbush Blueberry (Acidophilic):</i> pH 4.2–4.8 | EC 1.0–1.4 mS/cm | Acidified via Elemental Sulfur or Phosphoric Acid.<br>'
            '• <i>Table & Wine Grapes:</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | Regulated Deficit Irrigation (RDI) before harvest.<br><br>'
            '<b>2. Powdery Mildew, Downy Mildew & Botrytis Bio-Control:</b><br>'
            '• <i>Grape Powdery Mildew (Uncinula necator):</i> Bio-agent Ampelomyces quisqualis / potassium soap.<br>'
            '• <i>Grape Downy Mildew (Plasmopara viticola):</i> Bacillus amyloliquefaciens sprays.<br>'
            '• <i>Grey Mould (Botrytis cinerea on Strawberry/Grape):</i> Trichoderma harzianum applications during bloom and fruit set.'
        ),
        (
            'vegetables_solanaceous',
            '🍅 Пасленовые и Тыквенные овощные культуры (Томат, Перец, Баклажан, Огурец)',
            '🍅 Solanaceous & Cucurbit Vegetables (Tomato, Pepper, Eggplant, Cucumber)',
            '<b>1. Гидропоника и Капельные Рецептуры:</b><br>'
            '• <i>Томат и Перец:</i> pH 5.6–6.3 | EC 2.0–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Огурец (высокая вегетативная скорость):</i> pH 5.5–6.0 | EC 1.8–2.4 mS/cm | N:180, P:45, K:220, Ca:150, Mg:50 ppm.<br><br>'
            '<b>2. Диагностика и Борьба с Вредителями:</b><br>'
            '• <i>Верхушечная гниль томата/перца:</i> Блокировка Кальция из-за жары. Решение: листовой Хелат Кальция + стабилизация EC.<br>'
            '• <i>Био-контроль в закрытом и открытом грунте:</i> Против Белокрылки — энтомофаг Encarsia formosa. Против Паутинного клеща — хищный клещ Phytoseiulus persimilis.',
            
            '<b>1. Hydroponics & Fertigation Formulations:</b><br>'
            '• <i>Tomato & Pepper:</i> pH 5.6–6.3 | EC 2.0–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Cucumber (High vegetative rate):</i> pH 5.5–6.0 | EC 1.8–2.4 mS/cm | N:180, P:45, K:220, Ca:150, Mg:50 ppm.<br><br>'
            '<b>2. Diagnostics & Biological Pest Control:</b><br>'
            '• <i>Blossom End Rot:</i> Calcium blockage caused by heat spikes. Action: Foliar Calcium Chelate + EC stabilization.<br>'
            '• <i>Bio-Control Agents:</i> Encarsia formosa against Whitefly; Phytoseiulus persimilis against Spider Mites.'
        )
    ]
    
    cursor.executemany('INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()
    print("Бэкенд БД успешно обновлен! Структурированные категории культур заложены на RU и EN!")

if __name__ == '__main__':
    init_and_fill_db()
