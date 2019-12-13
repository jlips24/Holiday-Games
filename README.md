# Secret Santa

## Table of Contents
- [Description](#description)
- [Setup](#setup)
- [Usage](#usage)

## Description

My friends and I wanted to do a secret santa, but we don;t live close to each other, so we couldn't pull names out of a hat. I looked for an application to do this for us, but I dodn't trust any of them with our email addresses, so I built an open source secret santa application that you control.

## Setup
- For importing names from code:
- In SecretSanta.py, navigate to the `main` function
- There, you will see a variable called `people`, that contains an array of arrays. For simplification, we will call the outer array `people`, and each inner array a `person`
- Each `person` array is structured in the following way:
    ```
    [
        "Person's name", 
        "Person's email", 
        Person's match's array index (default to -1), 
        Boolean representing if this person was choosen yet (default to False)
    ]
    ```
    Example:
    ```
    [
        "John Doe",
        "jdoe@email.com"
        -1,
        False
    ]
    ```
- Create a `person` array for each person in your secret santa in the `people` array, being careful to only add an even amount of people, or the application will get stuck in an infinite loop
- Save the file and you're ready to go!

## Usage
1. In the terminal, navigate to your project directory
2. Execute the following command
    
    ```
    python3 SecretSanta.py
    ```
3. Go out and buy some gifts!