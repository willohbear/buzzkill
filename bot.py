import discord
import random
import asyncio
from discord.ext import commands
from discord.utils import get

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name='Buzzkill server Bot!'))
    print('Bot is ready.')

@client.event
async def on_member_join(member):
    mbed = discord.Embed(
        colour = (discord.Colour.magenta()),
        title = 'Welcome Message',
        description = f'Welcome {member.mention}, enjoy your stay!'
    )
    await member.send(embed=mbed)

@client.command(aliases=['rules1'])
async def r_one(ctx):
    embed=discord.Embed(title="WELCOME TO BUZZKILL.", description="We're an 18+ mass horror crossover aimed at intermediate and advanced writers who just want to have fun! As any horror fan knows, one very important thing we need to get out of the way is that this site deals with mature and highly triggering topics. While each writer's experience with the site will vary entirely dependent on character actions, reactions, and how deep they dive into the threads -- the unpredictable can happen here. Because of this, we regretfully cannot be a trigger-free area. Therefore if you're easily triggered by any mature themes, especially those often depicted within the horror genre, we ask you to leave, asap! For your own good!\n\nThe rules are a wee bit long and mighty, but we use them to make sure everyone starts off, and remains on the same page. We wanna cover all of our bases so we don't have to use the admin voice with anyone because that's lame and we're here for the fun and keeping this well oiled machine slugging away without issue.", color=0x469b57)
    embed.set_thumbnail(url="https://avatarfiles.alphacoders.com/155/155656.png")
    embed.set_footer(text="☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ☠ ")
    embed.set_image(url="https://i.imgur.com/P8mpxgG.png")
    await ctx.send(embed=embed)

@client.command(aliases=['rules2'])
async def r_two(ctx):
    embed=discord.Embed(title="GENERAL RULES", description="Those under 18 years old are not permitted to join. All characters will be 18+ only. Anyone can die and we don’t shy away from the nitty gritty. Death will play a part in this, especially to escalate the stakes and certain situations, but it isn’t going to be the focal point. We’re going to up the ante once we get a solid core group going and regular activity but there is so much to be explored. The admins have high hopes for this and some exciting directions we want to explore, therefore we will be heavily involved in plot drops, wild cards, in game advancement via information drops, challenge wins, and much, much more! Just because you apply, it doesn’t mean you’re automatically going to be accepted. ", color=0x469b57)
    embed.set_thumbnail(url="https://avatarfiles.alphacoders.com/155/155656.png")
    await ctx.send(embed=embed)

@client.command(aliases=['rules3'])
async def r_three(ctx):
    embed=discord.Embed(title="RESPECT AND OOC", description="Life is extra enough and we’ve got a strict zero tolerance for bullshit/bullying/drama policy here. We’re all adults and we’re going to ask that maturity be brought to the table. If you’ve got a problem with someone, come to the admin team, send an ask, let us know. If someone is being shady or a complete asshole; they really don’t have a place in the group because that’s what we’re here to avoid. It literally takes no effort at all to not be an asshole. In fact, it takes more effort TO be an asshole and ain’t nobody got time for that. Drama ic? BEAUTIFUL, GIVE IT TO US! OOC? Nah fam. As a group verse, you are under no obligation to follow everyone. It’s suggested just to keep up with everything, but considering we’re all indie blogs, it’s absolutely not necessary. While it’s not mandatory, we do have a group verse discord and we will send links upon acceptance, but you are under no obligation to join or take part, it’s just a simple way to keep everyone looped in for plotting potential and such.  ", color=0x469b57)
    embed.set_thumbnail(url="https://avatarfiles.alphacoders.com/155/155656.png")
    await ctx.send(embed=embed)

@client.command(aliases=['rules4'])
async def r_four(ctx):
    embed=discord.Embed(title="WRITING AND WORD COUNT", description="While we can certainly appreciate them, one liners have no place here. We don’t have a specific word count, we request that thread posts be at least two paragraphs, which is roughly 180+ words. We require a bit more because we want to see relationships build, threads flourish, and some incredible plots unfold. Not to mention the wild cards and challenges require a bit more because they offer opportunities in game to spice things up. In terms of writing style, we ask that first person is not used. Due to the nature of this verse, all external forces, (ie; weather, ‘killers’, ect) be left to the admins. That’s not to say your character can’t hear something, or suspect things, but in terms of actual attacks or the like, we ask you leave this up to the wild cards. We also don’t want to dive right in and suddenly have nothing left to build to, so we would like to give people time to establish themselves and gradually work up to absolute beauty. As always, never godmod anyone’s character’s. You can certainly do things to other characters, but when it comes to being in control, if you’re not playing the character, DON’T WRITE THEM FOR THE OTHER PLAYER. ", color=0x469b57)
    embed.set_thumbnail(url="https://avatarfiles.alphacoders.com/155/155656.png")
    await ctx.send(embed=embed)

@client.command(aliases=['rules5'])
async def r_five(ctx):
    embed=discord.Embed(title="ACTIVITY AND INVOLVEMENT", description="Ideally, we’d really love people that could post a couple times a week and that are actually excited to progress the overall story along, as well as their actual characters. There’s so much potential for opportunities, relationships, and interesting things you don’t typically get to explore so we want members that utilize that. If you’re not feeling the group, let us know and we’ll remove you! It’s really that easy. Also if you tell us you’re a 9 on the activity scale and come around every two weeks to post once, you’re gonna get the boot. It’s super easy to tell who is into it, and who isn’t. We’re not asking for people to move mountains, but we’re going to do what we have to to keep the group alive and thriving. If you are accepted, please be sure to read the newbie checklist and track all applicable tags. ", color=0x469b57)
    embed.set_thumbnail(url="https://avatarfiles.alphacoders.com/155/155656.png")
    await ctx.send(embed=embed)

@client.command(aliases=['rules6'])
async def r_six(ctx):
    embed=discord.Embed(title="CHARACTERS", description="As of right now, we’re only accepting canon characters, though if the group would be in favor of adding originals in the future, once we have an established base, we would be happy to do so. Duplicate face claims are a thing that shouldn’t be addressed IC, and we ask people skip over the cliche twin plots and identity mix ups as this is much more of an OOC issue. Duplicate characters are not allowed. All characters that are not human will be human for this verse and everything is set in present day. Pre-established connections are totally zen! We do ask that if you join, you don’t just write with one person, ignore the premise and concept of the group though, because that’s no fun and if we see it, we aren’t opposed to throwing in a little havoc via wild card, so like, abide by the rules fam. If someone from your fandom already has an accepted character, it wouldn’t hurt to peep their application to see what they’ve done, or if any changes have been made to the fandom as a whole. For fandom stuff, it’s first come, first serve. No character is immune to death. NSFW themes will be heavily present. You also may have multiple characters within the verse so long as you can keep them active. ", color=0x469b57)
    embed.set_thumbnail(url="https://avatarfiles.alphacoders.com/155/155656.png")
    await ctx.send(embed=embed)

@client.command(aliases=['rules7'])
async def r_seven(ctx):
    embed=discord.Embed(title="ACTIONS AND KILLS", description="Characters retain next to full free will here. Obviously, they can try and escape when the going gets tough, but that wouldn’t make for an interesting verse, so realistically they won’t get far. We also have a few morally ambiguous or straight up evil characters here too. We ask that the admins do the killing by the wildcard. Your muses can still slow burn terrorize, and plant that seed of fear, and reap psychological warfare, but when it comes to making your own moves, we ask you consult us first, and even then if we have something planned, that doesn’t mean you’ll be granted the ability to do so. ", color=0x469b57)
    embed.set_thumbnail(url="https://avatarfiles.alphacoders.com/155/155656.png")
    await ctx.send(embed=embed)

@client.command(aliases=['wc'])
async def wildcard(ctx, character):
    location = ['in Cabin 3',
                'in the woods',
                'in the lake',
                'on the pier',
                'by the lake',
                'around the campfire',
                'on your way to town',
                'sleeping in your bed',
                'relaxing in the canteen',
                'fixing the electric']
    event = ['you found a dead body',
            'you heard a scream',
            'you saw something out of the corner of your eye',
            'you heard someone whisper in your ear',
            'you are starting to feel faint',
            'you are murdered',
            'the lights went out',
            'something runs past you',
            'you are suddenly very cold',
            'something brushes against you',
            'you finally get phone service',
            'you lose phone service',
            'everything goes black',
            'your nose starts bleeding',
            'you hear someone call your name',]
    people = ['alone',
            'with one other person',
            'with two other people',
            'with three or more people']
    await ctx.send(f'**PROMPT:** {character}, you are {random.choice(location)} {random.choice(people)} and {random.choice(event)}.')

@client.command()
async def purge(ctx, limit: int = 100):
    deleted = await ctx.channel.purge(limit=limit)
    msg = await ctx.send(i18n(ctx, 'purge', len(deleted)))
    await a.sleep(2)
    await msg.delete()

@client.command(aliases=['cc'])
async def createthread(ctx):
    embed= discord.Embed(title=f'Thread creation', description=f'The following commands will create a channel for you to rp in the correct category. Please send a message with your command in the thread-creation channel within the member zone in order to create your channels. Examples here are for two character interestions but this can be changed if it is a solo thread (only include the first character name) or for more by adding another character e.g. Daphne-x-Shaggy-x-Scooby. Once your thread has been created, **please delete your message in the thread-creation channel**. If there are any issues, please contact an admin/moderator.')
    embed.add_field(name='Alternate universe or past timeline threads', value="To create a thread in this category you can use ```!createau character1name-x-character2name``` or ```!au character1name-x-character2name```", inline=False)
    embed.add_field(name='Technology threads', value="To create a thread in this category you can use the following (Note: _type_ in this case means technology type e.g. Text, Phonecall, Email, Twitter etc.): ```!createtech type character1name-x-character2name``` or ```!tech type character1name-x-character2name```", inline=False)
    embed.add_field(name='The Ski Lodge threads', value="To create a thread in this category you can use ```!createskilodge character1name-x-character2name``` or ```!lodge character1name-x-character2name```", inline=False)
    embed.add_field(name='The Cabins threads', value="To create a thread in this category you can use ```!createcabin character1name-x-character2name``` or ```!cabin character1name-x-character2name```", inline=False)
    embed.add_field(name='The Lake threads', value="To create a thread in this category you can use ```!createlake character1name-x-character2name``` or ```!lake character1name-x-character2name```", inline=False)
    embed.add_field(name='The Cafeteria threads', value="To create a thread in this category you can use ```!createcafeteria character1name-x-character2name``` or ```!cafeteria character1name-x-character2name```", inline=False)
    embed.add_field(name='The Forest threads', value="To create a thread in this category you can use ```!createforest character1name-x-character2name``` or ```!forest character1name-x-character2name```", inline=False)
    embed.add_field(name='The Campsite threads', value="To create a thread in this category you can use ```!createcamp character1name-x-character2name``` or ```!camp character1name-x-character2name```", inline=False)
    await ctx.send(embed=embed)

@client.command(aliases=['au'])
async def createau(ctx, thread):
    guild = ctx.message.guild
    name = 'ALTERNATE UNIVERSE/TIMELINE'
    category = discord.utils.get(ctx.guild.categories, name=name)
    await ctx.guild.create_text_channel(f'Thread-{thread}', category=category)

@client.command(aliases=['tech'])
async def createtechnology(ctx, type, thread):
    guild = ctx.message.guild
    name = 'technology'
    category = discord.utils.get(ctx.guild.categories, name=name)
    await ctx.guild.create_text_channel(f'{type}-{thread}', category=category)

@client.command(aliases=['lodge'])
async def createskilodge(ctx, thread):
    guild = ctx.message.guild
    name = 'the ski lodge'
    category = discord.utils.get(ctx.guild.categories, name=name)
    await ctx.guild.create_text_channel(f'{thread}', category=category)

@client.command(aliases=['cabin'])
async def createcabin(ctx, thread):
    guild = ctx.message.guild
    name = 'the cabins'
    category = discord.utils.get(ctx.guild.categories, name=name)
    await ctx.guild.create_text_channel(f'{thread}', category=category)

@client.command(aliases=['lake'])
async def createlake(ctx, thread):
    guild = ctx.message.guild
    name = 'the lake'
    category = discord.utils.get(ctx.guild.categories, name=name)
    await ctx.guild.create_text_channel(f'{thread}', category=category)

@client.command(aliases=['cafeteria'])
async def createcafeteria(ctx, thread):
    guild = ctx.message.guild
    name = 'the cafeteria'
    category = discord.utils.get(ctx.guild.categories, name=name)
    await ctx.guild.create_text_channel(f'{thread}', category=category)

@client.command(aliases=['forest'])
async def createforest(ctx, thread):
    guild = ctx.message.guild
    name = 'the forest'
    category = discord.utils.get(ctx.guild.categories, name=name)
    await ctx.guild.create_text_channel(f'{thread}', category=category)

@client.command(aliases=['camp'])
async def createcamp(ctx, thread):
    guild = ctx.message.guild
    name = 'the campsite'
    category = discord.utils.get(ctx.guild.categories, name=name)
    await ctx.guild.create_text_channel(f'{thread}', category=category)

if __name__ == '__main__':
    import config
    client.run(config.token)
