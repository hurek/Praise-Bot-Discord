import discord

MESSAGE_DATA = {
    # The Commons Stack
    776352358832930816: {
        'server_name': "The Commons Stack Discord",
        'title': "Congratulations! You've been dished Praise!",
        'description': "\n[__**View your praise on {}**__]({})\n\n"
                       "Your contribution to the Commons Stack has been recognized [in our Discord Server]"
                       "(https://discord.gg/uGYfNj9mbh). This Praise can give you reputation in our Trusted Seed.\n\n"
                       "To be eligible, you must be a member of the Commons Stack Trusted Seed. To apply, fill out "
                       "the form [here](https://commonsstack.org/apply). Once you are accepted we will be sending you "
                       "CSTK tokens on the address you mention in the form. If you already applied, no need to do this "
                       "again!\n\nYou can learn more about Praise on our [wiki](https://wiki.commonsstack.org/contribu"
                       "tors-guide) and the CSTK Token in [this article.](https://medium.com/commonsstack/cstk-the-toke"
                       "n-of-the-commons-stack-trusted-seed-931978625c61)\n**Thank you** for supporting the Commons "
                       "Stack!",
        'color': 0x00FA9A,
        'file': './img/theCommonsStack.png',
    },

    # Token Engineering
    701149241107808327: {
        'server_name': "TE Discord",
        'title': "Congratulations! You've been dished Praise!",
        'description': "\n[__**View your praise on {}**__]({})\n\n"
                       "Your contribution to the Token Engineering community has been recognized [in our Discord "
                       "Server](https://discord.gg/s9G2Wzv8gk). This Praise will become TE Commons Impact Hours "
                       "representing your impact on the Cultural Build, and TEC Impact Hours will become TEC Tokens "
                       "once the TE Commons Hatches!\n\nYou can learn more about Impact Hours on our [Medium Post "
                       "about it](https://medium.com/token-engineering-commons/how-to-earn-tec-tokens-now-an-inside-"
                       "look-at-impact-hours-7d93043b739d). :-D\n\nYou might also receive CSTK Tokens, which you can "
                       "read more about in [this article](https://medium.com/commonsstack/cstk-the-token-of-the-commons"
                       "-stack-trusted-seed-931978625c61).\n\n"
                       "**Thank you** for supporting Token Engineering!",
        'color': 0x696969,
        'file': './img/te.jpg',
    },

    # Token Engineering Commons
    810180621930070088: {
        'server_name': "TEC Discord",
        'title': "Congratulations! You've been dished Praise!",
        'description': "\n[__**View your praise on {}**__]({})\n\n"
                       "Your contribution to the Token Engineering community has been recognized [in our Discord "
                       "Server](https://discord.gg/cBnSkCAXAb). This Praise will become TE Commons Impact Hours "
                       "representing your impact on the Cultural Build, and TEC Impact Hours will become TEC Tokens "
                       "once the TE Commons Hatches!\n\nYou can learn more about Impact Hours on our [Medium Post "
                       "about it](https://medium.com/token-engineering-commons/how-to-earn-tec-tokens-now-an-inside-"
                       "look-at-impact-hours-7d93043b739d). :-D\n\nYou might also receive CSTK Tokens, which you can "
                       "read more about in [this article](https://medium.com/commonsstack/cstk-the-token-of-the-commons"
                       "-stack-trusted-seed-931978625c61).\n\n"
                       "**Thank you** for supporting Token Engineering!",
        'color': 0xd0e429,
        'file': './img/TEC.png',
    },

    # cadCad
    722946313775480845: {
        'server_name': "cadCad Discord",
        'title': "Congratulations! You've been dished Praise!",
        'description': "\n[__**View your praise on {}**__]({})\n\n"
                       "Your contribution to the cadCAD community has been recognized [in our Discord Server](https:"
                       "//discord.gg/uHG5B7tXF6). This Praise will become TE Commons Impact Hours representing your "
                       "impact on the Cultural Build, and TEC Impact Hours will become TEC Tokens once the TE Commons "
                       "Hatches!\n\nYou can learn more about Impact Hours on our [Medium Post about it](https://medium"
                       ".com/token-engineering-commons/how-to-earn-tec-tokens-now-an-inside-look-at-impact-hours-7d930"
                       "43b739d). :-D\n\nYou might also receive CSTK Tokens, which you can read more about in [this ar"
                       "ticle](https://medium.com/commonsstack/cstk-the-token-of-the-commons-stack-trusted-seed-931978"
                       "625c61).\n\n**Thank you** for supporting cadCAD and the emerging field of Token Engineering!",
        'color': 0x000080,
        'file': './img/cadCad.png',
    },

    # Giveth
    679428761438912522: {
        'server_name': "Giveth Discord",
        'title': "Congratulations! You've been dished Praise!",
        'description': "\n[__**View your praise on {}**__]({})\n\n"
                       "You did something amazing that contributes to the values and goals of Giveth. Thank you friend!"
                       "\nYour contribution has been recognised [in our Discord Server](https://discord.gg/xpb7rNpWdr)."
                       "\n\nFor now - your praise is recorded in our master spreadsheet, but soon your praise will be "
                       "converted\n" "into our upcoming GIV token.\n\nBe sure to follow updates on this and other "
                       "Giveth initiatives on our discord server, twitter and medium.",
        'color': 0x2E033F,
        'file': './img/givethio.png'
    },

    # Bot Training Ground
    764797633478787074: {
        'server_name': "Bot Training Ground Discord",
        'title': "Congratulations! You've been dished Praise!",
        'description': "\n[__**View your praise on {}**__]({})\n\n"
                       "Your contribution to the Commons Stack has been recognized [in our Discord Server]"
                       "(https://discord.gg/kwnzuYJfuM). This Praise can give you reputation in our Trusted Seed.\n\n"
                       "To be eligible, you must be a member of the Commons Stack Trusted Seed. To apply, fill out "
                       "the form [here](https://commonsstack.org/apply). Once you are accepted we will be sending you "
                       "CSTK tokens on the address you mention in the form. If you already applied, no need to do this "
                       "again!\n\nYou can learn more about Praise on our [wiki](https://wiki.commonsstack.org/contribu"
                       "tors-guide) and the CSTK Token in [this article.](https://medium.com/commonsstack/cstk-the-toke"
                       "n-of-the-commons-stack-trusted-seed-931978625c61)\n**Thank you** for supporting the Commons "
                       "Stack!",
        'color': 0x00FA9A,
        'file': './img/theCommonsStack.png'
    },
}


def createEmbed(server_id, message_link):
    embed = discord.Embed(
        title=MESSAGE_DATA[server_id]['title'],
        description=MESSAGE_DATA[server_id]['description'].format(MESSAGE_DATA[server_id]['server_name'], message_link),
        color=MESSAGE_DATA[server_id]['color'],
    )
    file = discord.File(MESSAGE_DATA[server_id]['file'], filename='footer.png')
    embed.set_image(url="attachment://footer.png")
    embed.set_footer(icon_url="attachment://footer.png")
    return {"embed": embed, "file": file}
