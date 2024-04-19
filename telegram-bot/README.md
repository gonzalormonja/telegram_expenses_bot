## Set env variables

You will need to get the following variables to be able to use the application:

TELEGRAM_BOT_TOKEN
POSTGRES_URL

### Use without docker

If you want to use the application without docker you must:
1_ place yourself in the folder telegram-bot
2_ install the dependencies using `npm install`
3_ run the project using `npx ts-node src/index.ts`.


#### Dependencies
* axios: to interact via http with the python service
* body-parser: to parse the body when creating a new user
* dotenv: to configure the environment variables
* express: to receive the http request to create a new user
* jsonwebtoken: to create a token to authenticate against the python service
* telegraf: to create a telegram bot