import sqlite3

def init_and_fill_db():
    conn = sqlite3.connect('agro_knowledge.db')
    cursor = conn.cursor()
    
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
            'stone_fruits',
            '🍒 Косточковые сады (Черешня, Персик, Нектарин, Слива, Абрикос/Урюк, Вишня)',
            '🍒 Stone Fruit Orchards (Cherry, Peach, Nectarine, Plum, Apricot, Sour Cherry)',
            '<b>1. Гидродинамика и Питание по фазам вегетации (USDA Organic / GlobalGAP):</b><br>'
            '• <i>Питательный профиль:</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Фаза цветения и завязи:</i> Внекорневой Хелат Бора (B) + Цинк (Zn) против осыпания.<br>'
            '• <i>Налив плодов:</i> Увеличение доли Калия (K) в соотношении N:K = 1:1.8 для сахаров и плотности.<br>'
            '• <i>Норма вылива:</i> 40–60 л/дерево в сутки при жарких температурах (>+32°C).<br><br>'
            '<b>2. Экологическая Защита и Болезни:</b><br>'
            '• <i>Монилиоз (Монилинный ожог):</i> Обработка Bacillus subtilis (26Д) в фазы «розовый бутон» и «падение лепестков».<br>'
            '• <i>Клястероспориоз и Коккомикоз:</i> Внесение Trichoderma harzianum капельно в прикорневую зону.<br>'
            '• <i>Вишневая муха и Тля:</i> Био-инсектицид Bacillus thuringiensis (БТБ) + Масло Нима (0.8%).',
            
            '<b>1. Irrigation Dynamics & Growth Stage Nutrition:</b><br>'
            '• <i>Nutrient Profile:</i> pH 6.0–6.5 | EC 1.4–1.8 mS/cm | N:120, P:40, K:180, Ca:140, Mg:45 ppm.<br>'
            '• <i>Flowering & Set:</i> Foliar Boron (B) + Zinc (Zn) chelates to prevent blossom drop.<br>'
            '• <i>Fruit Enlargement:</i> Increase Potassium (K) ratio to N:K = 1:1.8 for sugar accumulation.<br>'
            '• <i>Drip Flow Rate:</i> 40–60 L/tree daily during peak summer (>+32°C).<br><br>'
            '<b>2. Organic Bio-Protection:</b><br>'
            '• <i>Monilinia Blight:</i> Bacillus subtilis sprays at pink bud and petal fall stages.<br>'
            '• <i>Shot Hole & Blight:</i> Trichoderma harzianum fertigation to root zone.<br>'
            '• <i>Cherry Fruit Fly & Aphids:</i> Bacillus thuringiensis (BTB) + Cold-pressed Neem Oil (0.8%).'
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
            'pome_subtropical',
            '🍎 Семечковые & Субтропики (Яблоня, Груша, Айва, Гранат, Олива, Инжир, Хурма)',
            '🍎 Pome & Subtropical Crops (Apple, Pear, Quince, Pomegranate, Olive, Fig, Persimmon)',
            '<b>1. Стандарты Выращивания и Капельного Полива:</b><br>'
            '• <i>Яблоня, Груша, Айва:</i> pH 6.0–6.5 | EC 1.2–1.8 mS/cm | N:110, P:35, K:170, Ca:130, Mg:40 ppm.<br>'
            '• <i>Гранат, Олива, Инжир, Хурма:</i> pH 6.2–7.2 | EC 1.8–2.5 mS/cm | GDD > 3000°C.<br>'
            '• <i>Предотвращение растрескивания Граната:</i> Строго равномерный вылив + Хелат Кальция (Ca-EDTA) в июне-августе.<br><br>'
            '<b>2. Биологическая Защита:</b><br>'
            '• <i>Парша Яблони/Груши & Медяница:</i> Опрыскивание Bacillus subtilis + энтомофаги.<br>'
            '• <i>Гранатовая плодожорка:</i> Заселение Трихограммы (Trichogramma) + бактериальный инсектицид БТБ.',
            
            '<b>1. Production & Drip Fertigation Standards:</b><br>'
            '• <i>Apple, Pear, Quince:</i> pH 6.0–6.5 | EC 1.2–1.8 mS/cm | N:110, P:35, K:170, Ca:130, Mg:40 ppm.<br>'
            '• <i>Pomegranate, Olive, Fig, Persimmon:</i> pH 6.2–7.2 | EC 1.8–2.5 mS/cm | GDD > 3000°C.<br>'
            '• <i>Pomegranate Split Prevention:</i> Steady irrigation + Calcium Chelate (Ca-EDTA) in July–August.<br><br>'
            '<b>2. Biological Protection:</b><br>'
            '• <i>Apple/Pear Scab & Psylla:</i> Bacillus subtilis sprays + beneficial insect releases.<br>'
            '• <i>Pomegranate Moth:</i> Trichogramma releases + Bacillus thuringiensis (BTB) sprays.'
        )
    ]
    
    cursor.executemany('INSERT INTO knowledge (category, title_ru, title_en, content_ru, content_en) VALUES (?, ?, ?, ?, ?)', data)
    conn.commit()
    conn.close()
    print("Бэкенд Блок А (Все сады и орехи) успешно залит!")

if __name__ == '__main__':
    init_and_fill_db()
