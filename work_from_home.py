from creds import credentials
from objects.check_months_report import CheckMonthsReport
from objects.send_months_report import SendMonthsReport
from objects.save_dates import SaveDates
from objects.create_new_file_report import CreateNewFileReport
from objects.rail_time import RailTime

from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.dispatcher.filters import Command
from keyboard.keyboard_menu import kb_railway,kb_check_report,kb_send_report

bot = Bot(token=credentials.TOKEN)
dp = Dispatcher(bot)

check_month_report = CheckMonthsReport()
send_month_report = SendMonthsReport()
save_work_dates = SaveDates()
new_file_report = CreateNewFileReport()
rail_time = RailTime()

@dp.message_handler(Command('railway'))
async def railway(message : types.Message):
    await message.answer("Please choose your distination: ",reply_markup=kb_railway)

@dp.message_handler(text=['Bat Galim - Kiryat Motzkin'])
async def rail_time_checker_bg_km(message : types.Message):
    rail_time.rail_time_bg_km()

    if len(rail_time.rail_time_bg_km().get("routes")) > 4096:
        for x in range(0, len(rail_time.rail_time_bg_km().get("routes")), 4096):
            await bot.send_message(message.chat.id,"Bat-Galim : Kiryat-Motzkin" + rail_time.rail_time_bg_km().get("routes")[x:x + 4096])
    else:
        await bot.send_message(message.from_user.id,"Bat-Galim : Kiryat-Motzkin" + rail_time.rail_time_bg_km().get("routes"))


@dp.message_handler(text=['Kiryat Motzkin - Bat Galim'])
async def rail_time_checker_km_bg(message : types.Message):
    rail_time.rail_time_km_bg()

    if len(rail_time.rail_time_km_bg().get("routes")) > 4096:
        for x in range(0, len(rail_time.rail_time_km_bg().get("routes")), 4096):
            await bot.send_message(message.from_user.id,"Kiryat-Motzkin : Bat-Galim" + rail_time.rail_time_km_bg().get("routes")[x:x + 4096])
    else:
       await bot.send_message(message.from_user.id, "Kiryat-Motzkin : Bat-Galim" + rail_time.rail_time_km_bg().get("routes"))

# Check report

@dp.message_handler(Command('check_report'))
async def check_report(message : types.Message):
    await message.answer("Please select month to check of report : ", reply_markup = kb_check_report)

@dp.message_handler(text = ['January'])
async def check_days_january(message : types.Message):

    check_month_report.month("January")
    await bot.send_message(message.from_user.id, check_month_report.month("January"))

@dp.message_handler(text = ['February'])
async def check_days_february(message : types.Message):

    check_month_report.month("February")
    await bot.send_message(message.from_user.id, check_month_report.month("February"))

@dp.message_handler(text = ['March'])
async def check_days_march(message : types.Message):

    check_month_report.month("March")
    await bot.send_message(message.from_user.id, check_month_report.month("March"))

@dp.message_handler(text = ['April'])
async def check_days_april(message : types.Message):

    check_month_report.month("April")
    await bot.send_message(message.from_user.id, check_month_report.month("April"))

@dp.message_handler(text = ['May'])
async def check_days_may(message : types.Message):

    check_month_report.month("May")
    await bot.send_message(message.from_user.id, check_month_report.month("May"))

@dp.message_handler(text = ['June'])
async def check_days_june(message : types.Message):

    check_month_report.month("June")
    await bot.send_message(message.from_user.id, check_month_report.month("June"))

@dp.message_handler(text = ['July'])
async def check_days_july(message : types.Message):

    check_month_report.month("July")
    await bot.send_message(message.from_user.id, check_month_report.month("July"))

@dp.message_handler(text = ['August'])
async def check_days_august(message : types.Message):

    check_month_report.month("August")
    await bot.send_message(message.from_user.id, check_month_report.month("August"))

@dp.message_handler(text = ['September'])
async def check_days_september(message : types.Message):

    check_month_report.month("September")
    await bot.send_message(message.from_user.id, check_month_report.month("September"))


@dp.message_handler(text = ['October'])
async def check_days_october(message : types.Message):

    check_month_report.month("October")
    await bot.send_message(message.from_user.id, check_month_report.month("October"))


@dp.message_handler(text = ['November'])
async def check_days_november(message : types.Message):

   check_month_report.month("November")
   await bot.send_message(message.from_user.id, check_month_report.month("November"))


@dp.message_handler(text = ['December'])
async def check_days_december(message : types.Message):

    check_month_report.month("December")
    await bot.send_message(message.from_user.id, check_month_report.month("December"))



# Send report

@dp.message_handler(Command('send_report'))
async def send_report(message : types.Message):
    await message.answer("Please select report to send : ", reply_markup = kb_send_report)

@dp.message_handler(text = ['January.'])
async def send_january_report(message : types.Message):
    send_month_report.send_month("January")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['February.'])
async def send_february_report(message : types.Message):

    send_month_report.send_month("February")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['March.'])
async def send_march_report(message : types.Message):

    send_month_report.send_month("March")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['April.'])
async def send_april_report(message : types.Message):

    send_month_report.send_month("April")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['May.'])
async def send_may_report(message : types.Message):

    send_month_report.send_month("May")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['June.'])
async def send_june_report(message):

    send_month_report.send_month("June")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['July.'])
async def send_july_report(message : types.Message):

    send_month_report.send_month("July")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['August.'])
async def send_august_report(message : types.Message):

    send_month_report.send_month("August")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['September.'])
async def send_september_report(message : types.Message):

    send_month_report.send_month("September")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['October.'])
async def send_october_report(message : types.Message):

    send_month_report.send_month("October")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['November.'])
async def send_november_report(message : types.Message):

    send_month_report.send_month("November")
    await bot.send_message(message.from_user.id,"Report has been sent")

@dp.message_handler(text = ['December.'])
async def send_december_report(message : types.Message):

    send_month_report.send_month("December.")
    await bot.send_message(message.from_user.id,"Report has been sent")


def create_file():

 new_file_report.create_new_file_report()

@dp.message_handler(Command('work'))
async def work_command(message: types.Message):
    await message.reply("Please enter your date: ")


@dp.message_handler()
async def save_dates(message : types.Message):

    save_work_dates.dates_saver(message.text)
    await bot.send_message(message.from_user.id, "Your event has been successfully created")


create_file()
executor.start_polling(dp,skip_updates=True)

