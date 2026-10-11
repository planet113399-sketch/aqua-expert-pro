import sqlite3

def init_and_fill_db():
    conn = sqlite3.connect('agro_knowledge.db')
    cursor = conn.cursor()
    
    # Структура таблицы с поддержкой двух языков
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
            '• <i>Базилик (зеленый/фиолетовый):</i> pH 5.8–6.2 | EC 1.2–1.6 mS/cm | Температура раствора не ниже +18°C.<br>'
            '• <i>Чеснок и Лук:</i> pH 6.0–6.8 | EC 1.2–1.8 mS/cm | N:120, P:40, K:160, Ca:110, Mg:35 ppm.<br><br>'
            '<b>2. Агротехника и Био-стимуляция:</b><br>'
            '• <i>Микоризация:</i> Обработка Glomus intraradices перед посадкой развивает корневую систему в 2–2.5 раза.<br>'
            '• <i>Ускорение срезки:</i> L-аминокислоты + экстракт Ascophyllum nodosum ускоряют созревание на 5–7 дней.<br><br>'
            '<b>3. Биологическая защита без периода ожидания (USDA Organic):</b><br>'
            '• <i>Пероноспороз и Альтернариоз:</i> Bacillus subtilis (26Д) — 2–3 л/га.<br>'
            '• <i>Тля, Луковая муха и Трипс:</i> Эмульсия масла Нима (0.5%) + зеленое мыло.',
            
            '<b>1. Nutrient Regimes & Parameters (Drip / NFT / Soil):</b><br>'
            '• <i>Dill, Parsley, Cilantro, Celery:</i> pH 5.8–6.4 | EC 1.0–1.5 mS/cm | N:110, P:30, K:150, Ca:100, Mg:30 ppm.<br>'
            '• <i>Basil (Green/Purple):</i> pH 5.8–6.2 | EC 1.2–1.6 mS/cm | Root solution temp > +18°C.<br>'
            '• <i>Garlic & Onion:</i> pH 6.0–6.8 | EC 1.2–1.8 mS/cm | N:120, P:40, K:160, Ca:110, Mg:35 ppm.<br><br>'
            '<b>2. Agronomy & Bio-Stimulation:</b><br>'
            '• <i>Mycorrhizal Inoculation:</i> Glomus intraradices expands root absorption area by 2–2.5x.<br>'
            '• <i>Herb Growth Acceleration:</i> Foliar L-amino acids + Ascophyllum nodosum advance harvest by 5–7 days.<br><br>'
            '<b>3. Zero-Days Harvest Waiting Bio-Protection (USDA Organic):</b><br>'
            '• <i>Downy Mildew & Alternaria:</i> Bacillus subtilis (26D) at 2–3 L/ha.<br>'
            '• <i>Aphids, Onion Fly & Thrips:</i> Neem Oil emulsion (0.5%) + potassium green soap.'
        ),
        (
            'stone_fruits',
            '🍒 Косточковые сады (Черешня, Персик, Нектарин, Слива, Урюк/Абрикос)',
            '🍒 Stone Fruit Orchards (Cherry, Peach, Nectarine, Plum, Apricot)',
            '<b>1. Гидродинамика и Питание по фазам:</b><br>'
            '• <i>Питательный профиль:</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Фаза цветения:</i> Внекорневой Хелат Бора (B) + Цинк (Zn) против осыпания завязи.<br>'
            '• <i>Налив плодов:</i> Увеличение доли Калия (K) в соотношении N:K = 1:1.8.<br>'
            '• <i>Вылив капельниц:</i> 40–60 л/дерево в сутки при температуре выше +32°C.<br><br>'
            '<b>2. Био-Защита (USDA Organic / GlobalGAP):</b><br>'
            '• <i>Монилиоз:</i> Bacillus subtilis в фазы «розовый бутон» и «падение лепестков».<br>'
            '• <i>Клястероспориоз и Коккомикоз:</i> Trichoderma harzianum капельно в прикорневую зону.<br>'
            '• <i>Вишневая муха и Тля:</i> Инсектицид Bacillus thuringiensis (БТБ) + трихограмма.',
            
            '<b>1. Irrigation Dynamics & Nutrition:</b><br>'
            '• <i>Nutrient Profile:</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Flowering:</i> Foliar Boron (B) + Zinc (Zn) chelates to prevent blossom drop.<br>'
            '• <i>Fruit Enlargement:</i> N:K ratio adjusted to 1:1.8 for sugar accumulation.<br>'
            '• <i>Drip Flow Rate:</i> 40–60 L/tree daily during peak summer (> +32°C).<br><br>'
            '<b>2. Organic Bio-Protection:</b><br>'
            '• <i>Monilinia Blight:</i> Bacillus subtilis sprays at pink bud and petal fall stages.<br>'
            '• <i>Shot Hole & Blight:</i> Trichoderma harzianum fertigation to root zone.<br>'
            '• <i>Cherry Fruit Fly & Aphids:</i> Bacillus thuringiensis (BTB) + beneficial insects.'
        ),
        (
            'nuts_orchards',
            '🌰 Орехоплодные сады (Фисташка, Миндаль, Грецкий орех, Фундук)',
            '🌰 Nut Orchards (Pistachio, Almond, Walnut, Hazelnut)',
            '<b>1. Климатические нормативы и Почвенные допуски:</b><br>'
            '• <i>Часы холода (Chilling Hours):</i> 700–1000 часов ниже +7°C.<br>'
            '• <i>Сумма эффективных температур (GDD):</i> 1800–2200°C для созревания ядра.<br>'
            '• <i>Солеустойчивость:</i> Пороговый EC почвенной вытяжки до 6.0 mS/cm.<br>'
            '• <i>Питательный профиль:</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br><br>'
            '<b>2. Офлайн Атлас Болезней и Био-Контроль:</b><br>'
            '• <i>Вертициллезное увядание:</i> Капельный пролив Trichoderma harzianum (10–15 кг/га).<br>'
            '• <i>Фисташковая медяница и Тля:</i> Масло Нима (0.8%) + опрыскивание био-инсектицидом БТБ.<br>'
            '• <i>Альтернариоз и Септориоз:</i> Bacillus subtilis (26Д) + калийный гумат.',
            
            '<b>1. Climate Thresholds & Soil Tolerances:</b><br>'
            '• <i>Chilling Hours:</i> 700–1000 hours below +7°C.<br>'
            '• <i>Growing Degree Days (GDD):</i> 1800–2200°C required for kernel fill.<br>'
            '• <i>Salinity Tolerance:</i> Soil extract EC threshold up to 6.0 mS/cm.<br>'
            '• <i>Nutrient Profile:</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | N:140, P:45, K:210, Ca:160, Mg:50 ppm.<br><br>'
            '<b>2. Disease Atlas & Bio-Control Protocol:</b><br>'
            '• <i>Verticillium Wilt:</i> Trichoderma harzianum fertigation (10–15 kg/ha).<br>'
            '• <i>Pistachio Psylla & Aphids:</i> Cold-pressed Neem Oil (0.8%) + Bacillus thuringiensis spray.<br>'
            '• <i>Alternaria & Septoria:</i> Foliar Bacillus subtilis (26D) + potassium humate.'
        ),
        (
            'subtropical_fruits',
            '🍊 Субтропические культуры (Гранат, Олива, Инжир, Хурма)',
            '🍊 Subtropical Crops (Pomegranate, Olive, Fig, Persimmon)',
            '<b>1. Полив и Предотвращение Растрескивания:</b><br>'
            '• <i>Гранат:</i> Потребность в GDD > 3000°C. Равномерный капельный полив без перепадов.<br>'
            '• <i>Профилактика растрескивания:</i> Хелат Кальция (Ca-EDTA) в корень + внекорневой кальций с аминокислотами.<br>'
            '• <i>Питательный профиль:</i> pH 6.2–7.2 | EC 1.8–2.5 mS/cm | N:130, P:50, K:220, Ca:150, Mg:55 ppm.<br><br>'
            '<b>2. Экологическая Защита:</b><br>'
            '• <i>Гранатовая плодожорка:</i> Выпуск трихограммы (Trichogramma) + инсектицид БТБ.<br>'
            '• <i>Антракноз и Пятнистость Оливы:</i> Bacillus subtilis + экстракт морских водорослей.',
            
            '<b>1. Irrigation & Cracking Prevention:</b><br>'
            '• <i>Pomegranate:</i> Requires GDD > 3000°C. Steady drip irrigation.<br>'
            '• <i>Fruit Split Prevention:</i> Root Calcium Chelate (Ca-EDTA) + foliar Calcium in July–August.<br>'
            '• <i>Nutrient Profile:</i> pH 6.2–7.2 | EC 1.8–2.5 mS/cm | N:130, P:50, K:220, Ca:150, Mg:55 ppm.<br><br>'
            '<b>2. Ecological Protection:</b><br>'
            '• <i>Pomegranate Moth:</i> Trichogramma releases + Bacillus thuringiensis sprays.<br>'
            '• <i>Anthracnose & Olive Spot:</i> Bio-fungicide Bacillus subtilis + Ascophyllum nodosum.'
        ),
        (
            'berries_grapes',
            '🍇 Ягодные культуры и Виноград (Клубника, Голубика, Малина, Виноград)',
            '🍇 Berry Crops & Vineyards (Strawberry, Blueberry, Raspberry, Grape)',
            '<b>1. Стандарты Выращивания (Drip / NFT / Субстрат):</b><br>'
            '• <i>Клубника:</i> pH 5.5–6.2 | EC 1.2–1.6 mS/cm | Чувствительность к натрию (Na < 1.0 ммоль/л).<br>'
            '• <i>Голубика высокорослая:</i> pH 4.2–4.8 | EC 1.0–1.4 mS/cm | Подкисление элементарной серой.<br>'
            '• <i>Виноград:</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | Регулируемый дефицит полива (RDI) перед сбором.<br><br>'
            '<b>2. Био-Защита от Оидиума, Милдью и Серой Гнили:</b><br>'
            '• <i>Оидиум Винограда:</i> Ampelomyces quisqualis / калийное мыло.<br>'
            '• <i>Милдью Винограда:</i> Опрыскивание Bacillus amyloliquefaciens.<br>'
            '• <i>Серая гниль (Botrytis):</i> Trichoderma harzianum по цветкам и ягодам.',
            
            '<b>1. Production Standards (Drip / NFT / Substrate):</b><br>'
            '• <i>Strawberry:</i> pH 5.5–6.2 | EC 1.2–1.6 mS/cm | Sodium limit (Na < 1.0 mmol/L).<br>'
            '• <i>Highbush Blueberry:</i> pH 4.2–4.8 | EC 1.0–1.4 mS/cm | Acidified via Elemental Sulfur.<br>'
            '• <i>Grapes:</i> pH 6.0–6.8 | EC 1.5–2.2 mS/cm | Regulated Deficit Irrigation (RDI).<br><br>'
            '<b>2. Disease Bio-Control:</b><br>'
            '• <i>Grape Powdery Mildew:</i> Ampelomyces quisqualis / potassium soap.<br>'
            '• <i>Grape Downy Mildew:</i> Bacillus amyloliquefaciens sprays.<br>'
            '• <i>Grey Mould (Botrytis):</i> Trichoderma harzianum bloom and set applications.'
        ),
        (
            'vegetables_solanaceous',
            '🍅 Пасленовые и Тыквенные культуры (Томат, Перец, Баклажан, Огурец)',
            '🍅 Solanaceous & Cucurbit Vegetables (Tomato, Pepper, Eggplant, Cucumber)',
            '<b>1. Гидропоника и Капельные Рецептуры:</b><br>'
            '• <i>Томат и Перец:</i> pH 5.6–6.3 | EC 2.0–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Огурец:</i> pH 5.5–6.0 | EC 1.8–2.4 mS/cm | N:180, P:45, K:220, Ca:150, Mg:50 ppm.<br><br>'
            '<b>2. Диагностика и Био-Контроль Вредителей:</b><br>'
            '• <i>Верхушечная гниль:</i> Листовой Хелат Кальция + стабилизация EC.<br>'
            '• <i>Энтомофаги:</i> Encarsia formosa против Белокрылки; Phytoseiulus persimilis против Паутинного клеща.',
            
            '<b>1. Hydroponics & Fertigation Formulations:</b><br>'
            '• <i>Tomato & Pepper:</i> pH 5.6–6.3 | EC 2.0–3.2 mS/cm | N:160, P:50, K:240, Ca:180, Mg:60 ppm.<br>'
            '• <i>Cucumber:</i> pH 5.5–6.0 | EC 1.8–2.4 mS/cm | N:180, P:45, K:220, Ca:150, Mg:50 ppm.<br><br>'
            '<b>2. Diagnostics & Biological Control:</b><br>'
            '• <i>Blossom End Rot:</i> Foliar Calcium Chelate + EC stabilization.<br>'
            '• <i>Beneficial Insects:</i> Encarsia formosa for Whitefly; Phytoseiulus persimilis for Spider Mites.'
        ),
        (
            'field_crops',
            '🌾 Полевые, Зерновые и Масличные культуры (Пшеница, Кукуруза, Нут, Подсолнечник, Рапс)',
            '🌾 Field Crops, Grains & Oilseeds (Wheat, Corn, Chickpea, Sunflower, Rapeseed)',
            '<b>1. Биология питания и Азотофиксация:</b><br>'
            '• <i>Бобовые (Нут, Маш, Соя, Горох):</i> Инокуляция семян клубеньковыми бактериями (Mesorhizobium ciceri / Bradyrhizobium japonicum) обеспечивает фиксацию до 120–160 кг N/га из атмосферы.<br>'
            '• <i>Озимая Пшеница и Ячмень:</i> Дробное внесение азота по фазам Задокса (GS30-GS39). Листовая обработка гуматом калия + Цинк (Zn) в кущение.<br>'
            '• <i>Кукуруза и Подсолнечник:</i> Потребность в Боре (B) в фазу 6–8 листьев для формирования корзинок и початка.<br><br>'
            '<b>2. Сидерация и Биологическое Почвоведение (USDA Organic):</b><br>'
            '• <i>Покровные сидераты (Люцерна, Клевер, Вика, Горчица):</i> Заделка биомассы увеличивает содержание гумуса на 0.2–0.4% за сезон и подавляет нематод.<br>'
            '• <i>Биологическая защита зерновых:</i> Обработка семян и посевов Trichoderma harzianum + Pseudomonas fluorescens против корневых гнилей и фузариоза колоса.',
            
            '<b>1. Plant Nutrition & Atmospheric Nitrogen Fixation:</b><br>'
            '• <i>Legumes (Chickpea, Mungbean, Soy, Pea):</i> Seed inoculation with Mesorhizobium ciceri / Bradyrhizobium japonicum fixes 120–160 kg N/ha from the air.<br>'
            '• <i>Winter Wheat & Barley:</i> Split Nitrogen application aligned with Zadoks stages (GS30-GS39). Foliar Potassium Humate + Zinc (Zn) at tillering.<br>'
            '• <i>Corn & Sunflower:</i> Critical Boron (B) requirement at 6–8 leaf stage for flower head and ear development.<br><br>'
            '<b>2. Cover Crops & Biological Soil Health (USDA Organic):</b><br>'
            '• <i>Green Manure Crops (Alfalfa, Clover, Vetch, Mustard):</i> Incorporating biomass increases humus by 0.2–0.4% annually and suppresses nematodes.<br>'
            '• <i>Grain Biological Protection:</i> Seed treatment with Trichoderma harzianum + Pseudomonas fluorescens against root rot and Fusarium head blight.'
        )
    ]
    
    cursor.executemany('INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()
    print("Бэкенд БД успешно обновлен! Добавлены Полевые, Зерновые и Сидеральные культуры на RU и EN!")

if __name__ == '__main__':
    init_and_fill_db()
