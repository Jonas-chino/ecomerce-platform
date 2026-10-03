# Overview

I developed a console-based E-Commerce Platform that integrates with Google Cloud Firestore. The software simulates the backend of a store: it allows administrators to manage a product catalog, register users, and process purchase orders. When an order is created, the system reads from the `users` and `products` collections to verify the data, calculates the total price, records the transaction in an `orders` collection, and dynamically updates the product's available stock in the cloud. To use the program, you simply run the script in a terminal and navigate through a numbered interactive menu.

The primary purpose of writing this software was to master the `firebase-admin` SDK, understand document-oriented data structures, and practice transactional logic (like checking inventory before approving a sale) in a cloud environment.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

I am using **Google Cloud Firestore** (part of the Firebase platform), which is a flexible, scalable NoSQL cloud database.

The database structure is document-oriented and consists of three main collections that relate to each other through reference IDs:

- **`products` collection:** Stores individual product documents. Each document contains fields for `name` (string), `price` (number), and `stock` (number).
- **`users` collection:** Stores customer profiles. Each document contains fields for `name` (string) and `email` (string).
- **`orders` collection:** Acts as the relationship bridge between users and products. Each order document stores the `user_id`, `product_id`, `quantity` (number), `total_price` (number), and a `date` (timestamp).

# Development Environment

To develop this software, I used Visual Studio Code as my primary IDE and Git/GitHub for version control. The project is managed locally but interacts with the live Google Cloud environment via a secure service account key.

The software is written in **Python 3**. The primary library used is `firebase-admin` to authenticate and interact with the Firestore database. I also utilized the built-in `datetime` library to generate accurate timestamps for the purchase orders.

# Useful Websites

- https://www.freecodecamp.org/espanol/news/como-empezar-con-firebase-usando-python/
- https://www.youtube.com/watch?v=LaGYxQWYmmc&list=PLs3IFJPw3G9Jwaimh5yTKot1kV5zmzupt&index=1
- https://www.trymito.io/blog/how-to-connect-python-to-firebase-database-complete-guide

- https://elblogdelprogramador.com/posts/aprendiendo-firebase-con-python-una-guia-para-empezar/

# Future Work

{Make a list of things that you need to fix, improve, and add in the future.}

- Implement a secure User Authentication system instead of manually typing User IDs.
- Add robust data validation to prevent entering negative values for prices or stock
- Item 3
