
<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Geo Bot</h3>

  <p align="center">
    A discord bot that can play a "guess the country" game
    <br />
   
  </p>
</div>



<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisites">Prerequisites</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#acknowledgments">Acknoledgments</a></li>
    
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This bot can engage its players by presenting them with images with geographic locations and it challenges them to guess the country that is shown. 
The commands that the user can give the bot are: 
* **/ping** : the bot returns "Pong!". This command is used just to test if the bot is online and ready to play 
* **/start [number of rounds]** : this starts the game with the number of rounds the user wants to play. It will fetch the images and the game will start. At this moment the timer starts as well and it will be displayed on the screen for each round (2 minutes for each) 
* **/guess [country name]** : the player can give the guess command and the country that they are guessing and the bot will say if it's the wrong or correct answer. If the answer is correct, the game will continue to the next round When the rounds end, there will be a leader board displayed with all the players and their scores.

This discord bot is made for a little fun game with friends when you are bored.




### Built With

These are what I used to build the bot:

* ![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)




<!-- GETTING STARTED -->
## Getting Started

To be able to use this project you will need to download some stuff first.

### Prerequisites

* npm
  ```sh
  npm install -g n
  ```
* node,js
  ```sh
  sudo apt-get install nodejs
  ```
* discord,js
  ```sh
  npm install discord.js
  ```
### Installation

If you want to make your own bot like this you need to:
1. Initiating a project folder
   ```sh
   npm init
   ```
2. Clone the repo
   ```sh
   git clone https://github.com/AndraCristiana07/GeoBot.git
   ```
3. Set up a bot application
  * Open the [Discord developer portal](https://discord.com/developers/applications)
  * Log into your account
  * Click on "New Application"
  * Enter a name and click "Creat"
  * Now you should see another page
  * Click on "Bot" and click "Add Bot"
4. Add the bot to a server on discord
  * Here you have to create an invite link and choose permisions for your bot. For more information you can go to [Discord.js Guide on Adding a Bot to a server](https://discordjs.guide/preparations/adding-your-bot-to-servers.html#bot-invite-links).
    You will need to have most of the permission on for your bot to work.
5. After all is set, you should add your token and your clientID in the config.json file. You can find them on the page of your bot.


<!-- ROADMAP -->
## Roadmap

- [x] Make bot to be online
- [x] Make bot responsive
- [x] Scrape pictures from countries to be able to make game functional
- [x] Make bot able to start the game
- [x] Make bot able to recognise guesses
- [x] Start timer for each round
- [x] Make bot responses for wrong answer to dissapear after a few seconds
- [x] Show a leaderbot at the end



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Some things that helped me while making this project :
* [Discord.js Guide](https://discordjs.guide/#before-you-begin)




