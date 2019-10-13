from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class PingPong(Skill):

    @match_regex('ping')
    async def ping_pong(self, message):
        await message.respond('pong!')
