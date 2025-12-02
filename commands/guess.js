const { SlashCommandBuilder } = require('discord.js');
const { performance } = require('node:perf_hooks');

module.exports = {
	data: new SlashCommandBuilder()
		.setName('guess')
		.setDescription('Guess country name')
		.addStringOption(option =>
				option.setName("country_name")
					.setDescription("Guessed country")
					.setRequired(true)
		),
	async execute(interaction, games_states) {
		const startTime = performance.now()

		const country_name = interaction.options.get('country_name').value
		const user_id = interaction.user.id
		const guessed = games_states[interaction.guild.id + interaction.channel.id].guess(country_name, user_id, interaction.channel)
		
		

		if (guessed) {
			await interaction.reply(`yay! <@${interaction.user.id}> guessed **"${country_name}"**`);
		} else {
			await interaction.reply('nay! try again').then(() =>
				setTimeout(() => {
					interaction.deleteReply()
				}, 1000 * 3)
			)
		}
		const endTime = performance.now()
		const timeBenchmark = endTime - startTime
		console.log(`timing benchmark for guess: ${timeBenchmark} ms`)

	},
};