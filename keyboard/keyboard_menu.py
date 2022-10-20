from aiogram.types import ReplyKeyboardMarkup,KeyboardButton



kb_railway = ReplyKeyboardMarkup(
    keyboard = [
        [
        KeyboardButton(text='Bat Galim - Kiryat Motzkin'),
        KeyboardButton(text='Kiryat Motzkin - Bat Galim')
        ],
    ],
    resize_keyboard=True

)


check_button1 = KeyboardButton("January")
check_button2 = KeyboardButton("February")
check_button3 = KeyboardButton("March")
check_button4 = KeyboardButton("April")
check_button5 = KeyboardButton("May")
check_button6 = KeyboardButton("June")
check_button7 = KeyboardButton("Jule")
check_button8 = KeyboardButton("August")
check_button9 = KeyboardButton("September")
check_button10 = KeyboardButton("October")
check_button11 = KeyboardButton("November")
check_button12 = KeyboardButton("December")

kb_check_report = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(check_button1, check_button2, check_button3, check_button4, check_button5,check_button6,
                                                                                        check_button7, check_button8, check_button9, check_button10, check_button11, check_button12)

send_button1 = KeyboardButton("January.")
send_button2 = KeyboardButton("February.")
send_button3 = KeyboardButton("March.")
send_button4 = KeyboardButton("April.")
send_button5 = KeyboardButton("May.")
send_button6 = KeyboardButton("June.")
send_button7 = KeyboardButton("Jule.")
send_button8 = KeyboardButton("August.")
send_button9 = KeyboardButton("September.")
send_button10 = KeyboardButton("October.")
send_button11 = KeyboardButton("November.")
send_button12 = KeyboardButton("December.")

kb_send_report = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(send_button1, send_button2, send_button3, send_button4, send_button5, send_button6, send_button7,
                                                                                       send_button8, send_button9, send_button10, send_button11, send_button12)