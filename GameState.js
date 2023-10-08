
class GameState {
    constructor(props) {
        this.images = []			// filenames for each round
        this.good_answers = [] 	    // usernames
        this.current_round = -1	    // current round idx
        this.round_time = 2 * 60; // in seconds
    }


    guess(country_name, user_id, channel) {
        let correct_answer = this.get_current_country()
        if (correct_answer === country_name) {
            this.good_answers.push(user_id)
            this.start_new_round(channel)
            return true
        }
        return false
    }

    get_current_country() {
        return this.images[this.current_round].split('-')[0]
    }

    get_remaining_time(seconds) {
        let minutes = Math.floor(seconds / 60);
        seconds -= minutes * 60;
        if (seconds < 10)
            return "Remaining time: " + `**${minutes}:0${seconds}**`
        return "Remaining time: " + `**${minutes}:${seconds}**`
    }

    async start_new_round(channel) {
        this.current_round += 1

        if (this.current_round >= this.images.length) {
            this.send_leader_board(channel)
            return
        }

        channel.send({
            files: [
                {
                    attachment: "scraper/images/" + this.images[this.current_round],
                    name: 'guess.png'
                }
            ]
        })

        let time_message = await channel.send(this.get_remaining_time(this.round_time))

        const last_number_of_rounds = this.current_round

        for (let i = 1; i <= this.round_time; i++) {
            await new Promise(r => setTimeout(r, 1000))
            if (last_number_of_rounds !== this.current_round) break
            time_message.edit(this.get_remaining_time(this.round_time - i))
        }

        if (last_number_of_rounds === this.current_round) {
            channel.send(`The answer was **"${this.get_current_country()}"**. Better luck next round`)
            this.start_new_round(channel)
        }
    }

    send_leader_board(channel) {
        let correct_guesses = {}
        for (const user of this.good_answers) {
            if (correct_guesses[user] === undefined)
                correct_guesses[user] = 1
            else
                correct_guesses[user]++
        }
        let players = [...new Set(this.good_answers)];
        players.sort((p1, p2) => {
            return correct_guesses[p2] - correct_guesses[p1]
        })

        channel.send("## === LEADERBOARD ===")
        for (const p of players) {
            channel.send(`<@${p}>: ${correct_guesses[p]}`)
        }
        channel.send("## ====================")
    }

}


module.exports = GameState
