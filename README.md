# Hangman
ece 2524 erxiang xu

Objective 

Using python to create a hangman game. This will be a traditional hangman: en.wikipedia.org/wiki/Hangman_(game) 
The game begins by picking names  of famous computer scientists at random.

Purpose

This project is submitted as the final prject of ECE2524 class in FALL 2015 in Virginia Tech.

Description 

The player then guesses letters until he/she gets the answer right  or makes a total of six incorrect guesses . After each incorrect guess, a new body part is drawn: first the head, then the body, then the left arm, then the right arm, then the left leg and then the right leg: six incorrect guesses means that the player has lost. The space in each name is not considered part of the answer – the user needs only to guess the letters



Key point

In order to finish this project, I will do several things here:

Name is chosen at random from the list of computer scientists

Dashes are drawn for the letters of the answer, but no dash for space in scientist’s name

drawGuess function – Guessed letters are drawn on screen over dashes

drawAlphabet function – Alphabet is shown with guessed letters in red and others in green

drawMan function – Body parts are drawn as the player makes incorrect guesses

updateGuess function – Updates data structures correctly

Player wins if  guesses all letters correctly within 5 tries

Player loses if  makes 6 incorrect guesses



