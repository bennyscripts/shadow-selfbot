import requests
import asyncio
import requests
import urllib
import main
import base64

from discord.ext import commands
from utils.config import *

class Text(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="text", description="Main text command.", usage="")
    async def text(self, ctx):
        commands_list = self.bot.get_cog("Text").get_commands()
        commands_str = ""

        for cmd in commands_list:
            if cmd.description[-1] == ".":
                cmd.description = cmd.description[:-1]

            commands_str += f"{PREFIX}{cmd.name}{cmd.usage} » {cmd.description}\n"

        await ctx.send(f"""```css
{requests.get(f'https://artii.herokuapp.com/make?text=TEXT').text}
{commands_str}
```""")

    @commands.command(name="regional", description="Convert your messages into emojis.", usage=" [message]")
    async def regional(self, ctx, *, message):
        text = message.lower()

        regional_indicators = {
            'a': '<:regional_indicator_a:803940414524620800>',
            'b': '<:regional_indicator_b:803940414524620800>',
            'c': '<:regional_indicator_c:803940414524620800>',
            'd': '<:regional_indicator_d:803940414524620800>',
            'e': '<:regional_indicator_e:803940414524620800>',
            'f': '<:regional_indicator_f:803940414524620800>',
            'g': '<:regional_indicator_g:803940414524620800>',
            'h': '<:regional_indicator_h:803940414524620800>',
            'i': '<:regional_indicator_i:803940414524620800>',
            'j': '<:regional_indicator_j:803940414524620800>',
            'k': '<:regional_indicator_k:803940414524620800>',
            'l': '<:regional_indicator_l:803940414524620800>',
            'm': '<:regional_indicator_m:803940414524620800>',
            'n': '<:regional_indicator_n:803940414524620800>',
            'o': '<:regional_indicator_o:803940414524620800>',
            'p': '<:regional_indicator_p:803940414524620800>',
            'q': '<:regional_indicator_q:803940414524620800>',
            'r': '<:regional_indicator_r:803940414524620800>',
            's': '<:regional_indicator_s:803940414524620800>',
            't': '<:regional_indicator_t:803940414524620800>',
            'u': '<:regional_indicator_u:803940414524620800>',
            'v': '<:regional_indicator_v:803940414524620800>',
            'w': '<:regional_indicator_w:803940414524620800>',
            'x': '<:regional_indicator_x:803940414524620800>',
            'y': '<:regional_indicator_y:803940414524620800>',
            'z': '<:regional_indicator_z:803940414524620800>'
        }

        output = ""

        for letter in list(text):
            if letter in regional_indicators: output = output + regional_indicators[letter] + " "
            else: output = output + letter

        await ctx.send(output)

    @commands.command(name="base64", description="Encrypt your messages using Base64", usage=" [message]")
    async def base64(self, ctx, *, message):
        message_bytes = message.encode('ascii')
        base64_bytes = base64.b64encode(message_bytes)
        base64_message = base64_bytes.decode('ascii')

        await ctx.send(base64_message)

    @commands.command(name="base64decode", description="Decrypt a Base64 message.", usage=" [message]")
    async def base64decode(self, ctx, *, message):
        base64_bytes = message.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        decoded = message_bytes.decode('ascii')

        await ctx.send(decoded)

    @commands.command(name="suggest", description="Make a suggestion.", usage=" [suggestion]")
    async def suggest(self, ctx, *, suggestion):
        msg = await ctx.send(f"**💭 Suggestion**\n- {suggestion}")

        await msg.add_reaction('\U0001F44D')
        await msg.add_reaction('\U0001F44E')

    @commands.command(name="secret", description="Send all your messages in a secret block.", usage=" [message]")
    async def secret(self, ctx, *, message):
        await ctx.send('||' + message + '||')

    @commands.command(name="secretletters", description="Put all lettes from your message into separate secret blocks.", usage=" [message]")
    async def secretletters(self, ctx, *, message):
        def split(word):
            return list(word)
        msg = ""
        for letter in split(message):
            msg += "||" + letter +  "||"
        await ctx.send(msg)

    @commands.command(name="purgehack", description="Purge messages without permission.", usage="")
    async def purgehack(self, ctx):
        purgeMsg = "** **\n" * 75
        await ctx.send(purgeMsg)

    @commands.command(name="uppercase", description="Send your message in uppercase.", usage=" [message]")
    async def uppercase(self, ctx, *, message):
        string = message.upper()
        await ctx.send(string)

    @commands.command(name="lowercase", description="Send your message in lowercase.", usage=" [message]")
    async def lowercase(ctx, *, message):
        string = message.lower()
        await ctx.send(string)

    @commands.command(name="aesthetic", description="Send your messages s p a c e d out.", usage=" [message]")
    async def aesthetic(self, ctx, *, message):
        msg = ""
        for letter in main.split(message):
            msg += " " + letter +  " "
        await ctx.send(msg)

    @commands.command(name="animate", description="Animate your messages.", usage="animate [message]")
    async def animate(self, ctx, *, message):
        output = ""
        text = list(message)
        msg = await ctx.send(text[0])
        for letter in text:
            output = output + letter + ""
            await msg.edit(content=output)
            await asyncio.sleep(1)

    @commands.command(name="chatbypass", description="Send your messages in a different font.", usage="chatbypass [message]")
    async def chatbypass(self, ctx, *, message):
        text = message.lower()

        letters = {
            'a': '𝚊',
            'b': '𝚋',
            'c': '𝚌',
            'd': '𝚍',
            'e': '𝚎',
            'f': '𝚏',
            'g': '𝚐',
            'h': '𝚑',
            'i': '𝚒',
            'j': '𝚓',
            'k': '𝚔',
            'l': '𝚕',
            'm': '𝚖',
            'n': '𝚗',
            'o': '𝚘',
            'p': '𝚙',
            'q': '𝚚',
            'r': '𝚛',
            's': '𝚜',
            't': '𝚝',
            'u': '𝚞',
            'v': '𝚟',
            'w': '𝚠',
            'x': '𝚡',
            'y': '𝚢',
            'z': '𝚣'
        }

        output = ""
        text = list(text)
        for letter in text:
            if letter in letters:
                output = output + letters[letter] + ""
            else:
                output = output + letter
        await ctx.send(output)

    @commands.command(name="bold", description="Send all your messages in bold.", usage=" [message]")
    async def bold(self, ctx, *, message):
        await ctx.send('**' + message + '**')

    @commands.command(name="italic", description="Send all your messages in italics.", usage=" [message]")
    async def italic(self, ctx, *, message):
        await ctx.send('*' + message + '*')

    @commands.command(name="cpp", description="Send all your messages in a C++ code block.", usage=" [message]")
    async def cpp(self, ctx, *, message):
        await ctx.send(f"""```cpp\n{message}```""")

    @commands.command(name="cs", description="Send all your messages in a C Sharp code block.", usage=" [message]")
    async def cs(self, ctx, *, message):
        await ctx.send(f"""```cs\n{message}```""")

    @commands.command(name="java", description="Send all your messages in a Java code block.", usage=" [message]")
    async def java(self, ctx, *, message):
        await ctx.send(f"""```java\n{message}```""")

    @commands.command(name="python", description="Send all your messages in a Python code block.", usage=" [message]")
    async def python(self, ctx, *, message):
        await ctx.send(f"""```py\n{message}```""")

    @commands.command(name="js", description="Send all your messages in a JavaScript code block.", usage=" [message]")
    async def js(self, ctx, *, message):
        await ctx.send(f"""```js\n{message}```""")

    @commands.command(name="lua", description="Send all your messages in a Lua code block.", usage=" [message]")
    async def lua(self, ctx, *, message):
        await ctx.send(f"""```lua\n{message}```""")

    @commands.command(name="php", description="Send all your messages in a PHP code block.", usage=" [message]")
    async def php(self, ctx, *, message):
        await ctx.send(f"""```php\n{message}```""")

    @commands.command(name="html", description="Send all your messages in a HTML code block.", usage=" [message]")
    async def html(self, ctx, *, message):
        await ctx.send(f"""```html\n{message}```""")

    @commands.command(name="css", description="Send all your messages in a CSS code block.", usage=" [message]")
    async def css(self, ctx, *, message):
        await ctx.send(f"""```css\n{message}```""")

    @commands.command(name="yaml", description="Send all your messages in a YAML code block.", usage=" [message]")
    async def yaml(self, ctx, *, message):
        await ctx.send(f"""```yaml\n{message}```""")

    @commands.command(name="json", description="Send all your messages in a JSON code block.", usage=" [message]")
    async def _json(self, ctx, *, message):
        await ctx.send(f"""```json\n{message}```""")

    @commands.command(name="ascii", description="Send a message in ascii art.", usage=" [\"message\"] (font)")
    async def ascii(self, ctx, message: str, font="standard"):
        art = requests.get(f'http://artii.herokuapp.com/make?text={urllib.parse.quote_plus(message)}+&font={font}').text
        await ctx.send(f"```{art}```")

def setup(bot):
    bot.add_cog(Text(bot))
