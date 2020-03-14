CREATE USER 'dev'@'localhost' IDENTIFIED BY 'dev';
GRANT SELECT,INSERT,UPDATE,DELETE,CREATE,DROP ON *.* TO 'dev'@'localhost';

CREATE DATABASE  IF NOT EXISTS `swdb` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `swdb`;
-- MySQL dump 10.13  Distrib 8.0.17, for macos10.14 (x86_64)
--
-- Host: localhost    Database: swdb
-- ------------------------------------------------------
-- Server version	8.0.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `attendance`
--

DROP TABLE IF EXISTS `attendance`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `attendance` (
  `fac_course_id` int(11) DEFAULT NULL,
  `student_id` varchar(25) NOT NULL,
  `date_of_class` date NOT NULL,
  `hour_of_class` int(11) NOT NULL,
  `status_of_student` varchar(2) DEFAULT NULL,
  PRIMARY KEY (`date_of_class`,`student_id`,`hour_of_class`),
  KEY `fac_course_id` (`fac_course_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `attendance_ibfk_1` FOREIGN KEY (`fac_course_id`) REFERENCES `faculty_to_course` (`fac_course_id`),
  CONSTRAINT `attendance_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `attendance`
--

LOCK TABLES `attendance` WRITE;
/*!40000 ALTER TABLE `attendance` DISABLE KEYS */;
INSERT INTO `attendance` VALUES (1,'std101','2020-02-03',1,'OD'),(1,'std102','2020-02-03',1,'A'),(1,'std101','2020-02-04',2,'P'),(1,'std102','2020-02-04',2,'OD'),(1,'std101','2020-02-05',9,'P'),(1,'std102','2020-02-05',9,'P'),(1,'std101','2020-02-08',3,'A'),(1,'std102','2020-02-08',3,'P'),(1,'std101','2020-02-10',3,'P'),(1,'std102','2020-02-10',3,'A'),(1,'std101','2020-03-02',1,'P'),(1,'std102','2020-03-02',1,'P'),(1,'std101','2020-03-03',4,'P'),(1,'std102','2020-03-03',4,'P'),(1,'std101','2020-03-04',6,'P'),(1,'std102','2020-03-04',6,'A'),(1,'std101','2020-03-05',2,'OD'),(1,'std101','2020-03-05',3,'A'),(1,'std102','2020-03-05',2,'A'),(1,'std102','2020-03-05',3,'P'),(1,'std101','2020-03-06',3,'P'),(1,'std102','2020-03-06',3,'P'),(1,'std101','2020-03-09',4,'A'),(1,'std102','2020-03-09',4,'P'),(1,'std101','2020-03-10',2,'A'),(1,'std102','2020-03-10',2,'P'),(1,'std101','2020-03-12',5,'P'),(1,'std102','2020-03-12',5,'P'),(1,'std101','2020-03-25',7,'P'),(1,'std102','2020-03-25',7,'P'),(1,'std101','2020-04-05',3,'OD'),(1,'std102','2020-04-05',3,'P');
/*!40000 ALTER TABLE `attendance` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `course_details`
--

DROP TABLE IF EXISTS `course_details`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `course_details` (
  `course_id` varchar(25) NOT NULL,
  `course_name` varchar(50) NOT NULL,
  PRIMARY KEY (`course_id`),
  UNIQUE KEY `course_name` (`course_name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `course_details`
--

LOCK TABLES `course_details` WRITE;
/*!40000 ALTER TABLE `course_details` DISABLE KEYS */;
INSERT INTO `course_details` VALUES ('cse123','Basics of Computer Sc.'),('cse125','C Programming'),('cse124','Computer Organisation');
/*!40000 ALTER TABLE `course_details` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty`
--

DROP TABLE IF EXISTS `faculty`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty` (
  `faculty_id` varchar(10) NOT NULL,
  `fname` varchar(25) NOT NULL,
  `lname` varchar(25) NOT NULL,
  PRIMARY KEY (`faculty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty`
--

LOCK TABLES `faculty` WRITE;
/*!40000 ALTER TABLE `faculty` DISABLE KEYS */;
INSERT INTO `faculty` VALUES ('cse123','Deepak','Malhotra'),('fac101','Deepak','Malhothra'),('fac102','Archana','Pooram'),('fac103','Ananth','Shetty'),('fac104','Sai','Vamsi'),('fac105','Parvathi','Biju');
/*!40000 ALTER TABLE `faculty` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty_login`
--

DROP TABLE IF EXISTS `faculty_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty_login` (
  `faculty_id` varchar(10) DEFAULT NULL,
  `user_name` varchar(10) NOT NULL,
  `password` varchar(25) NOT NULL,
  PRIMARY KEY (`user_name`),
  KEY `faculty_id` (`faculty_id`),
  CONSTRAINT `faculty_login_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty_login`
--

LOCK TABLES `faculty_login` WRITE;
/*!40000 ALTER TABLE `faculty_login` DISABLE KEYS */;
INSERT INTO `faculty_login` VALUES ('fac103','ananths13','fac103'),('fac102','archanap12','fac102'),('cse123','deep','samsung'),('fac101','deepakm11','fac101'),('fac105','parvathib','fac105'),('fac104','saiv14','fac104');
/*!40000 ALTER TABLE `faculty_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty_notification`
--

DROP TABLE IF EXISTS `faculty_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty_notification` (
  `fac_notif_id` int(11) NOT NULL AUTO_INCREMENT,
  `faculty_id` varchar(10) DEFAULT NULL,
  `fac_message` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`fac_notif_id`),
  KEY `faculty_id` (`faculty_id`),
  CONSTRAINT `faculty_notification_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty_notification`
--

LOCK TABLES `faculty_notification` WRITE;
/*!40000 ALTER TABLE `faculty_notification` DISABLE KEYS */;
INSERT INTO `faculty_notification` VALUES (1,'fac101','ISSUE RAISED BY X STUDENT'),(2,'fac101','Student std101 raised an issue '),(3,'fac101','Student std101 raised an issue ');
/*!40000 ALTER TABLE `faculty_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `faculty_to_course`
--

DROP TABLE IF EXISTS `faculty_to_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `faculty_to_course` (
  `fac_course_id` int(11) NOT NULL AUTO_INCREMENT,
  `faculty_id` varchar(25) DEFAULT NULL,
  `course_id` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`fac_course_id`),
  KEY `faculty_id` (`faculty_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `faculty_to_course_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `faculty_to_course_ibfk_2` FOREIGN KEY (`course_id`) REFERENCES `course_details` (`course_id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `faculty_to_course`
--

LOCK TABLES `faculty_to_course` WRITE;
/*!40000 ALTER TABLE `faculty_to_course` DISABLE KEYS */;
INSERT INTO `faculty_to_course` VALUES (1,'fac101','cse123'),(4,'fac102','cse124'),(5,'fac101','cse125'),(6,'fac103','cse125');
/*!40000 ALTER TABLE `faculty_to_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue`
--

DROP TABLE IF EXISTS `issue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issue` (
  `issue_id` int(11) NOT NULL AUTO_INCREMENT,
  `date_of_issue` date NOT NULL,
  `hour_of_issue` int(11) NOT NULL,
  `status_of_issue` varchar(25) DEFAULT 'Ongoing',
  `remarks` text,
  PRIMARY KEY (`issue_id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue`
--

LOCK TABLES `issue` WRITE;
/*!40000 ALTER TABLE `issue` DISABLE KEYS */;
INSERT INTO `issue` VALUES (2,'2020-02-04',2,'seen','df'),(3,'2020-03-05',2,'ongoing','2'),(4,'2020-03-04',6,'rejected','6');
/*!40000 ALTER TABLE `issue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `issue_track`
--

DROP TABLE IF EXISTS `issue_track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `issue_track` (
  `faculty_id` varchar(10) DEFAULT NULL,
  `student_id` varchar(10) DEFAULT NULL,
  `issue_id` int(11) NOT NULL,
  PRIMARY KEY (`issue_id`),
  KEY `faculty_id` (`faculty_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `issue_track_ibfk_1` FOREIGN KEY (`issue_id`) REFERENCES `issue` (`issue_id`),
  CONSTRAINT `issue_track_ibfk_2` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `issue_track_ibfk_3` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `issue_track`
--

LOCK TABLES `issue_track` WRITE;
/*!40000 ALTER TABLE `issue_track` DISABLE KEYS */;
INSERT INTO `issue_track` VALUES ('fac101','std101',2),('fac101','std101',3),('fac101','std101',4);
/*!40000 ALTER TABLE `issue_track` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `od`
--

DROP TABLE IF EXISTS `od`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `od` (
  `od_id` varchar(25) NOT NULL,
  `remarks` text,
  `approved_status` varchar(25) NOT NULL,
  PRIMARY KEY (`od_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `od`
--

LOCK TABLES `od` WRITE;
/*!40000 ALTER TABLE `od` DISABLE KEYS */;
/*!40000 ALTER TABLE `od` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `od_filename`
--

DROP TABLE IF EXISTS `od_filename`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `od_filename` (
  `image_id` int(11) NOT NULL,
  `pathname` text,
  UNIQUE KEY `image_id` (`image_id`),
  CONSTRAINT `od_filename_ibfk_1` FOREIGN KEY (`image_id`) REFERENCES `upload_od` (`image_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `od_filename`
--

LOCK TABLES `od_filename` WRITE;
/*!40000 ALTER TABLE `od_filename` DISABLE KEYS */;
INSERT INTO `od_filename` VALUES (1,'static/od-image-uploads/std101_fac103_1'),(2,'static/od-image-uploads/std101_fac103_2'),(3,'static/od-image-uploads/std101_fac103_3');
/*!40000 ALTER TABLE `od_filename` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `od_track`
--

DROP TABLE IF EXISTS `od_track`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `od_track` (
  `od_id` varchar(25) DEFAULT NULL,
  `faculty_id` varchar(10) DEFAULT NULL,
  `student_id` varchar(10) DEFAULT NULL,
  `course_id` varchar(10) DEFAULT NULL,
  KEY `od_id` (`od_id`),
  KEY `faculty_id` (`faculty_id`),
  KEY `student_id` (`student_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `od_track_ibfk_1` FOREIGN KEY (`od_id`) REFERENCES `od` (`od_id`),
  CONSTRAINT `od_track_ibfk_2` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `od_track_ibfk_3` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  CONSTRAINT `od_track_ibfk_4` FOREIGN KEY (`course_id`) REFERENCES `course_details` (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `od_track`
--

LOCK TABLES `od_track` WRITE;
/*!40000 ALTER TABLE `od_track` DISABLE KEYS */;
/*!40000 ALTER TABLE `od_track` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student`
--

DROP TABLE IF EXISTS `student`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student` (
  `student_id` varchar(10) NOT NULL,
  `fname` varchar(25) NOT NULL,
  `lname` varchar(25) NOT NULL,
  `class_advisor` varchar(10) DEFAULT NULL,
  PRIMARY KEY (`student_id`),
  KEY `class_advisor` (`class_advisor`),
  CONSTRAINT `student_ibfk_1` FOREIGN KEY (`class_advisor`) REFERENCES `faculty` (`faculty_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student`
--

LOCK TABLES `student` WRITE;
/*!40000 ALTER TABLE `student` DISABLE KEYS */;
INSERT INTO `student` VALUES ('cse234','Ahmed','Mallick','cse123'),('std101','Parvathi','Sanjana','fac103'),('std102','Anushka','Reddy','fac103'),('std103','Sundar','Pichai','fac103'),('std104','Ram','Newton','fac103'),('std105','Rajshree','Muthuraman','fac103');
/*!40000 ALTER TABLE `student` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_login`
--

DROP TABLE IF EXISTS `student_login`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_login` (
  `student_id` varchar(10) DEFAULT NULL,
  `user_name` varchar(10) NOT NULL,
  `password` varchar(25) NOT NULL,
  PRIMARY KEY (`user_name`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `student_login_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_login`
--

LOCK TABLES `student_login` WRITE;
/*!40000 ALTER TABLE `student_login` DISABLE KEYS */;
INSERT INTO `student_login` VALUES ('cse234','ahmed','motorola'),('std102','anushkar12','std102'),('std101','parvathi11','std101'),('std104','ramn14','std104'),('std103','sudarp13','std103');
/*!40000 ALTER TABLE `student_login` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_notification`
--

DROP TABLE IF EXISTS `student_notification`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_notification` (
  `stud_notif_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` varchar(10) DEFAULT NULL,
  `stud_message` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`stud_notif_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `student_notification_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=13 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_notification`
--

LOCK TABLES `student_notification` WRITE;
/*!40000 ALTER TABLE `student_notification` DISABLE KEYS */;
INSERT INTO `student_notification` VALUES (2,'std101','fac101 has changed issue 2 to seen'),(3,'std101','fac101 has changed issue 3 to resolved'),(4,'std101','fac101 has changed issue 4 to rejected'),(12,'std101','fac101 has changed issue 3 to ongoing');
/*!40000 ALTER TABLE `student_notification` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `student_to_course`
--

DROP TABLE IF EXISTS `student_to_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `student_to_course` (
  `student_id` varchar(25) NOT NULL,
  `course_id` varchar(25) NOT NULL,
  `faculty_id` varchar(25) DEFAULT NULL,
  PRIMARY KEY (`student_id`,`course_id`),
  KEY `faculty_id` (`faculty_id`),
  KEY `course_id` (`course_id`),
  CONSTRAINT `student_to_course_ibfk_1` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`),
  CONSTRAINT `student_to_course_ibfk_2` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `student_to_course_ibfk_3` FOREIGN KEY (`course_id`) REFERENCES `course_details` (`course_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `student_to_course`
--

LOCK TABLES `student_to_course` WRITE;
/*!40000 ALTER TABLE `student_to_course` DISABLE KEYS */;
INSERT INTO `student_to_course` VALUES ('std101','cse123','fac101'),('std102','cse123','fac101'),('std101','cse124','fac102'),('std102','cse124','fac102'),('std101','cse125','fac103'),('std102','cse125','fac103');
/*!40000 ALTER TABLE `student_to_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `upload_od`
--

DROP TABLE IF EXISTS `upload_od`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `upload_od` (
  `image_id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` varchar(10) DEFAULT NULL,
  `faculty_id` varchar(10) DEFAULT NULL,
  `status_of_approval` varchar(3) DEFAULT 'NO',
  PRIMARY KEY (`image_id`),
  KEY `faculty_id` (`faculty_id`),
  KEY `student_id` (`student_id`),
  CONSTRAINT `upload_od_ibfk_1` FOREIGN KEY (`faculty_id`) REFERENCES `faculty` (`faculty_id`),
  CONSTRAINT `upload_od_ibfk_2` FOREIGN KEY (`student_id`) REFERENCES `student` (`student_id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `upload_od`
--

LOCK TABLES `upload_od` WRITE;
/*!40000 ALTER TABLE `upload_od` DISABLE KEYS */;
INSERT INTO `upload_od` VALUES (1,'std101','fac101','NO'),(2,'std101','fac101','NO'),(3,'std101','fac101','NO');
/*!40000 ALTER TABLE `upload_od` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping routines for database 'swdb'
--
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-03-14 19:02:15
