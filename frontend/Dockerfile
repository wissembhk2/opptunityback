FROM nikolaik/python-nodejs:latest

# Declaring env
ENV NODE_ENV development

# Setting up the work directory
WORKDIR /react-app

# Installing dependencies
COPY ./package.json /react-app
RUN npm install -f

# Copying all the files in our project
COPY . .

# Starting our application
CMD npm start
