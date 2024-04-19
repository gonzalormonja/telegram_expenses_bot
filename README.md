# Telegram Expenses bot
Repository created to perform a technical challenge

## Setup project

### Requirements

* docker

### Clone repository


To clone the repository we must use

```
git clone https://github.com/gonzalormonja/telegram_expenses_bot.git
```

### Set env variables

inside each project you can see the variables and how to obtain them in the readme file.

### Run project

To execute the project it is sufficient to run
```
docker compose up
```
This will start both services.

## Usage

### Create new user

To create a new user you can simply use the POST api/users endpoint with the body {telegram_id}.
This endpoint has no authentication, it is only to allow the testing of the application. 

#### Get Telegram user id
You must search for the bot called @userinfobot (the bot, there are fake groups, be careful).

### Use bot

Create a telegram bot using @botFather, set the necessary environment variables to integrate it and use the bot created.