# Book Bazaar
#### Video Demo:  https://youtu.be/hYGXzaybJS0
#### Description:
Book bazaar is an e-commerce website which can be used to buy books. 

This application was developed using HTML, Bootstrap CSS, Python and Flask. It uses SQLite as its database

## Functionality
1. Login
2. User Registration
3. Book List with ability to filter on Author, Genre & Age. Only one filter can be used at a time.
4. View Book Details, along with other books in series, if any.
5. Add Book to cart 
6. Checkout
7. View Order History showing list of books previous ordered

## Database Design
Sqlite is used for database. 

There are four tables used to store data for the application

| Table Name | Description | Fields |
| -- | -- | -- |
| users | Contains list of registered users | id, username, country, state, city, address, hash |
| books | List of books that are shown | id, author, price, minAge, maxAge, genres, series, name, image|
| order1 | List of orders | id, user_id, order_num, time, total_amt|
| order_items | List of books purchased in order | id, order_id, book_id, qty, price|


## HTML Templates
There are 10 templates: 

| File Name | Description | 
| -- | -- |
| about.html | Provides a breif descroption of the project |
| cart.html | Displays current books in cart |
| checkout.html | Displays a message after the user proceeds to checkout |
| details.html | Shows some details about the book which user selected and also shows other books in the series,if any |
| history.html | Shows the order history of the books which user bought |
| index.html | It is the home page where you can find the list of all the books |
| layout.html | All other pages extend from this file |
| login.html | Used to Login |
| register.html | Create an account |
| yourAcc.html | Displays the details of the user that's logged in |
| | |
| scripts.sql | provides the scripts required to poplulate the ecom.db |

## Session Variables
| Variable Name | Description |
| -- | -- |
| user_id | Stores id of logged in user. Empty if no user logged in |
| cart | List of books (with qty). Empty list if no books added to cart |

## Book filters
The main page allows the user to filter on following three fields
- Author
- Genre
- Age

It is made by using a feature in bootstrap called collapsible accordian.

### Populate filter
The values in all three filters are obtained using DISTINCT query in books table

### Checking filter
When user clicks on the filter the clicked filter is passed to index page as query string. Index page will add where clause if the querystring is present.

## Handling cart
The books in cart is stored as list in session. When user adds a book, the added book is appended to the list in session.

The cart page firstly checks if the user has added any items to the cart yet. If the user has added item or items in the cart,
it displays a table with four columns which are as follows - Image of the book, Name of the book , Quantitiy of the book, and finally the price
of the book. below the table (in the bottom left ) you will see a "checkout" button which the user can use to checkout and buy the items.If there are not any items in the cart a message is displayed saying " No items in the cart".

## Checkout 
When user checks out, the items in cart is inserted int order1 and order_items table. History page uses order_items page to show the purchase history. 
