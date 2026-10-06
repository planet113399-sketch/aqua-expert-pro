import sqlite3

conn = sqlite3.connect("agro_knowledge.db")
cursor = conn.cursor()

# Пересоздаем таблицу для полной чистоты и обновления структуры
cursor.execute("DROP TABLE IF EXISTS knowledge")
cursor.execute("""
CREATE TABLE knowledge (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    code_eppo TEXT,
    category TEXT,
    name_ru TEXT,
    name_en TEXT,
    description_ru TEXT,
    description_en TEXT,
    tank_mix_rule_ru TEXT,
    tank_mix_rule_en TEXT,
    is_organic INTEGER
)
""")

# Полная базовая информация высокой детализации
records = [
    (
        "GYPSUM-PRO",
        "Почвоведение & Мелиорация",
        "Гипс агрономический (Сульфат кальция - CaSO₄·2H₂O)",
        "Agricultural Gypsum (Calcium Sulfate)",
        (
            "ПОЛНОЕ РУКОВОДСТВО ПО ПРИМЕНЕНИЮ ГИПСА:\n\n"
            "1. НАЗНАЧЕНИЕ И ЦЕЛИ ИСПОЛЬЗОВАНИЯ:\n"
            "• Химическая мелиорация и рассоление солонцовых и щелочных почв (замещение натрия на кальций в почвенном поглощающем комплексе).\n"
            "• Улучшение структуры почвы: разрушает плотную почвенную корку, предотвращает эрозию, улучшает водопроницаемость и аэрацию тяжелых глинистых почв.\n"
            "• Источник доступного кальция (Ca - 23%) и серы (S - 18%) без изменения кислотности (pH) почвы.\n\n"
            "2. В КАКИХ УСЛОВИЯХ И ПРИ КАКИХ СИМПТОМАХ ИСПОЛЬЗОВАТЬ:\n"
            "• При высоком содержании обмениваемого натрия (>5% от ЕКО).\n"
            "• На плотных глинистых почвах, где плохо просачивается вода и застаиваются лужи.\n"
            "• При дефиците кальция (отмирание точек роста у овощных культур, вершиночная гниль томатов).\n"
            "• На культурах с высокой потребностью в сере (рапс, подсолнечник, бобовые, капуста).\n\n"
            "3. СРОКИ И СПОСОБ ВНЕСЕНИЯ:\n"
            "• Основное внесение: Осенью или ранней весной под глубокую вспашку или дискование на глубину 15–20 см.\n"
            "• Важное условие: Гипс эффективно работает только при достаточном увлажнении (осадки или обильный полив после внесения для вымывания солей натрия).\n\n"
            "4. НОРМЫ ВНЕСЕНИЯ (ДОЗИРОВКА):\n"
            "• Слабосолонцеватые почвы: 1.5 – 3 тонны на гектар (150–300 г/м²).\n"
            "• Средне- и сильносолонцеватые почвы: 5 – 10 тонн на гектар (500–1000 г/м²).\n"
            "• Подкормка и улучшение структуры тяжелых глин: 300–500 кг/га."
        ),
        (
            "COMPREHENSIVE GYPSUM GUIDE:\n\n"
            "1. PURPOSE & INTENDED USE:\n"
            "• Chemical reclamation of sodic/alkaline soils by replacing sodium with calcium.\n"
            "• Soil structure improvement: prevents crusting, improves water infiltration and aeration in heavy clay soils.\n"
            "• Excellent source of readily available Calcium (23%) and Sulfur (18%) without altering soil pH.\n\n"
            "2. APPLICATION CONDITIONS:\n"
            "• Sodic soils with exchangeable sodium > 5%.\n"
            "• Dense clay soils with poor water infiltration and drainage issues.\n"
            "• High-sulfur requirement crops (canola, legumes, sunflower).\n\n"
            "3. TIMING AND METHOD:\n"
            "• Application: Autumn or early spring prior to deep plowing (15-20 cm depth).\n"
            "• Requires adequate rainfall or irrigation to flush displaced sodium salts."
        ),
        "Регламент: Не смешивать в одном растворе с фосфатными удобрениями высокого разведения до внесения в почву. Совместим с органикой.",
        "Rule: Do not tank-mix directly with concentrated phosphate fertilizers. Compatible with organic amendments.",
        1,
    ),
    (
        "BIOCHAR-PRO",
        "Почвоведение & Мелиорация",
        "Биочар (Древесный биоуголь-мелиорант)",
        "Biochar Soil Amendment",
        (
            "ПОЛНОЕ РУКОВОДСТВО ПО ИСПОЛЬЗОВАНИЮ БИОЧАРА:\n\n"
            "1. ДЛЯ ЧЕГО ИСПОЛЬЗУЕТСЯ:\n"
            "• Долговечное (до 100+ лет) улучшение структуры почвы и создание губчатой матрицы.\n"
            "• Удержание влаги и предотвращение вымывания минеральных удобрений из корнеобитаемого слоя.\n"
            "• Дом для полезной микрофлоры (микориза, азотфиксаторы).\n\n"
            "2. УСЛОВИЯ И Правила Применения:\n"
            "• ВАЖНО: Не вносить «сырой» чистый биочар без предварительной зарядки, иначе он временно заберет на себя питательные вещества из почвы!\n"
            "• Зарядка биочара: За 2–3 недели до внесения смешать биочар с компостом, биогумусом или раствором органо-минеральных удобрений в пропорции 1:1.\n\n"
            "3. ДОЗИРОВКА И СРОКИ:\n"
            "• Норма внесения: 5–10% от объема почвосмеси в теплицах или 1–2 кг на 1 м² в открытом грунте.\n"
            "• Вносится 1 раз на много лет при перекопке или посадке деревьев/кустарников."
        ),
        (
            "BIOCHAR COMPLETE MANUAL:\n\n"
            "1. PURPOSES:\n"
            "• Long-term soil structure enhancement and moisture retention matrix.\n"
            "• Prevents nutrient leaching in sandy and depleted soils.\n\n"
            "2. CRITICAL PREPARATION:\n"
            "• Inoculation/Charge: Pre-mix 1:1 with compost or liquid organic fertilizer 2-3 weeks before application to avoid initial nutrient drawdown."
        ),
        "Регламент: Заряжать биогумусом или компостом перед внесением.",
        "Rule: Must be charged with nutrients/compost prior to soil application.",
        1,
    ),
    (
        "SULFUR-PRO",
        "Агрохимия & Удобрения",
        "Сера молотая агрономическая (S - 99%)",
        "Agricultural Elemental Sulfur",
        (
            "ПОЛНОЕ РУКОВОДСТВО ПО ПРИМЕНЕНИЮ СЕРЫ:\n\n"
            "1. ОСНОВНЫЕ ЦЕЛИ ИСПОЛЬЗОВАНИЯ:\n"
            "• Мягкое и подконтрольное подкисление почвы (снижение уровня pH) для кислолюбивых культур (голубика, брусника, гортензии, хвойные).\n"
            "• Фунгицидное и акарицидное действие против мучнистой росы и клещей.\n"
            "• Мезоэлемент питания для масличных и бобовых культур.\n\n"
            "2. КАК И КОГДА ИСПОЛЬЗОВАТЬ:\n"
            "• Для подкисления: Вносится за 3–6 месяцев до посадки, так как бактериям требуется время для перевода серы в серную кислоту.\n"
            "• Температурный режим: Почвенные бактерии активны при температуре почвы выше +12°C."
        ),
        (
            "ELEMENTAL SULFUR MANUAL:\n\n"
            "1. PURPOSES:\n"
            "• Soil acidification (pH lowering) for acid-loving crops (blueberries, hydrangeas).\n"
            "• Natural fungicide and acaricide against powdery mildew and mites."
        ),
        "Регламент: Работать в защитных очках и респираторе.",
        "Rule: Wear protective goggles and dust mask.",
        1,
    ),
]

cursor.executemany(
    """
INSERT INTO knowledge (
    code_eppo, category, name_ru, name_en, description_ru, description_en, tank_mix_rule_ru, tank_mix_rule_en, is_organic
) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
""",
    records,
)

conn.commit()
conn.close()

print(" УСПЕШНО! База данных заполнена подробными экспертными инструкциями!")