# Highway Heist !
This is a game developed using the `Pygame` library. The objective of the game is to `collect coins while avoiding the sign boards`. The car can be controlled using the arrow keys[which are available on the screen(It works on screen touch and not using a keyboard)]. The score increases with each coin collected. Each `player has 3 lives` and he/she `loses 1 live after colliding with a sign board` (if the player collides with 3 sign boards, the game ends).

[**NOTE** : A new feature, **AI mode(Random Forest Classifier)**, has been introduced and is still in development phase]

![Screenshot_2023-05-07-12-40-46-737](https://user-images.githubusercontent.com/114089324/236663273-e3f641e5-ac0e-4ecd-9b53-4f6483a5e706.jpeg)

## Installation
Before running the game, `Pygame` library needs to be installed. Pygame can be installed using the following command:
```
pip install pygame==2.0.1
```
After Pygame is installed, download the game files and run the game by running the following command in the directory where the game files are located:
```
python3 main.py
```
## Installation - AI mode enabled game(Still in development phase)
If you want to play the all new AI mode, which is still in development phase, then you have to install the `scikit-learn` and `pandas` library also:
```
pip install -r requirements.txt
```
**OR**
```
pip install scikit-learn==1.0 pandas==1.3.3 pygame==2.0.1
```
Then run the following command:
```
python3 main_AI.py
```
## How to Play
> Press the left arrow button to move the car to the left.

> Press the right arrow button to move the car to the right.

> Press the button which looks like a break to stop the car.

> Collect as many coins as possible while avoiding the sign boards. The score will increase with each coin collected.

> Each player has 3 lives and he/she loses 1 live after colliding with a sign board (if the player collides with 3 sign boards, the game ends).

## Files
```main.py```: This is the main game file(Doesnt has AI mode).

```main_AI.py```: This is the AI game file(Still in development).

```requirements.txt```: This is the requirements file.

```assets/images```: This directory contains the images used in the game.

```assets/audios```: This directory contains the audio files used in the game.

```assets/HighScore.txt```: This file contains the high score achieved in the game.

```assets/data.json```: This file contains the data for training the AI in the all new AI mode.

## Credits
This game was developed by **Omanshu**.
