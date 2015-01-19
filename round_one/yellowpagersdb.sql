-- MySQL dump 10.13  Distrib 5.6.17, for Win64 (x86_64)
--
-- Host: localhost    Database: The YellowPagers
-- ------------------------------------------------------
-- Server version	5.6.13

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `address`
--

DROP TABLE IF EXISTS `address`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `address` (
  `unique_id` int(11) NOT NULL,
  `address_number` int(11) DEFAULT NULL,
  `address_prefix` varchar(45) DEFAULT NULL,
  `address_lines` varchar(250) DEFAULT NULL,
  `address_postfix` varchar(45) DEFAULT NULL,
  `city` varchar(45) DEFAULT NULL,
  `state` varchar(45) DEFAULT NULL,
  `zip` int(15) DEFAULT NULL,
  `date_added` date NOT NULL,
  `date_modified` date NOT NULL,
  `type` varchar(45) NOT NULL,
  KEY `unique_id_idx` (`unique_id`),
  CONSTRAINT `unique_id` FOREIGN KEY (`unique_id`) REFERENCES `people` (`unique_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `address`
--

LOCK TABLES `address` WRITE;
/*!40000 ALTER TABLE `address` DISABLE KEYS */;
INSERT INTO `address` VALUES (0,897,'East','43rd','Avenue','Eugene','OR',97405,'2015-01-17','2015-01-17','home'),(0,1585,'East','13th','Avenue','Eugene','OR',97403,'2015-01-17','2015-01-17','work'),(0,128,NULL,'Windswept','Drive','Feasterville','PA',19053,'2015-01-17','2015-01-17','secondary');
/*!40000 ALTER TABLE `address` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `email`
--

DROP TABLE IF EXISTS `email`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `email` (
  `unique_id` int(11) NOT NULL,
  `primary_email` varchar(45) DEFAULT NULL,
  `secondary_email` varchar(45) DEFAULT NULL,
  `thrid_email` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`unique_id`),
  KEY `unique_id_email_idx` (`unique_id`),
  CONSTRAINT `unique_id_email_FK` FOREIGN KEY (`unique_id`) REFERENCES `people` (`unique_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `email`
--

LOCK TABLES `email` WRITE;
/*!40000 ALTER TABLE `email` DISABLE KEYS */;
INSERT INTO `email` VALUES (0,'vsyms613@gmail.com',NULL,NULL),(1,'joenorton75@gmail.com',NULL,NULL),(2,'katypinto11@gmail.com',NULL,NULL),(3,'hey.xiz.cs@gmail.com',NULL,NULL),(4,'twhite745@gmail.com',NULL,NULL),(5,'jadam.green@gmail.com',NULL,NULL),(6,'jgoddard19@gmail.com',NULL,NULL);
/*!40000 ALTER TABLE `email` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `favorites`
--

DROP TABLE IF EXISTS `favorites`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `favorites` (
  `unique_id` int(11) NOT NULL AUTO_INCREMENT,
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`unique_id`),
  CONSTRAINT `unique_id_fav_FK` FOREIGN KEY (`unique_id`) REFERENCES `people` (`unique_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `favorites`
--

LOCK TABLES `favorites` WRITE;
/*!40000 ALTER TABLE `favorites` DISABLE KEYS */;
/*!40000 ALTER TABLE `favorites` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `groups`
--

DROP TABLE IF EXISTS `groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `groups` (
  `type` varchar(50) NOT NULL,
  `unique_id` int(10) NOT NULL,
  PRIMARY KEY (`type`),
  KEY `unique_id_group_FK_idx` (`unique_id`),
  CONSTRAINT `unique_id_group_FK` FOREIGN KEY (`unique_id`) REFERENCES `people` (`unique_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `groups`
--

LOCK TABLES `groups` WRITE;
/*!40000 ALTER TABLE `groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master`
--

DROP TABLE IF EXISTS `master`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `master` (
  `addressbook_name` varchar(45) NOT NULL,
  `date_added` date NOT NULL,
  `date_modified` date NOT NULL,
  `addressbook_code` varchar(45) NOT NULL,
  PRIMARY KEY (`addressbook_name`),
  UNIQUE KEY `addressbook_code_idx` (`addressbook_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master`
--

LOCK TABLES `master` WRITE;
/*!40000 ALTER TABLE `master` DISABLE KEYS */;
/*!40000 ALTER TABLE `master` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `people`
--

DROP TABLE IF EXISTS `people`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `people` (
  `unique_id` int(11) NOT NULL,
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `addressbook_code` varchar(45) NOT NULL,
  PRIMARY KEY (`unique_id`),
  UNIQUE KEY `fname_idx` (`fname`),
  KEY `addressbook_code_FK_idx` (`addressbook_code`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1 COMMENT='		';
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `people`
--

LOCK TABLES `people` WRITE;
/*!40000 ALTER TABLE `people` DISABLE KEYS */;
INSERT INTO `people` VALUES (0,'Victoria','Norton',''),(1,'Joseph','Norton',''),(2,'Kat','Pinto',''),(3,'Xi','Zhang',''),(4,'Taylor','White',''),(5,'Adam','Green',''),(6,'Jared','Goddard',''),(7,'Stuart ','Faulk','');
/*!40000 ALTER TABLE `people` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `personal_notes`
--

DROP TABLE IF EXISTS `personal_notes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `personal_notes` (
  `unique_id` int(11) NOT NULL AUTO_INCREMENT,
  `date_added` date NOT NULL,
  `date_modified` date NOT NULL,
  `note` varchar(500) DEFAULT NULL,
  PRIMARY KEY (`unique_id`),
  CONSTRAINT `unique_id_note_FK` FOREIGN KEY (`unique_id`) REFERENCES `people` (`unique_id`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `personal_notes`
--

LOCK TABLES `personal_notes` WRITE;
/*!40000 ALTER TABLE `personal_notes` DISABLE KEYS */;
/*!40000 ALTER TABLE `personal_notes` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `phone_number`
--

DROP TABLE IF EXISTS `phone_number`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `phone_number` (
  `unique_id` int(11) NOT NULL,
  `mobile_phone` varchar(45) DEFAULT NULL,
  `home_phone` varchar(45) DEFAULT NULL,
  `work_phone` varchar(45) DEFAULT NULL,
  `secondary_number` varchar(45) DEFAULT NULL,
  PRIMARY KEY (`unique_id`),
  CONSTRAINT `unique_id_number_FK` FOREIGN KEY (`unique_id`) REFERENCES `people` (`unique_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `phone_number`
--

LOCK TABLES `phone_number` WRITE;
/*!40000 ALTER TABLE `phone_number` DISABLE KEYS */;
INSERT INTO `phone_number` VALUES (0,'215-630-9788','541-654-8040','541-364-0500',NULL),(1,'123-456-7890',NULL,NULL,NULL),(2,'789-963-1239','456-965-7799',NULL,NULL),(3,'541-357-7890',NULL,'852-546-6699',NULL),(4,'503-789-9856',NULL,NULL,NULL),(5,'570-555-3546','479-973-5513',NULL,NULL);
/*!40000 ALTER TABLE `phone_number` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `search`
--

DROP TABLE IF EXISTS `search`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `search` (
  `fname` varchar(45) NOT NULL,
  `lname` varchar(45) DEFAULT NULL,
  `date_searched` date NOT NULL,
  KEY `fname_search_FK_idx` (`fname`),
  CONSTRAINT `fname_FK` FOREIGN KEY (`fname`) REFERENCES `people` (`fname`) ON DELETE NO ACTION ON UPDATE NO ACTION
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `search`
--

LOCK TABLES `search` WRITE;
/*!40000 ALTER TABLE `search` DISABLE KEYS */;
/*!40000 ALTER TABLE `search` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping events for database 'The YellowPagers'
--

--
-- Dumping routines for database 'The YellowPagers'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2015-01-17 21:06:48
