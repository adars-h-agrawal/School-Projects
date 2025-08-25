-- shop.sql

CREATE DATABASE IF NOT EXISTS shop;
USE shop;

-- Employee Table
CREATE TABLE IF NOT EXISTS employee (
    EmpId INT PRIMARY KEY,
    Name VARCHAR(50),
    Salary DECIMAL(10,2)
);

-- Products Table
CREATE TABLE IF NOT EXISTS prod (
    SNo INT PRIMARY KEY,
    Type VARCHAR(50),
    Brand VARCHAR(50),
    Model VARCHAR(50),
    Quantity INT,
    Price DECIMAL(10,2)
);

-- Customers Table
CREATE TABLE IF NOT EXISTS customs (
    CustomerName VARCHAR(50),
    PhoneNo BIGINT PRIMARY KEY,
    Email VARCHAR(50),
    CreditPoints INT,
    PreviousPurchase DECIMAL(10,2)
);

-- Bill Table
CREATE TABLE IF NOT EXISTS bill (
    SNo INT,
    ProductName VARCHAR(50),
    Quantity INT,
    Price DECIMAL(10,2),
    CreditPoint INT,
    FinalPrice DECIMAL(10,2)
);
