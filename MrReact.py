import discord, json, os

from discord.ext import commands
from colorama import Fore
from datetime import datetime

# ---------------------------------------------------------------- Config ----------------------------------------------------------------

try:
    with open("react.json", "r") as confjson: 
	    configData = json.load(confjson)
except:
    pass

def EditConfig(key, value):
    configData[f"{key}"] = value 
    with open("react.json", "w") as outfile:
        json.dump(configData, outfile, indent = 4) 

# ---------------------------------------------------------------- Bot ----------------------------------------------------------------

MrReact = commands.Bot(command_prefix=configData['Prefix'], self_bot=True, help_command=None, status=discord.Status.do_not_disturb)

# ---------------------------------------------------------------- Handling/Events ----------------------------------------------------------------

@MrReact.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Error{Fore.WHITE}]{Fore.WHITE} [+] You are missing input requirements.')
    elif isinstance(error, discord.HTTPException):
       print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Error{Fore.WHITE}]{Fore.WHITE} [+] You are ratelimited | Request could not be sent.')
    elif isinstance(error, commands.CommandNotFound):
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Error{Fore.WHITE}]{Fore.WHITE} [+] That is not a command. Do {MrReact.command_prefix}help for commands')
    else:
        print(f'[{datetime.now().strftime("%H:%M:%S")}] [{Fore.GREEN}Info{Fore.WHITE}] [{Fore.LIGHTRED_EX}Error{Fore.WHITE}]{Fore.WHITE} [+] {error}')

@MrReact.event
async def on_message(message):
    await MrReact.process_commands(message)

    if message.author == MrReact.user: 
        return
    
    if configData["UserID"] == "0": 
        return 
       
    if message.author.id == int(configData["UserID"]) and configData["IsNerd"] == "On": 
        await message.add_reaction("🇳")
        await message.add_reaction("🇪")
        await message.add_reaction("🇷")
        await message.add_reaction("🇩") 
        await message.add_reaction("🤓")
    elif message.author.id == int(configData["UserID"]) and configData["Emoji"] == "":
        await message.add_reaction("🤓")
    elif message.author.id == int(configData["UserID"]) :
        await message.add_reaction(configData['Emoji'])

# ---------------------------------------------------------------- Commands ----------------------------------------------------------------    

@MrReact.command()
async def cls(ctx): 
    await ctx.message.delete()
    os.system("cls")
    logo()

@MrReact.command()
async def toggle(ctx, item, value):
    await ctx.message.delete() 
    match item:
        case "id":  
            EditConfig("UserID", value)
            await ctx.send(f"Updated Config, Added User To The Auto React List!", delete_after=5)
        case "emoji":
            EditConfig("Emoji", value)
            await ctx.send(f"Updated Config, Emoji Updated!", delete_after=5)
        case "nerdmode":
            EditConfig("IsNerd", value)
            await ctx.send(f"Updated Config, Nerd Mode Active!!", delete_after=5)  
        case "prefix":
            EditConfig("Prefix", value) 
            await ctx.send(f"Updated Config, Prefix Changed To: {value}, You need to restart!", delete_after=5)  

# ---------------------------------------------------------------- Entry Point ----------------------------------------------------------------

def logo():
    os.system("cls")
    width = os.get_terminal_size().columns
    os.system('title MrReact v6.9')
    print(f"You have {Fore.LIGHTGREEN_EX}Successfully{Fore.WHITE} logged in! Please Enjoy Using {Fore.LIGHTYELLOW_EX}MrReact{Fore.WHITE} v6.9.")
    print(Fore.LIGHTMAGENTA_EX+'  ⣐⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'  ⣿⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣤⣶⣦⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'⣿⣅⡠⠃⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'⢹⣿⣇⡀⠀⠀⠀⢀⣤⣤⣤⣾⣿⣿⣿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'⢸⣿⣿⣷⡀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣶'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣤⡀⠀⠀⠀⣀⣀⣤⣾'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇'.center(width))
    print(Fore.LIGHTMAGENTA_EX+'⠀⠉⠙⠉⠉⠁⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⠟⠋⠁⠀⠀'.center(width))
    print(Fore.LIGHTGREEN_EX+f'     Troll Like The Best {Fore.WHITE}Or{Fore.LIGHTGREEN_EX} Get Troll Like The Rest'.center(width))
    print(Fore.LIGHTGREEN_EX+f'                By: {Fore.LIGHTCYAN_EX}Joshua{Fore.WHITE}({Fore.YELLOW}UrfingPoor{Fore.WHITE})\n\n'.center(width))
   
def main():
    os.system("cls")
    print(f'{Fore.LIGHTYELLOW_EX}    Options: 1. Login | 2. Change Discord Token | 3. exit{Fore.WHITE}\n'.center(os.get_terminal_size().columns))
    match input(f"{Fore.WHITE}What's Your Choice: "):
        case "1":
            logo()
            MrReact.run(configData["Token"])   
            main()
        case "2":
            EditConfig("Token", input("Enter your discord token: ")) 
            main()
        case "3":
            exit()

if __name__ == "__main__":
	main()