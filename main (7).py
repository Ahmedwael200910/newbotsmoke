import requests,re
import telebot
from telebot import types
from gatet import Tele
import os
token = "7064122761:AAGFibmlDdGgZ1HujdX5kmjoZHD8Wj31Q20"
bot=telebot.TeleBot(token,parse_mode="HTML")
@bot.message_handler(commands=["start"])
def start(message):
	mo=requests.get('https://t.me/gg_r0h/2').text
	chat_id = message.chat.id
	if not str(chat_id) in mo:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @B_9_BB")
		return
	bot.reply_to(message,"Send the file now \n ارسل الملف الان")
@bot.message_handler(content_types=["document"])
def main(message):
	mo=requests.get('https://t.me/gg_r0h/2').text
	chat_id = message.chat.id
	if not str(chat_id) in mo:
		bot.reply_to(message, "You cannot use the bot to contact developers to purchase a bot subscription @B_9_BB")
		return
	dd = 0
	live = 0
	ko = (bot.reply_to(message, "Checking Your Cards...⌛").message_id)
	ee = bot.download_file(bot.get_file(message.document.file_id).file_path)
	with open("combo.txt", "wb") as w:
		w.write(ee)
	try:
		with open("combo.txt", 'r') as file:
			lino = file.readlines()
			total = len(lino)
			for cc in lino:
				current_dir = os.getcwd()
				for filename in os.listdir(current_dir):
					if filename.endswith(".stop"):
						bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗦𝗧𝗢𝗣𝗣𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @B_9_BB')
						os.remove('stop.stop')
						return
				try:
					headers = {
					'Referer': 'https://bincheck.io/',
					    'Upgrade-Insecure-Requests': '1',
					    'User-Agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36',
					    'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"',
					    'sec-ch-ua-mobile': '?1',
					    'sec-ch-ua-platform': 'Android',
					}
					response = requests.get('https://bincheck.io/details/' + cc[:6], headers=headers)
					html_text = response.text
					    
					card_brand_pattern = r'Card Brand</td>\n<td width="65%" class="p-2">\s*(\w+)'
					card_type_pattern = r'Card Type</td>\n<td width="65%" class="p-2">\s*(\w+)'
					card_level_pattern = r'Card Level</td>\n<td width="65%" class="p-2">\s*(\w+)'
					issuer_name_pattern = r'Issuer Name / Bank</td>\n<td width="65%" class="p-2">\s*<a[^>]*>([^<]+)'
					iso_country_name_pattern = r'ISO Country Name</td>\n<td width="65%" class="p-2">\s*<a[^>]*>([^<]+)'
					iso_country_code_pattern = r'ISO Country Code A2</td>\n<td width="65%" class="p-2">\s*(\w+)'
					card_brand_match = re.search(card_brand_pattern, html_text)
					card_brand = card_brand_match.group(1) if card_brand_match else "------"
					card_type_match = re.search(card_type_pattern, html_text)
					card_type = card_type_match.group(1) if card_type_match else "------"
					card_level_match = re.search(card_level_pattern, html_text)
					card_level = card_level_match.group(1) if card_level_match else "------"
					issuer_name_match = re.search(issuer_name_pattern, html_text)
					issuer_name = issuer_name_match.group(1) if issuer_name_match else "------"
					iso_country_name_match = re.search(iso_country_name_pattern, html_text)
					iso_country_name = iso_country_name_match.group(1) if iso_country_name_match else "------"
				except:
					pass

				try:
					last = str(Tele(cc))
				except Exception as e:
					print(e)
					last = "ERROR"
				mes = types.InlineKeyboardMarkup(row_width=1)
				cm1 = types.InlineKeyboardButton(f" {cc} ", callback_data='u8')
				cm2 = types.InlineKeyboardButton(f" 𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫 ✅  :  {live}  ", callback_data='x')
				cm3 = types.InlineKeyboardButton(f"  𝑰𝑵𝑺𝑼𝑭𝑭𝑰𝑪𝑰𝑬𝑵𝑻 𝑭𝑼𝑵𝑫𝑺 🥶  :  0  ", callback_data='x')
				cm4 = types.InlineKeyboardButton(f" 𝑪𝑵𝑵 🩸 : 0  ", callback_data='x')
				cm5 = types.InlineKeyboardButton(f" 𝑫𝑬𝑪𝑳𝑰𝑵𝑬𝑫 ❌ :  {dd}  ", callback_data='x')
				cm7 = types.InlineKeyboardButton(f" 𝑭𝑹𝑨𝑼𝑫 🕵🏻‍♂️ : 0 ", callback_data='x')
				cm6 = types.InlineKeyboardButton(f" 𝑹𝑰𝑺𝑲 💔  : 0 ", callback_data='x')
				cm8 = types.InlineKeyboardButton(f" 𝑻𝑶𝑻𝑨𝑳 💎   : {total} ", callback_data='x')

				mes.add(cm1,cm2,cm3, cm4, cm5, cm6,cm7)
				bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='''Wait for processing 
𝒃𝒚 ➜ @B_9_BB ''', reply_markup=mes)
				msg = f" 𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫 𝑪𝑨𝑹𝑫 ✅\n━━━━━━━━━━━━━━━━━━━━\n 𝑪𝑪:<code>{cc}</code> \n 𝑮𝑨𝑻𝑬𝑾𝑨𝒀:𝑩𝑹𝑨𝑰𝑵𝑻𝑹𝑬𝑬 𝑨𝑼𝑻𝑯 1\n𝑺𝑻𝑨𝑻𝑼𝑺 :𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫 ✅\n 𝐑𝐞𝐬𝐩𝐨𝐧𝐬𝐞: 1000: 𝑨𝑷𝑷𝑹𝑶𝑽𝑬𝑫\n━━━━━━━━━━━━━━━━━━━━\n 𝑪𝑯𝑬𝑪𝑲𝑬𝑹 𝑩𝒀 - tg://openmessage?user_id={id}[𝑷𝑹𝑬𝑴𝑰𝑼𝑴]"
				print(last)
				if "live" in last or 'Funds' in last or "Gateway Rejected: avs" in last or "Card Issuer Declined CVV" in last or "funds" in last or "successfully" in last or "Nice! New payment method added:" in last or "Duplicate card exists in the vault." in last or "Approved" in last or "Invalid postal code or street address." in last or 'Transaction Not Allowed' in last:
					live += 1
					bot.reply_to(message, msg)
				else:
					dd += 1
	except Exception as e:
		print(e)
	bot.edit_message_text(chat_id=message.chat.id, message_id=ko, text='𝗕𝗘𝗘𝗡 𝗖𝗢𝗠𝗣𝗟𝗘𝗧𝗘𝗗 ✅\n𝗕𝗢𝗧 𝗕𝗬 ➜ @B_9_BB')
@bot.callback_query_handler(func=lambda call: call.data == 'stop')
def menu_callback(call):
	with open("stop.stop", "w") as file:
		pass
print("تم تشغيل البوت")
bot.polling()
