
""" 
Simple Telegram Bot to automate the process of obtaining Outline.com links. 
Created by Raivat Shah in 2019. 
"""
# Imports
from telegram.ext import Updater, CommandHandler, MessageHandler, filters
import logging
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
import telegram

# Logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

# Command Handlers. Usually take two arguments: bot and update. 
def start(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Karibu <b>" + update.message.from_user.first_name + "</b> \nNitumie ujumbe ulioandikwa '/maegesho + namba yako ya gari' (mfaano /maegesho T123FKG) kisha subiri sekunde chache nikupe taarifa ya madeni ya maegesho", parse_mode=telegram.ParseMode.HTML )

def mwanzo(update, context):
    context.bot.send_message(chat_id=update.message.chat_id, text="Karibu <b>" + update.message.from_user.first_name + "</b> \nNitumie ujumbe ulioandikwa '/maegesho + namba yako ya gari' (mfaano /maegesho T123FKG) kisha subiri sekunde chache nikupe taarifa ya madeni ya maegesho", parse_mode=telegram.ParseMode.HTML )

def maegesho(update, context):
    # Processing Outline
    options = Options()
    options.add_argument("--headless")
    options.add_argument("window-size=1400,1500")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("start-maximized")
    options.add_argument("enable-automation")
    options.add_argument("--disable-infobars")
    options.add_argument("--disable-dev-shm-usage")
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    browser.get('https://termis.tarura.go.tz/#/portal/parking')
    linkbar = browser.find_element(By.XPATH, value="//input[@formcontrolname='plateNumber']")
    linkbar.send_keys(context.args) # pass in the link from the argument
    linkbar.send_keys(Keys.ENTER)
    time.sleep(7)

    # count results
    #num_rows = len (browser.find_elements(By.XPATH, value="//table/tbody/tr"))
    num_rows = len (browser.find_elements(By.XPATH, value="//table/tbody/tr/td[2]"))

    #send number of tickets
    if num_rows == 0 :
        context.bot.send_message(chat_id=update.message.chat_id, text="Huna deni la gharama za maegesho😊" )
    else :
        context.bot.send_message(chat_id=update.message.chat_id, text="Ndugu <b>" + update.message.from_user.first_name + "</b>, una deni la <b>tiketi " + repr(num_rows) + "</b>. \n<i>(Kwa sasa nina uwezo wa kukutumia hadi tiketi 3)</i>", parse_mode=telegram.ParseMode.HTML )


    #trial manual yakuprint tickets (tedious)
    try:
        cn_1 = browser.find_element(By.XPATH, value="//table/tbody/tr[1]/td[2]")
    except:
        print("cn_1 not found")
    try:
        cn_2 = browser.find_element(By.XPATH, value="//table/tbody/tr[3]/td[2]")
    except:
        print("cn_2 not found")
    try:
        cn_3 = browser.find_element(By.XPATH, value="//table/tbody/tr[5]/td[2]")
    except:
        print("cn_3 not found")
    try:
        deni_1 = browser.find_element(By.XPATH, value="//table/tbody/tr[1]/td[3]")
    except:
        print("deni_1 not found")
    try:
        deni_2 = browser.find_element(By.XPATH, value="//table/tbody/tr[3]/td[3]")
    except:
        print("deni_2 not found")
    try:
        deni_3 = browser.find_element(By.XPATH, value="//table/tbody/tr[5]/td[3]")
    except:
        print("deni_3 not found")
    try:
        kiasi_1 = browser.find_element(By.XPATH, value="//table/tbody/tr[1]/td[4]")
    except:
        print("kiasi_1 not found")
    try:
        kiasi_2 = browser.find_element(By.XPATH, value="//table/tbody/tr[3]/td[4]")
    except:
        print("kiasi_2 not found")
    try:
        kiasi_3 = browser.find_element(By.XPATH, value="//table/tbody/tr[5]/td[4]")
    except:
        print("kiasi_3 not found")
    try:
        baki_1 = browser.find_element(By.XPATH, value="//table/tbody/tr[1]/td[5]")
    except:
        print("baki_1 not found")
    try:
        baki_2 = browser.find_element(By.XPATH, value="//table/tbody/tr[3]/td[5]")
    except:
        print("baki_2 not found")
    try:
        baki_3 = browser.find_element(By.XPATH, value="//table/tbody/tr[5]/td[5]")
    except:
        print("baki_3 not found")


    #trial ya kuprint tickets
    rows = browser.find_elements(By.XPATH, value="//table/tbody/tr")
    num_rows = len (rows)
    for i in range (1, num_rows + 1) :
        cols = browser.find_elements(By.XPATH, value="//table/tbody/tr["+str(i)+"]/td")
        num_cols = len (cols)
        for j in range (1, num_cols + 1) :
            celtext = browser.find_elements(By.XPATH, value="//table/tbody/tr["+str(i)+"]/td["+str(j)+"]")
            if i == 1 and j == 2 :
                context.bot.send_message(chat_id=update.message.chat_id, text="1. Control number <b>" + cn_1.text + "</b> inadaiwa kiasi cha <b>Tzs. " + deni_1.text + "</b>. \nKiasi ulichopunguza ni <b>Tzs. " + kiasi_1.text + "</b> na kiasi kilichobaki ni <b>Tzs. " + baki_1.text + "</b>", parse_mode=telegram.ParseMode.HTML )
            elif i == 3 and j == 2 :
                context.bot.send_message(chat_id=update.message.chat_id, text="2. Control number <b>" + cn_2.text + "</b> inadaiwa kiasi cha <b>Tzs. " + deni_2.text + "</b>. \nKiasi ulichopunguza ni <b>Tzs. " + kiasi_2.text + "</b> na kiasi kilichobaki ni <b>Tzs. " + baki_2.text + "</b>", parse_mode=telegram.ParseMode.HTML )
            elif i == 5 and j == 2 :
                context.bot.send_message(chat_id=update.message.chat_id, text="3. Control number <b>" + cn_3.text + "</b> inadaiwa kiasi cha <b>Tzs. " + deni_3.text + "</b>. \nKiasi ulichopunguza ni <b>Tzs. " + kiasi_3.text + "</b> na kiasi kilichobaki ni <b>Tzs. " + baki_3.text + "</b>", parse_mode=telegram.ParseMode.HTML )





        # for value in celtext:
        #     if value.text != "":
        #         context.bot.send_message(chat_id=update.message.chat_id, text="Cell Value of row number " + str(i) + " and column number " + str(j) + " Is " + value.text)



    # send result message back

    context.bot.send_message(chat_id=update.message.chat_id, text="Asante kwa kuniamini. \n\nNiunganishe na mtu unaeona kwamba huduma hii itamfaa kwa kumtumia ujumbe huu na kumwambia abonyeze <a href='t.me/MalipoBot'>HAPA</a> nimhudumie.", parse_mode=telegram.ParseMode.HTML )
    context.bot.send_message(chat_id=update.message.chat_id, text="Pia kama wewe ni mpangaji au mwenye nyumba, usisite kushiriki kwenye group la <b><a href='t.me/+JM4XwO7uVeY4OTE8'>INAPANGISHWA</a></b> kuwajulisha wanachama endapo eneo ulipo litakua wazi. Lengo ni kuepuka gharama za udalali.", parse_mode=telegram.ParseMode.HTML )


def main():
    # Create updater and pass in Bot's auth key. 
    updater = Updater('TOKEN', use_context=True)
    # Get dispatcher to register handlers
    dispatcher = updater.dispatcher
    # answer commands
    dispatcher.add_handler(CommandHandler('start', start))
    dispatcher.add_handler(CommandHandler('mwanzo', mwanzo))
    dispatcher.add_handler(CommandHandler('maegesho', maegesho))
    # start the bot
    updater.start_polling()
    # Stop
    updater.idle()

if __name__ == '__main__':
    main()
