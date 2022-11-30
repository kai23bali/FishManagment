-- phpMyAdmin SQL Dump
-- version 5.2.0
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Generation Time: Nov 30, 2022 at 11:17 PM
-- Server version: 10.4.24-MariaDB
-- PHP Version: 8.1.6

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `fish management`
--

-- --------------------------------------------------------

--
-- Table structure for table `costumer`
--

CREATE TABLE `costumer` (
  `userID` int(11) NOT NULL,
  `firstName` varchar(255) NOT NULL,
  `lastName` varchar(255) NOT NULL,
  `userName` varchar(255) NOT NULL,
  `passcode` varchar(255) NOT NULL,
  `email` varchar(255) NOT NULL,
  `shippingAddress` varchar(255) NOT NULL,
  `paymentInfo` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `costumer`
--

INSERT INTO `costumer` (`userID`, `firstName`, `lastName`, `userName`, `passcode`, `email`, `shippingAddress`, `paymentInfo`) VALUES
(1, 'CJ', 'Chua', 'chua2002', '12345', 'cj@b.com', 'sdgafd', 'dsfgsa'),
(5, 'CJ', 'Chua', 'cj6886', '1234', 'cj6886@b.com', '345ear|sgw3e|gfae|df', '132412|34|12/324|wef233r|Charles Chua');

-- --------------------------------------------------------

--
-- Table structure for table `inventory`
--

CREATE TABLE `inventory` (
  `itemID` int(5) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(500) NOT NULL,
  `stock` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `inventory`
--

INSERT INTO `inventory` (`itemID`, `name`, `description`, `stock`, `price`) VALUES
(1, 'Redish-purple snapper', 'Like a red snapper, but with a splash of purple', -1, '34.65'),
(2, 'Snaggletooth Carp', 'This one is a pest', 35, '0.99'),
(3, '1 fish', 'The first fish', 342, '1.00'),
(4, '2 fish', 'The second fish', 811, '2.00');

-- --------------------------------------------------------

--
-- Table structure for table `orders`
--

CREATE TABLE `orders` (
  `orderID` int(11) NOT NULL,
  `itemID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `quantity` int(11) NOT NULL,
  `price` decimal(10,2) NOT NULL,
  `orderTime` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `orders`
--

INSERT INTO `orders` (`orderID`, `itemID`, `userID`, `name`, `quantity`, `price`, `orderTime`) VALUES
(2, 2, 1, 'Snaggletooth Carp', 3, '0.99', 'Mon Nov 28 22:07:00 2022'),
(3, 2, 5, 'Snaggletooth Carp', 12, '0.99', 'Wed Nov 30 15:03:02 2022'),
(4, 1, 5, 'Redish-purple snapper', 2, '34.65', 'Wed Nov 30 15:03:45 2022'),
(5, 1, 5, 'Redish-purple snapper', 3, '34.65', 'Wed Nov 30 15:36:52 2022'),
(6, 1, 5, 'Redish-purple snapper', 4, '34.65', 'Wed Nov 30 15:36:52 2022'),
(7, 4, 5, '2 fish', 2, '2.00', 'Wed Nov 30 16:15:52 2022');

-- --------------------------------------------------------

--
-- Table structure for table `shoppingcart`
--

CREATE TABLE `shoppingcart` (
  `itemID` int(11) NOT NULL,
  `userID` int(11) NOT NULL,
  `quantity` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Dumping data for table `shoppingcart`
--

INSERT INTO `shoppingcart` (`itemID`, `userID`, `quantity`) VALUES
(2, 1, 2);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `costumer`
--
ALTER TABLE `costumer`
  ADD PRIMARY KEY (`userID`);

--
-- Indexes for table `inventory`
--
ALTER TABLE `inventory`
  ADD PRIMARY KEY (`itemID`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `orders`
--
ALTER TABLE `orders`
  ADD PRIMARY KEY (`orderID`),
  ADD KEY `order_to_inventory` (`itemID`),
  ADD KEY `order_to_user` (`userID`);

--
-- Indexes for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  ADD KEY `cart_to_inventory` (`itemID`),
  ADD KEY `cart_to_user` (`userID`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `costumer`
--
ALTER TABLE `costumer`
  MODIFY `userID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT for table `inventory`
--
ALTER TABLE `inventory`
  MODIFY `itemID` int(5) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `orders`
--
ALTER TABLE `orders`
  MODIFY `orderID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=8;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `orders`
--
ALTER TABLE `orders`
  ADD CONSTRAINT `order_to_inventory` FOREIGN KEY (`itemID`) REFERENCES `inventory` (`itemID`),
  ADD CONSTRAINT `order_to_user` FOREIGN KEY (`userID`) REFERENCES `costumer` (`userID`);

--
-- Constraints for table `shoppingcart`
--
ALTER TABLE `shoppingcart`
  ADD CONSTRAINT `cart_to_inventory` FOREIGN KEY (`itemID`) REFERENCES `inventory` (`itemID`),
  ADD CONSTRAINT `cart_to_user` FOREIGN KEY (`userID`) REFERENCES `costumer` (`userID`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
