# Work information database

This project is a web page working as a database for storing client and country information for multitude of accounts managed in my work. For backend this was achieved with Django framework using PostgreSQL database (changed here to sqlite so it's easier to review and test through github). Frontend framework used was bootstrap.

### Project assumptions

Main goal of this project was to allow my team in work to gather and access the data we collect for various clients and countries we manage. In order to do so few functionalities had to be implemented. Users had to have possibility to add new countries and clients to database. Later for each of these entries they had to add specific comments/data entry that can later be reviewed by other users. Besides that also “blog” option had to be implemented so that users can add various questions/comments while other users could add their replies to such entries.

Note: User registration is not added as option as this is internal tool managed by administrator. This is to avoid incorrect data entries by unauthorized users.  

### Implemented functionalities:

· Possibility to review all the database data for all users

· All main functions like adding countries, clients, blog entries, comments (for logged in users only)

### Functionalities to be implemented:

· Further work on a frontend layer

· Option to modify user profile
