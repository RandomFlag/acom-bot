import finding
from findImage import findIMG, lastPage
from telebot import types
import telebot
page = {}
bot = telebot.TeleBot("747515125:AAF5kvmBAkR_yjZ-YOmPFjCJZReYrz1aBaM")
state = {}
comic = {}

#"/start" message l
@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
    global page
    page [message.chat.id] = 1
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('/start')
    bot.send_message(message.chat.id, "Search:", reply_markup=markup)
    state [message.chat.id] = 'FindCom'
    
#response on text
@bot.message_handler(content_types=["text"])
def handle_text(message):
    global state
    global page
    
    #Finding Comics
    if state.get(message.chat.id, 'FindCom')  == 'FindCom':
        urls, names = finding.findCom (message.text)
        keyboard = types.InlineKeyboardMarkup()
        for q in names:
            ind = names.index(q)
            callback_button = types.InlineKeyboardButton(text = q, callback_data=urls[ind])
            keyboard.add(callback_button)
        bot.send_message(message.chat.id, "Results for: " + message.text , reply_markup=keyboard)
        
    #Reading Comics
    elif state.get(message.chat.id, 'FindCom')  == 'ReadCom':
        if message.text == '<':
            page [message.chat.id] -=1
        elif message.text == '>':
            page [message.chat.id] += 1
        elif message.text == str(page.get(message.chat.id, 1)) + '/' + lastPage(comic.get(message.chat.id, '0')):
            state [message.chat.id] = 'InputPage'
            markup = types.ReplyKeyboardRemove()
            bot.send_message(message.chat.id, 'Choose your page:' , reply_markup=markup)
            return
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('<', str(page.get(message.chat.id, 1)) + '/' + lastPage(comic.get(message.chat.id, '0')), '>')
        markup.row('/start')
        bot.edit_message_text(message.chat.id, findIMG(comic.get(message.chat.id, '0') + '/', page.get(message.chat.id, 1)), reply_markup=markup)
        
    #Inputting page
    elif state.get(message.chat.id, 'FindCom')  == 'InputPage':
        page [message.chat.id] = int(message.text, 10)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('<', str(page.get(message.chat.id, 1))+ '/' + lastPage(comic.get(message.chat.id, '0')), '>')
        markup.row('/start')
        bot.send_message(message.chat.id, findIMG(comic.get(message.chat.id, '0') + '/', page.get(message.chat.id, 1)), reply_markup=markup)
        state [message.chat.id] = 'ReadCom'
        
        
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    # Если сообщение из чата с ботом
    global comic
    global state
    comic[call.message.chat.id] = call.data
    if True:
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.row('<', str(page.get(call.message.chat.id, 1)) + '/' + lastPage(comic.get(call.message.chat.id, '0')), '>')
        markup.row('/start')
        bot.send_photo(call.message.chat.id, findIMG(comic.get(call.message.chat.id, '0') + '/', page.get(call.message.chat.id, 1)), reply_markup=markup)
        comic[call.message.chat.id] = call.data
        state [call.message.chat.id] = 'ReadCom'
        
        
bot.polling(none_stop=True, interval=0)
