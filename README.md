<!-- Improved compatibility of back to top link: See: https://github.com/othneildrew/Best-README-Template/pull/73 -->
<a name="readme-top"></a>
<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Don't forget to give the project a star!
*** Thanks again! Now go create something AMAZING! :D
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->


<!-- PROJECT LOGO -->
<br />
<div align="center">

  <h3 align="center">Geo Bot</h3>

  <p align="center">
    A discord bot that can play a "guess the country" game
    <br />
    <a href="https://github.com/othneildrew/Best-README-Template"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <!-- <a href="https://github.com/othneildrew/Best-README-Template">View Demo</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Report Bug</a>
    ·
    <a href="https://github.com/othneildrew/Best-README-Template/issues">Request Feature</a> -->
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
    <li><a href="#usage">Usage</a></li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
    <li><a href="#acknowledgments">Acknowledgments</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

<!-- [![Product Name Screen Shot][product-screenshot]](https://example.com) -->

This bot can engage its players by presenting them with images with geographic locations and it challenges them to guess the country that is shown. 
The commands that the user can give the bot are: 
* /ping : the bot returns "Pong!". This command is used just to test if the bot is online and ready to play 
* /start [number of rounds] : this starts the game with the number of rounds the user wants to play. It will fetch the images and the game will start. At this moment the timer starts as well and it will be displayed on the screen for each round (2 minutes for each) 
* /guess [country name] : the player can give the guess command and the country that they are guessing and the bot will say if it's the wrong or correct answer. If the answer is correct, the game will continue to the next round When the rounds end, there will be a leader board displayed with all the players and their scores.

This discord bot is made for a little fun game with friends when you are bored.


<p align="right">(<a href="#readme-top">back to top</a>)</p>



### Built With

This section should list any major frameworks/libraries used to bootstrap your project. Leave any add-ons/plugins for the acknowledgements section. Here are a few examples.

* <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/6/6a/JavaScript-logo.png/600px-JavaScript-logo.png" width="30" height="30">
<!-- * [![React][React.js]][React-url] -->
* <img src="data:image/png;base64,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" width="30" height="30">


<p align="right">(<a href="#readme-top">back to top</a>)</p>



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

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- USAGE EXAMPLES -->
<!-- ## Usage

Use this space to show useful examples of how a project can be used. Additional screenshots, code examples and demos work well in this space. You may also link to more resources.

_For more examples, please refer to the [Documentation](https://example.com)_

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



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





<p align="right">(<a href="#readme-top">back to top</a>)</p>




<!-- LICENSE
## License

Distributed under the MIT License. See `LICENSE.txt` for more information.

<p align="right">(<a href="#readme-top">back to top</a>)</p> -->



<!-- CONTACT -->
## Contact

Andra -  tapornadra@gmail.com

Project Link: https://github.com/AndraCristiana07/GeoBot

<p align="right">(<a href="#readme-top">back to top</a>)</p>



<!-- ACKNOWLEDGMENTS -->
## Acknowledgments

Some things that helped me while making this project :
* [Discord.js Guide](https://discordjs.guide/#before-you-begin)


<p align="right">(<a href="#readme-top">back to top</a>)</p>



