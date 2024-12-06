from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, MessageHandler, filters, ConversationHandler,ContextTypes

# Вставьте ваш токен

# Вставьте ваш токен
TOKEN = '8047510722:AAGJuvMZweRNiIeG3C3OILrW1-fAW8fNFR0'

# Данные о турах
tours = {
    "Чарынский каньон": {
        "description": "Что входит в тур в Чарынский каньон\n1.	Транспорт:•	Трансфер на комфортном автобусе или микроавтобусе.\n•	Услуги профессионального водителя.\n2.	Гид-сопровождающий:\n•	Опытный гид, который расскажет об истории и природных особенностях Чарынского каньона.\n3.	Питание:\n•	Ланч-бокс или обед.\n•	Чай или напитки (особенность Ozimiz Tour).\n4.	Дополнительные услуги:\n•	Входные билеты на территорию национального парка.\n•	Свободное время для прогулки и фотографий.\n•	Организация мини-экскурсий на месте.\n5.	Другие бонусы:\n•	Медицинская аптечка в автобусе.\n•	Возможность выбрать индивидуальный маршрут для небольших групп.",
        "price": "	•	Групповой тур (Размер группы: 8-15 чел): 12,000–15,000 тенге.\n•	Индивидуальный тур: от 25,000 тенге за человека (в зависимости от уровня комфорта).",
        "dates": "20-21 октября"
    },
    "Кольсай и Каинды  от Ozimiz Tour": {
        "description": "Что вас ждёт:\nЭто уникальный двухдневный тур, который погружает вас в природную красоту Алматинской области и атмосферу казахского гостеприимства. Маршрут охватывает озёра Кольсай и Каинды, знаменитые своим кристально чистым воздухом, яркими пейзажами и спокойной атмосферой.\nПрограмма тура:День 1:\n	1.	Ранний выезд из Алматы:\n•	Комфортабельный микроавтобус с кондиционером и опытным водителем.\n2.	Озеро Каинды:\n•	Экскурсия к озеру с гидом.\n	•	Время для самостоятельной прогулки и фотографий.\n•	Перекус (чай и лёгкий снэк от Ozimiz Tour).\n3.	Прибытие в гостевой дом:\n•	Размещение у местных жителей в уютных домиках (2-3 человека в комнате).\n•	Домашний ужин из свежих местных продуктов.\n• вечерний сбор у костра\n\nДень 2:\n	1.	Завтрак:\n•	Традиционные казахские блюда (айран, баурсаки, каши, чай).\n2.	Экскурсия на Кольсайские озёра:\n•	Прогулка вокруг первого озера.\n•	Возможность арендовать лошадей для путешествия к следующему озеру (за доп. плату).\n	3.	Обед:\n•	На природе или в гостевом доме.\n4.	Возвращение в Алматы:\n•	Около 20:00 – 21:00 вы будете доставлены обратно в город.\nЧто входит в тур:\n1.	Транспорт:\n•	Трансфер по маршруту на комфортабельном микроавтобусе.\n2.	Проживание:\n•	1 ночь в домиках у местных жителей (чистое постельное бельё, горячая вода).\n3.	Питание:\n•	Завтрак, обед и ужин (традиционные блюда местной кухни).\n•	Чай и сладости от Ozimiz Tour.\n4.	Гид:\n	•	Сопровождение опытного гида на всём маршруте.\n5.	Входные билеты:\n•	Оплата экологических сборов на территории национального парка.\n6.	Дополнительные услуги:\n•	Помощь в организации активности (например, прогулки на лошадях).\nПочему выбрать Ozimiz Tour?\n•	Авторские маршруты, составленные с учётом ваших пожеланий.\n•	Тёплая атмосфера и знакомство с традициями казахского гостеприимства.\n•	Чай как фирменная фишка тура, чтобы ваш отдых был ещё комфортнее.\n",
        "price": "•	Групповой тур (6–12 человек): от 30,000 до 35,000 тенге.\n•	Индивидуальный тур (2–4 человека): от 45,000 тенге.",
        "dates": "25-26,27 октября"
    },
    "Озеро Иссык от Ozimiz Tour": {
        "description": "Чем уникален этот тур?\nИссык — одно из самых живописных мест в Алматинской области, где горы, сосновые леса и бирюзовая гладь озера создают незабываемую атмосферу. Этот тур подойдёт для тех, кто хочет отдохнуть от городской суеты, насладиться свежим воздухом и погрузиться в историю региона.\nПрограмма тура:Утро:\n\n1.	Выезд из Алматы:\n•	Ранний сбор группы, отправление на комфортном микроавтобусе.\n•	По пути гид расскажет историю Иссыкского озера и катастрофы 1963 года.\n2.	Прибытие на озеро:\n•	Время для самостоятельной прогулки, фотографий и наслаждения природой.\n•	Лёгкий пикник на берегу озера (входит в стоимость).\nДень:\n3. Экскурсия:\n\n•	Посещение Иссыкского музея (по желанию), где вы узнаете о сакской культуре и знаменитом «Золотом человеке».\n•	Свободное время: возможность арендовать лодки (если доступно) или просто отдохнуть у воды.\n4.	Обед на природе:\nТрадиционный казахский обед, приготовленный из местных продуктов.\nВечер:\n5. Возвращение в Алматы:\n\n•	По пути остановка в красивых местах для фотографий.\n•	Прибытие в город к вечеру (около 18:00).\nЧто входит в тур:\n\n1.	Транспорт:\n•	Трансфер на комфортабельном микроавтобусе.\n2.	Питание:\n•	Лёгкий перекус (чай и снэки).\n•	Обед на природе.\n3.	Гид:\n•	Опытный гид, который сделает путешествие интересным и познавательным.\n4.	Дополнительные услуги:\n•	Входные билеты в национальный парк.\n•	Организация пикника и помощь в создании комфортной атмосферы.\nПреимущества тура с Ozimiz Tour:\n\n•	Уникальный подход: внимание к деталям, включая фирменный чай.\n•	Удобный маршрут с комфортным транспортом.\n•	Возможность погрузиться в местную культуру и историю.",
        "price": "•	Групповой тур (8–15 человек): от 15,000 тенге.\n•	Индивидуальный тур (2–4 человека): от 25,000 тенге.",
        "dates": "1 ноября"
    }
}

# Состояния разговора
NAME, PHONE, EMAIL, PERSON_COUNT = range(4)



# Хендлер для кнопки "Забронировать тур"
async def book_tour(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Чарынский каньон", callback_data='Charyn')],
        [InlineKeyboardButton("Кольсай и Каинды", callback_data='Kolsai')],
        [InlineKeyboardButton("Озеро Иссык", callback_data='Issyk')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.callback_query.message.edit_text("Выберите тур для бронирования:", reply_markup=reply_markup)

# Хендлер для выбора тура
async def tour_info(update: Update, context):
    tour_name = update.callback_query.data
    full_tour_name = ""

    if tour_name == "Charyn":
        full_tour_name = "Чарынский каньон"
    elif tour_name == "Kolsai":
        full_tour_name = "Кольсай и Каинды от Ozimiz Tour"
    elif tour_name == "Issyk":
        full_tour_name = "Озеро Иссык от Ozimiz Tour"
    
    # Получаем информацию о туре
    tour = tours.get(full_tour_name)
    
    if tour:
        message = f"Тур: {full_tour_name}\n\nОписание: {tour['description']}\n\nСтоимость: {tour['price']}\nДаты тура: {tour['dates']}"
        keyboard = [
            [InlineKeyboardButton("ПОДТВЕРДИТЬ БРОНИРОВАНИЕ", callback_data=f'confirm_{tour_name}')]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.callback_query.message.edit_text(message, reply_markup=reply_markup)

# Хендлер для подтверждения бронирования
async def confirm_booking(update: Update, context):
    tour_name = update.callback_query.data.split('_')[1]
    full_tour_name = ""

    if tour_name == "Charyn":
        full_tour_name = "Чарынский каньон"
    elif tour_name == "Kolsai":
        full_tour_name = "Кольсай и Каинды от Ozimiz Tour"
    elif tour_name == "Issyk":
        full_tour_name = "Озеро Иссык от Ozimiz Tour"
    
    # Сохраняем выбранный тур в контексте
    context.user_data['tour_name'] = full_tour_name

    # Запрос имени
    await update.callback_query.message.edit_text(f"Пожалуйста, введите ваше имя для бронирования тура: {full_tour_name}")
    return NAME

# Хендлер для получения имени клиента
async def get_name(update: Update, context):
    context.user_data['name'] = update.message.text
    await update.message.reply_text("Теперь введите ваш контактный номер телефона:")
    return PHONE

# Хендлер для получения номера телефона
async def get_phone(update: Update, context):
    context.user_data['phone'] = update.message.text
    await update.message.reply_text("Теперь введите ваш email:")
    return EMAIL

# Хендлер для получения email
async def get_email(update: Update, context):
    context.user_data['email'] = update.message.text
    await update.message.reply_text("Теперь введите количество человек для бронирования:")
    return PERSON_COUNT

# Хендлер для получения количества людей
async def get_person_count(update: Update, context):
    context.user_data['person_count'] = update.message.text

    # Отображаем итоговое сообщение с данными
    tour = tours.get(context.user_data['tour_name'])
    if tour:
        message = f"Ваши данные для бронирования:\n\n" \
                  f"Тур: {context.user_data['tour_name']}\n" \
                  f"Имя: {context.user_data['name']}\n" \
                  f"Телефон: {context.user_data['phone']}\n" \
                  f"Email: {context.user_data['email']}\n" \
                  f"Количество человек: {context.user_data['person_count']}\n" \
                  f"Стоимость: {tour['price']}\n" \
                  f"Даты тура: {tour['dates']}\n\n" \
                  "Ваши данные были переданы менеджеру. С вами скоро свяжутся для уточнения деталей."
        
        keyboard = [
            [InlineKeyboardButton("Данные не правильны", callback_data="confirm_booking")]
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await update.message.reply_text(message, reply_markup=reply_markup)
    
    # Завершаем разговор
    return ConversationHandler.END






# Хендлер для команды /start

async def start(update: Update, context):
    keyboard = [
        [InlineKeyboardButton("Сотрудничество с нами", callback_data='collaboration')],
        [InlineKeyboardButton("Особые предложения", callback_data='special_offers')],
        [InlineKeyboardButton("О нас", callback_data='about_us')],
        [InlineKeyboardButton("Отзывы", callback_data='reviews')],
        [InlineKeyboardButton("Связь с нами", callback_data='contact_manager')],
        [InlineKeyboardButton("Забронировать тур", callback_data='book_tour')]  # Кнопка в виде списка
]

    
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Добро пожаловать в Ozimiz Tour!\nМы рады видеть вас на нашей странице.", reply_markup=reply_markup)

# Обработчики для кнопок
# 2. Сотрудничество с нами
async def collaboration(update: Update, context):
    message = "- • Проведение совместных акций, например, «Скидка на экскурсию при бронировании в отеле\n• Предоставление эксклюзивных туристических пакетов для гостей отелей.\n• Распространение информационных брошюр Ozimiz Tour на стойках ресепшн.\n• финансовые отчеты\n• индивидуальные предложения \n• статистика и аналитика\n• прогнозирование спроса\n• реклама вашей продукции"
    await update.callback_query.message.edit_text(message)

# 3. Особые предложения
async def special_offers(update: Update, context):
    message = "Особые предложения:\nТур на Алаколь на 4 дня\n\nПродолжительность: 4 дня / 3 ночи\nТранспорт: Комфортабельный автобус (туда и обратно)\nПроживание: Отель на первой береговой линии с бассейном\nПитание: Трехразовое питание (завтрак, обед, ужин)\n\nПрограмма тура\n\nДень 1: Отправление и размещение\n\n	•	06:00: Сбор группы и отправление на автобусе к озеру Алаколь.\n	•	В пути: Технические остановки, легкие закуски.\n	•	13:00: Прибытие в отель, регистрация и размещение.\n	•	14:00-15:00: Обед в ресторане отеля.\n	•	16:00: Свободное время для отдыха:\n	•	Купание в бассейне или на пляже.\n	•	Прогулки вдоль берега.\n	•	19:00: Ужин в отеле.\n	•	Вечером – свободное время для расслабления или настольных игр в отеле.\n\nДень 2: Наслаждение природой и отдых\n\n	•	08:00-09:00: Завтрак.\n	•	09:30: Утренний пляжный отдых или плавание в бассейне.\n	•	12:30-13:30: Обед.\n	•	14:00: Дополнительно:\n	•	Экскурсия к целебным грязевым местам Алаколя (по желанию).\n	•	Катание на катамаранах (за дополнительную плату).\n	•	18:30: Ужин в отеле.\n	•	20:00: Вечерняя развлекательная программа: караоке или танцы у бассейна.\n\nДень 3: Активный отдых и релакс\n\n	•	08:00-09:00: Завтрак.\n	•	09:30-12:30: Утренний отдых у воды или йога на пляже.\n	•	12:30-13:30: Обед.\n	•	14:00: Возможности для активного отдыха:\n	•	Игра в пляжный волейбол.\n	•	Аренда велосипедов для прогулок вдоль побережья.\n	•	18:30: Ужин.\n	•	20:00: Вечерний костер на берегу с чаем и легкими закусками.\n\nДень 4: Завершение тура\n\n	•	08:00-09:00: Завтрак.\n	•	09:30: Освобождение номеров.\n	•	10:00: Отправление обратно.\n	•	17:00-18:00: Прибытие в город.\n\nСтоимость тура:\nВключает:\n\n	•	Проезд на автобусе.\n	•	Проживание в отеле на первой береговой линии.\n	•	Трехразовое питание.\n	•	Пользование бассейном и инфраструктурой отеля.\n	•	Сопровождение гида.\n\nДополнительно оплачивается:\n\n	•	Личные расходы.\n	•	Экскурсии и развлечения по желанию.\n  \n\nЦена: 70.000тг на чел\n           Детский 55.000тг \nЭтот тур идеально подходит для тех, кто хочет отдохнуть и насладиться красотой Алаколя."
    await update.callback_query.message.edit_text(message)

# 4. О нас
async def about_us(update: Update, context):
    message = "О нас:\n\n О компании Ozimiz Tour\nOzimiz Tour — это один из лучших вариантов для тех, кто хочет провести незабываемый отдых и открыть для себя красоту природы Казахстана. Мы предлагаем уникальные туры, которые позволят вам ощутить гармонию с природой, насладиться ее великолепием и создать воспоминания, которые останутся с вами на всю жизнь.\n\nПочему выбирают нас?\n	•	Погружение в природу\nМы доставляем вас к самым живописным уголкам Казахстана: от завораживающих озер Каинды и Кольсай до величественного Чарынского каньона. Каждый маршрут тщательно продуман, чтобы вы могли насладиться природой в ее первозданной красоте.\n	•	Лучшие гиды\nНаши гиды — это не просто специалисты, это настоящие проводники в мир казахстанской культуры и природы. Они не только расскажут увлекательные истории, но и сделают ваш отдых комфортным и безопасным.\n	•	Чай — символ гостеприимства\nОдной из наших фирменных черт является теплый прием, который всегда сопровождается ароматным казахстанским чаем. Это не просто напиток — это часть традиции, создающая уют и ощущение дома, где бы вы ни находились.\n\nOzimiz Tour — это отдых, который сочетает в себе комфорт, приключения и душевное тепло. Присоединяйтесь к нам, чтобы открыть для себя Казахстан, его природу и культуру, как никогда раньше!"
    await update.callback_query.message.edit_text(message)

# 5. Отзывы
async def reviews(update: Update, context):
    message = "Отзывы:\n\nДобрый вечер! Мне понравилось приложение, все очень удобно, функционально, хороший дизайн👍🏻\n\n\nЗдравствуйте, очень классно что расписаны все туры, много информации, доступные цены. Также отдельное спасибо, за подбор индивидуальных туров\n\n\nЗдравствуйте, несмотря на свой возраст, разобрался в приложении, все понятно и просто. С женой хотели развеять будни и сгонять в Кольсай, цены очень хорошие, поэтому выбор пал на «ozimiz tour»😃👍🏻"
    await update.callback_query.message.edit_text(message)

# 6. Связь с менеджером
async def contact_manager(update: Update, context):
    message = "Свяжитесь с нами\n\nДля бронирования туров и получения дополнительной информации:\n\n📞 Телефон: +7 (XXX) XXX-XX-XX\n📩 Email: info@ozimiztour.kz\n📱 Instagram: @ozimiztour\n🌐 Сайт: www.ozimiztour.kz\n\nНаши менеджеры с радостью ответят на все ваши вопросы и помогут организовать ваш идеальный отдых!"
    await update.callback_query.message.edit_text(message)

async def cancel(update: Update, context):
    await update.message.reply_text("Процесс бронирования был отменен.")
    return ConversationHandler.END  # Завершаем разговор
# Хендлер для отмены бронирования
async def cancel(update: Update, context):
    await update.message.reply_text("Процесс бронирования отменен.")
    return ConversationHandler.END  # Завершаем разговор



# Основной хендлер для команды /start
def main():
 
    application = Application.builder().token(TOKEN).build()
    conv_handler = ConversationHandler(
        entry_points=[CallbackQueryHandler(confirm_booking, pattern='^confirm_')],
        states={
            NAME: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_name)],
            PHONE: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_phone)],
            EMAIL: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_email)],
            PERSON_COUNT: [MessageHandler(filters.TEXT & ~filters.COMMAND, get_person_count)]
        },
        fallbacks=[]
    )

    # Добавление хендлеров
    application.add_handler(CommandHandler('start', start))
    application.add_handler(CallbackQueryHandler(collaboration, pattern='^collaboration$'))
    application.add_handler(CallbackQueryHandler(special_offers, pattern='^special_offers$'))
    application.add_handler(CallbackQueryHandler(about_us, pattern='^about_us$'))
    application.add_handler(CallbackQueryHandler(reviews, pattern='^reviews$'))
    application.add_handler(CallbackQueryHandler(contact_manager, pattern='^contact_manager$'))
    application.add_handler(CallbackQueryHandler(book_tour, pattern='^book_tour$'))
    application.add_handler(CallbackQueryHandler(tour_info, pattern='^(Charyn|Kolsai|Issyk)$'))
    application.add_handler(conv_handler)

    # Запуск бота
    application.run_polling()

if __name__ == '__main__':
    main()