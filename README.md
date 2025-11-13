# 🚗 Revive Motors

**Revive Motors** is a web-based platform for buying and selling reconditioned cars.  
Developed using **Django**, **PostgreSQL**, and **basic HTML/CSS**, it provides a smooth trading experience while maintaining secure user access and data consistency through **MVT architecture** and **Django ORM**.

---

## 🧩 Project Overview

**Revive Motors** serves as an online marketplace where users can list, browse, and purchase reconditioned cars.  
It ensures data integrity by enforcing strict ownership validation — only the rightful owner of a car can modify its details or change its sale status.  
The project also records all transactions, ensuring transparent trading history between buyers and sellers.

![image](https://github.com/saad-noman/revive-motors/blob/82e16b0bb2a89b82f0cef80aba1a478a9241005f/Revive-Motors.png)
![image](https://github.com/saad-noman/revive-motors/blob/82e16b0bb2a89b82f0cef80aba1a478a9241005f/Revive%20Motors%20Extended.png)

---

## 🚀 Core Features

### 👤 User Management
- User registration and login using Django’s built-in authentication system.  
- Each user has a secure account and personalized content.  

### 🚘 Car Management
- Add new cars for sale with essential details.  
- Edit or delete owned cars only if the logged-in user is the owner.  
- Change sale status (e.g., “For Sale” / “Not For Sale”) for owned cars only.  
- Card-style UI for browsing car listings with images and details.  
- View detailed information for each car.

### 💱 Transaction Management
- Users can **buy and sell cars** through the platform.  
- Automatic **ownership transfer** occurs immediately upon purchase.  
- The system maintains an **all-time transaction history** for every trade.  
- Instant updates on both car ownership and transaction records.  

---

## 🛠️ Tech Stack

| Component | Technology |
|------------|-------------|
| **Framework** | Django |
| **Frontend** | HTML, CSS |
| **Backend** | Python |
| **Database** | PostgreSQL |
| **Architecture** | MVT (Model–View–Template) |
| **ORM** | Django ORM |

---

## 🏗️ Architecture Overview

The project follows Django’s **MVT (Model–View–Template)** pattern:

- **Model:** Represents database tables and relationships using Django ORM.  
- **View:** Contains business logic and handles user requests.  
- **Template:** Defines the user interface with HTML and dynamic data rendering.  

This architecture provides modularity, scalability, and clear separation of responsibilities.

---

## 🗃️ Database Structure

### **Main Entities**
- **User** – Represents registered users who can buy or sell cars.  
- **Car** – Stores car details such as model, price, year, ownership, and sale status.  
- **Transaction** – Logs every buy/sell activity with details.  

The system uses **PostgreSQL** for data storage and Django’s **ORM** for safe and efficient database queries.

---

## 💡 Design Highlights

- **Secure access control** – Users can only modify their own listings.  
- **Automatic data synchronization** – Ownership and transaction updates happen instantly after a sale.  
- **Dynamic rendering** – Real-time display of available cars and their statuses.  
- **Minimalist UI** – Clean and responsive HTML/CSS design with card-based car showcasing.  

---

## 🧭 Future Enhancements

- Implement search and filter functionalities for cars.  
- Add image upload support for car listings.  
- Introduce user profile pages and saved listings.  
- Integrate payment gateways for secure transactions.  
- Develop RESTful APIs for mobile app or external system integration.  

---

## 👨‍💻 Author

**Saad Noman Adeeb**
- Undergraduate CSE Student, BRAC University

---



