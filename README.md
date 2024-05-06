# Pokemon Card Guessing Game

Using a JSON filed from the web filled with individual Pokemon card data, I will create a "Guess that Pokemon"  game.

## Features

* Standard mode: the player picks from a list of sets and is given the 'flavour text' of a random Pokemon card which describes thematic information about the Pokemon on the card. The player can then guess the Pokemon immediately or choose between extra information either "retreat cost" or "attack" which reveals those pieces of information. Again they can guess or choose a hint from "stage" or "type". The player must then guess the Pokemon. If the player is correct they are given the chance to play again

* Spell check: If the guess is off by 1 or 2 characters, the player will be prompted to try again once.

* Hard mode: the player is given a random card from the entirety of the app's database and the card's flavour text. The player can opt for 1 hint from "attacks"  and "stage" and must then guess the card.

* Scoring: the more hints the player uses, the less points they will receive, they will also receive a bonus for completing a streak of correct Pokemon guesses. This data will be saved to a local file and players can keep track of their scores since installing the game.

[Repository where I got the data from](https://github.com/PokemonTCG/pokemon-tcg-data)
