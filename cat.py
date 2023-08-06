import requests
from telethon.sync import TelegramClient, events

API_ID = '1509431'
API_HASH = '5d08c3603085ecea80b52deacf238204'
BOT_TOKEN = '6065534515:AAHksB5Ov268rMcKdWU_95uXd4cxeGq8he8'

bot = TelegramClient('bot_session', API_ID, API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(pattern=r'^meow$', incoming=True))
async def handle_meow(event):
    try:
        cat_fact_url = 'https://catfact.ninja/fact'
        cat_image_url = 'https://api.thecatapi.com/v1/images/search'

        # Get a random cat fact
        cat_fact_response = requests.get(cat_fact_url)
        cat_fact = cat_fact_response.json().get('fact', 'Sorry, no cat facts available right now.')

        # Get the user's first name
        user_first_name = event.sender.first_name

        # Prepare the response message with cat fact and personalized username
        response_message = f"😺 Did you know, {user_first_name}? Here's a cat fact to make you purr with joy:\n\n{cat_fact}"

        # Get a random cat image
        cat_image_response = requests.get(cat_image_url)
        cat_image = cat_image_response.json()[0]['url']

        # Send the response message and the cat image together
        await event.respond(response_message, file=cat_image)

    except requests.RequestException as e:
        await event.respond("Oops! Something went wrong while fetching cat data. Please try again later.")


@bot.on(events.NewMessage(pattern='^start$', incoming=True))
async def handle_start(event):
    await event.respond('meow')


bot.run_until_disconnected()

