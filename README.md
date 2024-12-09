# Secret Santa

## Table of Contents
- [Description](#description)
- [Setup](#setup)
- [Usage](#usage)

## Description

My friends and I wanted to do a secret santa, but we don't live close to each other, so we couldn't pull names out of a hat. I looked for an application to do this for us, but I dodn't trust any of them with our email addresses, so I built an open source secret santa application that you control.

This application runs in the command line. It supports Secret Santa and White Elephant.

## Setup
- Clone this repository on your local machine
- In terminal, navigate to the project directory
- Run the following commands:
    ```
    python3 -m venv venv

    source venv/bin/activate

    pip3 install -r requirements.txt

    cp .env.example .env

    cp config/people.csv.example config/people.csv
    ```
- Fill in the environment variables in the .env file
- You're ready to go!

## Usage

1. In the project directory, theres a config folder. There, you'll see a file called `people.csv`. Enter the information of all the people involved in your christmas game here
2. In the terminal, navigate to your project directory
3. Execute the following command
    
    ```
    python3 main.py
    ```
4. Use numbers to navigate the menu and choose your game
5. Have everyone check their email and buy some gifts!
