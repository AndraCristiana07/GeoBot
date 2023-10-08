const { SlashCommandBuilder} = require('discord.js');
const { exec } = require('child_process');
const fs= require('fs');
const GameState = require('../GameState');

module.exports = {
    data: new SlashCommandBuilder()
        .setName('start')
        .setDescription('Starts a game')
        .addStringOption(option =>
                option.setName("rounds_number")
                    .setDescription("Guessed country")
                    .setRequired(true)
        ),
    async execute(interaction, games_states) {
        console.log(`Request from user ${interaction.user.username} on server ${interaction.guild.name} on channel ${interaction.channel.name}`)

        let new_game = new GameState();
        games_states[interaction.guild.id + interaction.channel.id] = new_game

        await interaction.reply(`Generating images...`)

        let generated = 0

        const round_count = parseInt(interaction.options.get('rounds_number').value)

        for (let i = 1; i <= round_count * 2; i++) {
            exec("cd scraper && source venv/bin/activate && python3 fetch_street_view.py", (error, stdout, stderr) => {
            // exec("echo NEXT", (error, stdout, stderr) => {
            //     console.log("OUT:", stdout)
                generated += 1
                if (generated === round_count) {
                    fs.readdir('scraper/images', function (err, files) {
                        //handling error
                        if (err) {
                            return console.log('Unable to scan directory: ' + err);
                        }

                        while (new_game.images.length !== round_count) {
                            let item = files[Math.floor(Math.random() * files.length)];
                            if (new_game.images.includes(item)) continue;
                            new_game.images.push(item)
                        }
                        interaction.editReply(`Ready to go!`)

                        // start game loop
                        new_game.start_new_round(interaction.channel)
                    });
                }
            })
        }



    },
};