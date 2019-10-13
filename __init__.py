from opsdroid.skill import Skill
from opsdroid.matchers import match_regex


class PingPongSkill(Skill):

    @match_regex(r'ping|ping!')
    async def ping_pong(self, message):
        await message.respond('pong!')
