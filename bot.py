import os
import random

from dotenv import load_dotenv
from discord.ext import commands
import discord

load_dotenv()
'''Token in .env file will be placed here'''
TOKEN = os.getenv('DISCORD_TOKEN')
'''This will display the help comands, with 'Main Comands, when people do !help'''
help_command = commands.DefaultHelpCommand(no_category='Main Commands')
'''This sets the prefix that people will use to use a command '!''''
bot = commands.Bot(command_prefix='!',description = 'Commands', help_command = help_command)

'''bot.event will run as soon as the bot is turned on'''
@bot.event
async def on_ready():
    '''Will return in the command promp , that the bot is online'''
    print(f'{bot.user.name} has connected to Discord!')

'''set a bot command for users to use, in this example !hello is the command'''
@bot.command(name='hello', help=' -Response with a welcome comment') '''help= will show the description of the command of what it does in the !help table'''
async def welcome(ctx):
    '''I added some responses that will be defined to the variable same'''
    same = 'Hey ' + str(ctx.author.mention), 'Hey Baby', 'Hellooo!', 'Eat Shit ' + str(ctx.author.mention) '''here ctx.author.mention will @ the author of the command'''
    '''using the random module will pick a random choice'''
    response = random.choice(same)
    '''sends the response to the user'''
    await ctx.send(response)

@bot.command(name='send', help=' -This will send money to someone.')
async def sharing(ctx, who, share: int):
    print('Send Command ' + str(ctx.author))
    my_file = open("MoneyBank.txt")
    string_list = my_file.readlines()
    my_file.close()
    clean_list = []
    who = str(who).strip('<>')
    who = str(who).strip('@!')
    who = str(who).strip('@&')
    username = await bot.fetch_user(who)
    for i in string_list:
        clean_list.append(i.strip())
    print(clean_list)
    if str(ctx.author) not in clean_list:
        await ctx.send('You do not own a Bank Account ' + ctx.author.mention + ' please use "!new"')

    else:
        x = clean_list.index(str(ctx.author))
        y = clean_list[x + 1].strip()
        if int(y) < share:
            await ctx.send("You don't have enough to send that much idiot")
        elif share <= 0:
            await ctx.send("You can't send that much moron")
        elif ctx.author == username:
            await ctx.send("You can't send money to your self moron.")
        else:
            my_file = open("MoneyBank.txt")
            string_list = my_file.readlines()
            my_file.close()
            clean_list = []
            for i in string_list:
                clean_list.append(i.strip())
            x = clean_list.index(str(ctx.author))
            string_list[x + 1].strip()
            string_list[x + 1] = str(int(string_list[x + 1]) - share)
            if (x + 2) == len(string_list):
                my_file = open("MoneyBank.txt", "w")
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()
            else:
                string_list[x + 1] += str('\n')
                my_file = open("MoneyBank.txt", "w")
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()
            my_file = open("MoneyBank.txt")
            string_list = my_file.readlines()
            my_file.close()
            clean_list = []
            for i in string_list:
                clean_list.append(i.strip())
            x = clean_list.index(str(username))
            string_list[x + 1].strip()
            string_list[x + 1] = str(int(string_list[x + 1]) + share)
            if (x + 2) == len(string_list):
                my_file = open("MoneyBank.txt", "w")
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()
            else:
                string_list[x + 1] += str('\n')
                my_file = open("MoneyBank.txt", "w")
                new_file_contents = "".join(string_list)
                my_file.write(new_file_contents)
                my_file.close()
            await ctx.send("Sent $" + "{:,}".format(share) + ' to ' + str(username))

@bot.command(name='admin', help=' -This will send money to someone.')
async def admin(ctx, who, share: int):
    print('Admin ' + str(ctx.author))
    if ctx.author == await bot.fetch_user(299579178104258563):
        who = str(who).strip('<>')
        who = str(who).strip('@!')
        who = str(who).strip('@&')
        username = await bot.fetch_user(who)
        my_file = open("MoneyBank.txt")
        string_list = my_file.readlines()
        my_file.close()
        clean_list = []
        for i in string_list:
            clean_list.append(i.strip())
        x = clean_list.index(str(username))
        string_list[x + 1].strip()
        string_list[x + 1] = str(int(string_list[x + 1]) + share)
        y = int(string_list[x + 1].strip())
        if (x + 2) == len(string_list):
            my_file = open("MoneyBank.txt", "w")
            new_file_contents = "".join(string_list)
            my_file.write(new_file_contents)
            my_file.close()
        else:
            string_list[x + 1] += str('\n')
            my_file = open("MoneyBank.txt", "w")
            new_file_contents = "".join(string_list)
            my_file.write(new_file_contents)
            my_file.close()
        await ctx.send("Sent $" + "{:,}".format(share) + ' to ' + str(username))
    else:
        await ctx.send("You can't use this command")

class Gambling(commands.Cog):

    @commands.command(name='new', help='-Makes you a bank account!')
    async def NewBank(self, ctx):
        print('New Command ' + str(ctx.author))
        not_new = 0
        f = open("MoneyBank.txt", 'r')
        for line in f:
            if str(ctx.author) == line.strip():
                await ctx.send('You are not New ' + ctx.author.mention + ' you already have an account -_-')
                not_new += 1
                break

        if not_new == 0:
            f = open("MoneyBank.txt", "a")
            f.write('\n' + str(ctx.author))
            f.write('\n' + str(0))
            f.close()
            await ctx.send('Bank Account Created!' + ctx.author.mention)

    @commands.command(name='bal', help=' - Well show the amount in your Bank')
    async def bank(self, ctx):
        print('bal command ' + str(ctx.author))
        my_file = open("MoneyBank.txt")
        string_list = my_file.readlines()
        my_file.close()
        clean_list = []
        for i in string_list:
            clean_list.append(i.strip())
        x = clean_list.index(str(ctx.author))
        y = int(clean_list[x + 1].strip())
        y = ctx.author.mention + ' Balance is: $' + "{:,}".format(y)
        y = str(y).strip('()')
        y = str(y).replace("'", '')
        await ctx.send(y)

    @commands.command(name='beg', help=' -You go to the streets to beg for a spare coin')
    @commands.cooldown(1, 30, commands.BucketType.user)
    async def begging(self, ctx):
        my_file = open("MoneyBank.txt")
        string_list = my_file.readlines()
        my_file.close()
        clean_list = []
        for i in string_list:
            clean_list.append(i.strip())
        x = clean_list.index(str(ctx.author))
        y = int(clean_list[x + 1].strip())
        more = random.choice(range(0, 10000))
        print(more)
        string_list[x + 1].strip()
        await ctx.send('Given: ' + str(more))
        string_list[x + 1] = str(int(string_list[x + 1]) + more)
        balance = 'New Balance: $' + "{:,}".format(int(string_list[x + 1]))
        if (x + 2) == len(string_list):
            my_file = open("MoneyBank.txt", "w")
            new_file_contents = "".join(string_list)
            my_file.write(new_file_contents)
            my_file.close()
        else:
            string_list[x + 1] += str('\n')
            my_file = open("MoneyBank.txt", "w")
            new_file_contents = "".join(string_list)
            my_file.write(new_file_contents)
            my_file.close()
        balance = str(balance).strip('()')
        balance = str(balance).replace("'", '')
        balance = str(balance).strip(",")
        await ctx.send(balance + ' ' + str(ctx.author.mention))
        
        
    @commands.command(name='megabeg', help=' -You go to the streets to beg for silver')
    @commands.cooldown(1, 3600, commands.BucketType.user)
    async def beggingMega(self, ctx):
        my_file = open("MoneyBank.txt")
        string_list = my_file.readlines()
        my_file.close()
        clean_list = []
        for i in string_list:
            clean_list.append(i.strip())
        x = clean_list.index(str(ctx.author))
        y = int(clean_list[x + 1].strip())
        more = random.choice(range(100000, 500000))
        print(more)
        string_list[x + 1].strip()
        await ctx.send('Given: ' + str(more))
        string_list[x + 1] = str(int(string_list[x + 1]) + more)
        balance = 'New Balance: $' + "{:,}".format(int(string_list[x + 1]))
        if (x + 2) == len(string_list):
            my_file = open("MoneyBank.txt", "w")
            new_file_contents = "".join(string_list)
            my_file.write(new_file_contents)
            my_file.close()
        else:
            string_list[x + 1] += str('\n')
            my_file = open("MoneyBank.txt", "w")
            new_file_contents = "".join(string_list)
            my_file.write(new_file_contents)
            my_file.close()
        balance = str(balance).strip('()')
        balance = str(balance).replace("'", '')
        balance = str(balance).strip(",")
        await ctx.send(balance + ' ' + str(ctx.author.mention))
        
        
        
        
    @commands.command(name='ultrabeg', help=' -You go to the streets to beg for gold')
    @commands.cooldown(1, 86400, commands.BucketType.user)
    async def beggingUltra(self, ctx):
        my_file = open("MoneyBank.txt")
        string_list = my_file.readlines()
        my_file.close()
        clean_list = []
        for i in string_list:
            clean_list.append(i.strip())
        x = clean_list.index(str(ctx.author))
        y = int(clean_list[x + 1].strip())
        more = random.choice(range(1000000, 2000000))
        print(more)
        string_list[x + 1].strip()
        await ctx.send('Given: ' + str(more))
        string_list[x + 1] = str(int(string_list[x + 1]) + more)
        balance = 'New Balance: $' + "{:,}".format(int(string_list[x + 1]))
        if (x + 2) == len(string_list):
            my_file = open("MoneyBank.txt", "w")
            new_file_contents = "".join(string_list)
            my_file.write(new_file_contents)
            my_file.close()
        else:
            string_list[x + 1] += str('\n')
            my_file = open("MoneyBank.txt", "w")
            new_file_contents = "".join(string_list)
            my_file.write(new_file_contents)
            my_file.close()
        balance = str(balance).strip('()')
        balance = str(balance).replace("'", '')
        balance = str(balance).strip(",")
        await ctx.send(balance + ' ' + str(ctx.author.mention))


    @commands.command(name='challenge', help=' -Roll dice against someone, Ex !challenge @user bet')
    async def fight(self, ctx, who, bet: int):
        who = str(who).strip('<>')
        who = str(who).strip('@!')
        who = str(who).strip('@&')
        username = await bot.fetch_user(who)
        my_file = open("MoneyBank.txt")
        string_list = my_file.readlines()
        my_file.close()
        clean_list = []
        for i in string_list:
            clean_list.append(i.strip())
        print(clean_list)
        if str(ctx.author) not in clean_list:
            await ctx.send('You do not own a Bank Account ' + ctx.author.mention + ' please use "!new"')
        elif str(username) not in clean_list:
            await ctx.send(str(username) + ' does not own a Bank Account ' + ctx.author.mention + ' tell them to use "!new"')
        else:
            x = clean_list.index(str(ctx.author))
            y = clean_list[x + 1].strip()
            challenged = clean_list.index(str(username))
            c = clean_list[challenged + 1].strip()
            if (int(y) < bet) and (bet != 1):
                await ctx.send("You don't have enough to bet that much idiot")
            elif (int(c) < bet) and (bet != 1):
                await ctx.send("The poor fuck doesn't have enough to bet that much")
            elif username == ctx.author:
                await ctx.send("You can't challenge yourself dumbfuck")
            else:
                def check(m):
                    return m.content == "accept"

                msg = await bot.wait_for("message", check=check, timeout=60)
                if username == msg.author:
                    my_file = open("MoneyBank.txt")
                    string_list = my_file.readlines()
                    my_file.close()
                    clean_list = []
                    for i in string_list:
                        clean_list.append(i.strip())
                    print(clean_list)
                    total = 0
                    total_c = 0
                    comp_1 = 0
                    comp_2 = 0
                    dice_1 = 0
                    dice_2 = 0
                    for i in range(1, 3):
                        choices = [1, 2, 3, 4, 5, 6]
                        dice = random.choice(choices)
                        if i == 1:
                            comp_1 += dice
                        else:
                            comp_2 += dice
                        total_c += dice
                    for i in range(1, 3):
                        choices = [1, 2, 3, 4, 5, 6]
                        dice = random.choice(choices)
                        if i == 1:
                            dice_1 += dice
                        else:
                            dice_2 += dice
                        total += dice
                    if total_c < total:
                        response = '**You won!**'
                        my_file = open("MoneyBank.txt")
                        string_list = my_file.readlines()
                        my_file.close()
                        clean_list = []
                        for i in string_list:
                            clean_list.append(i.strip())
                        x = clean_list.index(str(ctx.author))
                        string_list[x + 1].strip()
                        string_list[x + 1] = str(int(string_list[x + 1]) + (bet *2))
                        y = int(string_list[x + 1].strip())
                        balance = 'New Balance: $' + "{:,}".format(y)
                        if (x + 2) == len(string_list):
                            my_file = open("MoneyBank.txt", "w")
                            new_file_contents = "".join(string_list)
                            my_file.write(new_file_contents)
                            my_file.close()
                        else:
                            string_list[x + 1] += str('\n')
                            my_file = open("MoneyBank.txt", "w")
                            new_file_contents = "".join(string_list)
                            my_file.write(new_file_contents)
                            my_file.close()
                            for i in string_list:
                                clean_list.append(i.strip())
                            x = clean_list.index(str(username))
                            string_list[x + 1].strip()
                            string_list[x + 1] = str(int(string_list[x + 1]) - bet)
                            if (x + 2) == len(string_list):
                                my_file = open("MoneyBank.txt", "w")
                                new_file_contents = "".join(string_list)
                                my_file.write(new_file_contents)
                                my_file.close()
                            else:
                                string_list[x + 1] += str('\n')
                                my_file = open("MoneyBank.txt", "w")
                                new_file_contents = "".join(string_list)
                                my_file.write(new_file_contents)
                                my_file.close()
                        embed = discord.Embed(title="Dice Roll | Competitor: " + str(ctx.author), description=
                                              "**" + str(username) + "**\n" +
                                              "Dice 1 = " + '**' + str(comp_1) + '**' + '\n'
                                              "Dice 2 = " + '**' + str(comp_2) + '**' + '\n'
                                              "Total = " + '**' + str(total_c) + '**' + '\n' + '\n' +
                                              '**' + str(ctx.author) + '**' + ":"
                                              "\nDice 1 = " + '**' + str(dice_1) + '**' + '\n'
                                              "Dice 2 = " + '**' + str(dice_2) + '**' + '\n'
                                              "Total = " + '**' + str(total) + '**' + '\n' +
                                              response + ' ' + str(ctx.author.mention) +
                                              "\n" + str(balance), color=44336)
                        await ctx.send(embed=embed)
                    elif total_c > total:
                        response = '**You lost!**'
                        my_file = open("MoneyBank.txt")
                        string_list = my_file.readlines()
                        my_file.close()
                        clean_list = []
                        for i in string_list:
                            clean_list.append(i.strip())
                        x = clean_list.index(str(ctx.author))
                        string_list[x + 1].strip()
                        string_list[x + 1] = str(int(string_list[x + 1]) - bet)
                        y = int(string_list[x + 1].strip())
                        balance = 'New Balance: $' + "{:,}".format(y)
                        if (x + 2) == len(string_list):
                            my_file = open("MoneyBank.txt", "w")
                            new_file_contents = "".join(string_list)
                            my_file.write(new_file_contents)
                            my_file.close()
                        else:
                            string_list[x + 1] += str('\n')
                            my_file = open("MoneyBank.txt", "w")
                            new_file_contents = "".join(string_list)
                            my_file.write(new_file_contents)
                            my_file.close()
                            for i in string_list:
                                clean_list.append(i.strip())
                            x = clean_list.index(str(username))
                            string_list[x + 1].strip()
                            string_list[x + 1] = str(int(string_list[x + 1]) + (bet*2))
                            if (x + 2) == len(string_list):
                                my_file = open("MoneyBank.txt", "w")
                                new_file_contents = "".join(string_list)
                                my_file.write(new_file_contents)
                                my_file.close()
                            else:
                                string_list[x + 1] += str('\n')
                                my_file = open("MoneyBank.txt", "w")
                                new_file_contents = "".join(string_list)
                                my_file.write(new_file_contents)
                                my_file.close()
                        embed = discord.Embed(title="Dice Roll | Competitor: " + str(ctx.author), description=
                                              "**" + str(username) + "**\n" +
                                              "Dice 1 = " + '**' + str(comp_1) + '**' + '\n'
                                              "Dice 2 = " + '**' + str(comp_2) + '**' + '\n'
                                              "Total = " + '**' + str(total_c) + '**' + '\n' + '\n' +
                                              '**' + str(ctx.author) + '**' + ":"
                                              "\nDice 1 = " + '**' + str(dice_1) + '**' + '\n'
                                              "Dice 2 = " + '**' + str(dice_2) + '**' + '\n'
                                              "Total = " + '**' + str(total) + '**' + '\n' +
                                              response + ' ' + str(ctx.author.mention) +
                                              "\n" + str(balance), color=44336)
                        await ctx.send(embed=embed)
                    elif total_c == total:
                        response = '**You Tied!**'
                        my_file = open("MoneyBank.txt")
                        string_list = my_file.readlines()
                        my_file.close()
                        clean_list = []
                        for i in string_list:
                            clean_list.append(i.strip())
                        x = clean_list.index(str(ctx.author))
                        string_list[x + 1].strip()
                        string_list[x + 1] = str(int(string_list[x + 1]))
                        y = int(string_list[x + 1].strip())
                        balance = 'New Balance: $' + "{:,}".format(y)
                        if (x + 2) == len(string_list):
                            my_file = open("MoneyBank.txt", "w")
                            new_file_contents = "".join(string_list)
                            my_file.write(new_file_contents)
                            my_file.close()
                        else:
                            string_list[x + 1] += str('\n')
                            my_file = open("MoneyBank.txt", "w")
                            new_file_contents = "".join(string_list)
                            my_file.write(new_file_contents)
                            my_file.close()
                            for i in string_list:
                                clean_list.append(i.strip())
                            x = clean_list.index(str(username))
                            string_list[x + 1].strip()
                            string_list[x + 1] = str(int(string_list[x + 1]))
                            if (x + 2) == len(string_list):
                                my_file = open("MoneyBank.txt", "w")
                                new_file_contents = "".join(string_list)
                                my_file.write(new_file_contents)
                                my_file.close()
                            else:
                                string_list[x + 1] += str('\n')
                                my_file = open("MoneyBank.txt", "w")
                                new_file_contents = "".join(string_list)
                                my_file.write(new_file_contents)
                                my_file.close()
                        embed = discord.Embed(title="Dice Roll | Competitor: " + str(ctx.author), description=
                                              "**" + str(username) + "**\n" +
                                              "Dice 1 = " + '**' + str(comp_1) + '**' + '\n'
                                              "Dice 2 = " + '**' + str(comp_2) + '**' + '\n'
                                              "Total = " + '**' + str(total_c) + '**' + '\n' + '\n' +
                                              '**' + str(ctx.author) + '**' + ":"
                                              "\nDice 1 = " + '**' + str(dice_1) + '**' + '\n'
                                              "Dice 2 = " + '**' + str(dice_2) + '**' + '\n'
                                              "Total = " + '**' + str(total) + '**' + '\n' +
                                              response + ' ' + str(ctx.author.mention) +
                                              "\n" + str(balance), color=44336)
                        await ctx.send(embed=embed)
                else:
                    await ctx.send("You weren't challenged idiot")

    @commands.command(name='roll', help='-Simulates rolling dice agaisnt Arnold|Ex: !roll_dice <total> <bet>')
    @commands.cooldown(rate=2, per=2)
    async def roll(self, ctx, bet: int):
        print('Roll Command ' + str(ctx.author))
        my_file = open("MoneyBank.txt")
        string_list = my_file.readlines()
        my_file.close()
        clean_list = []
        for i in string_list:
            clean_list.append(i.strip())
        print(clean_list)
        if str(ctx.author) not in clean_list:
            await ctx.send('You do not own a Bank Account ' + ctx.author.mention + ' please use "!new"')

        else:
            x = clean_list.index(str(ctx.author))
            y = clean_list[x + 1].strip()
            if (int(y) < bet) and (bet != 1):
                await ctx.send("You don't have enough to bet that much idiot")

            else:
                total = 0
                total_c = 0
                comp_1 = 0
                comp_2 = 0
                dice_1 = 0
                dice_2 = 0
                for i in range(1, 3):
                    choices = [1, 2, 2, 2, 3, 4, 5, 5, 6, 6]
                    dice = random.choice(choices)
                    if i == 1:
                        comp_1 += dice
                    else:
                        comp_2 += dice
                    total_c += dice
                for i in range(1, 3):
                    choices = [1, 2, 2, 3, 3, 4, 5, 6]
                    dice = random.choice(choices)
                    if i == 1:
                        dice_1 += dice
                    else:
                        dice_2 += dice

                    total += dice
                if total_c < total:
                    responses = '**You won!**', '**You won.. Poor Arnold**', '**Taking Money from an Old Man..** ', '**Yikes you Won**'
                    response = random.choice(responses)
                    my_file = open("MoneyBank.txt")
                    string_list = my_file.readlines()
                    my_file.close()
                    clean_list = []
                    for i in string_list:
                        clean_list.append(i.strip())
                    x = clean_list.index(str(ctx.author))
                    string_list[x + 1].strip()
                    if (total - total_c) > 5:
                        string_list[x + 1] = str(int(string_list[x + 1]) + int(bet * 3))
                    elif (total - total_c) > 3:
                        string_list[x + 1] = str(int(string_list[x + 1]) + int(bet * 2.5))
                    else:
                        string_list[x + 1] = str(int(string_list[x + 1]) + (bet * 2))
                    y = int(string_list[x + 1].strip())
                    balance = 'New Balance: $' + "{:,}".format(y)
                    if (x + 2) == len(string_list):
                        my_file = open("MoneyBank.txt", "w")
                        new_file_contents = "".join(string_list)
                        my_file.write(new_file_contents)
                        my_file.close()
                    else:
                        string_list[x + 1] += str('\n')
                        my_file = open("MoneyBank.txt", "w")
                        new_file_contents = "".join(string_list)
                        my_file.write(new_file_contents)
                        my_file.close()
                    embed = discord.Embed(title="Dice Roll | Competitor: " + str(ctx.author), description=
                                                "**Arnold's Roll:**\n"
                                                "Dice 1 = " + '**' + str(comp_1) + '**' + '\n'
                                                "Dice 2 = " + '**' + str(comp_2) + '**' + '\n'
                                                "Total = " + '**' + str(total_c) + '**' + '\n' + '\n' +
                                                '**' + str(ctx.author) + '**' + ":"
                                                "\nDice 1 = " + '**' + str(dice_1) + '**' + '\n'
                                                "Dice 2 = " + '**' + str(dice_2) + '**' + '\n'
                                                "Total = " + '**' + str(total) + '**' + '\n' +
                                                response + ' ' + str(ctx.author.mention) +
                                                "\n" + str(balance), color=7289)
                    await ctx.send(embed=embed)
                elif total_c == total:
                    my_file = open("MoneyBank.txt")
                    string_list = my_file.readlines()
                    my_file.close()
                    clean_list = []
                    for i in string_list:
                        clean_list.append(i.strip())
                    x = clean_list.index(str(ctx.author))
                    string_list[x + 1].strip()
                    string_list[x + 1] = str(int(string_list[x + 1]))
                    y = int(string_list[x + 1].strip())
                    balance = 'New Balance: $' + "{:,}".format(y)
                    if (x + 2) == len(string_list):
                        my_file = open("MoneyBank.txt", "w")
                        new_file_contents = "".join(string_list)
                        my_file.write(new_file_contents)
                        my_file.close()
                    else:
                        string_list[x + 1] += str('\n')
                        my_file = open("MoneyBank.txt", "w")
                        new_file_contents = "".join(string_list)
                        my_file.write(new_file_contents)
                        my_file.close()
                    embed = discord.Embed(title="Dice Roll | Competitor: " + str(ctx.author), description=
                                                "**Arnold's Roll:**\n"
                                                "Dice 1 = " + '**' + str(comp_1) + '**' + '\n'
                                                "Dice 2 = " + '**' + str(comp_2) + '**' + '\n'
                                                "Total = " + '**' + str(total_c) + '**' + '\n' + '\n' +
                                                '**' + str(ctx.author) + '**' + ":"
                                                "\nDice 1 = " + '**' + str(dice_1) + '**' + '\n'
                                                "Dice 2 = " + '**' + str(dice_2) + '**' + '\n'
                                                "Total = " + '**' + str(total) + '**' + '\n'
                                                "You Tied! " + str(ctx.author.mention) +
                                                "\n" + str(balance), color=7289)
                    await ctx.send(embed=embed)

                elif total_c > total:
                    responses = 'You lost moron', 'Imagine Losing to a Machine!', 'You actually lost LOL', 'Yikes losing'
                    response = random.choice(responses)
                    my_file = open("MoneyBank.txt")
                    string_list = my_file.readlines()
                    my_file.close()
                    clean_list = []
                    for i in string_list:
                        clean_list.append(i.strip())
                    x = clean_list.index(str(ctx.author))
                    string_list[x + 1].strip()
                    string_list[x + 1] = str(int(string_list[x + 1]) - bet)
                    y = int(string_list[x + 1].strip())
                    balance = 'New Balance: $' + "{:,}".format(y)
                    if (x + 2) == len(string_list):
                        my_file = open("MoneyBank.txt", "w")
                        new_file_contents = "".join(string_list)
                        my_file.write(new_file_contents)
                        my_file.close()
                    else:
                        string_list[x + 1] += str('\n')
                        my_file = open("MoneyBank.txt", "w")
                        new_file_contents = "".join(string_list)
                        my_file.write(new_file_contents)
                        my_file.close()
                    embed = discord.Embed(title="Dice Roll | Competitor: " + str(ctx.author), description=
                                                "**Arnold's Roll:**\n"
                                                "Dice 1 = " + '**' + str(comp_1) + '**' + '\n'
                                                "Dice 2 = " + '**' + str(comp_2) + '**' + '\n'
                                                "Total = " + '**' + str(total_c) + '**' + '\n' + '\n' +
                                                '**' + str(ctx.author) + '**' + ":"
                                                "\nDice 1 = " + '**' + str(dice_1) + '**' + '\n'
                                                "Dice 2 = " + '**' + str(dice_2) + '**' + '\n'
                                                "Total = " + '**' + str(total) + '**' + '\n' + '**' +
                                                response + '**' + ' ' + str(ctx.author.mention) +
                                                "\n" + str(balance), color=7289)
                    await ctx.send(embed=embed)

bot.add_cog(Gambling())
bot.run(TOKEN)
