-- MySQL dump 10.13  Distrib 8.0.34, for Win64 (x86_64)
--
-- Host: localhost    Database: creditcard_capstone
-- ------------------------------------------------------
-- Server version	8.0.34

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
-- Table structure for table `cdw-sapp_loan_application`
--

DROP TABLE IF EXISTS `cdw-sapp_loan_application`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cdw-sapp_loan_application` (
  `Application_ID` text,
  `Gender` text,
  `Married` text,
  `Dependents` text,
  `Education` text,
  `Self_Employed` text,
  `Credit_History` int DEFAULT NULL,
  `Property_Area` text,
  `Income` text,
  `Application_Status` text
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cdw-sapp_loan_application`
--

LOCK TABLES `cdw-sapp_loan_application` WRITE;
/*!40000 ALTER TABLE `cdw-sapp_loan_application` DISABLE KEYS */;
INSERT INTO `cdw-sapp_loan_application` VALUES ('LP002714','Male','No','1','Not Graduate','No',1,'Semiurban','low','Y'),('LP001520','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001002','Male','No','0','Graduate','No',1,'Urban','medium','Y'),('LP001953','Male','Yes','1','Graduate','No',1,'Semiurban','medium','Y'),('LP001245','Male','Yes','2','Not Graduate','Yes',1,'Semiurban','low','Y'),('LP002448','Male','Yes','0','Graduate','No',0,'Rural','low','N'),('LP001744','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP002716','Male','No','0','Not Graduate','No',1,'Semiurban','medium','Y'),('LP001528','Male','No','0','Graduate','No',0,'Rural','medium','N'),('LP002720','Male','Yes','3+','Graduate','No',1,'Urban','medium','Y'),('LP001749','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001529','Male','Yes','0','Graduate','Yes',1,'Rural','low','Y'),('LP001750','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001531','Male','No','0','Graduate','No',1,'Urban','medium','N'),('LP002723','Male','No','2','Graduate','No',0,'Rural','low','N'),('LP001532','Male','Yes','2','Not Graduate','No',1,'Rural','low','N'),('LP001751','Male','Yes','0','Graduate','No',1,'Rural','low','N'),('LP002731','Female','No','0','Not Graduate','Yes',1,'Urban','high','Y'),('LP001535','Male','No','0','Graduate','No',1,'Urban','low','Y'),('LP001758','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP002734','Male','Yes','0','Graduate','No',1,'Urban','medium','Y'),('LP001536','Male','Yes','3+','Graduate','No',0,'Semiurban','high','Y'),('LP002738','Male','No','2','Graduate','No',1,'Semiurban','low','Y'),('LP001761','Male','No','0','Graduate','Yes',1,'Rural','medium','Y'),('LP001543','Male','Yes','1','Graduate','No',1,'Urban','medium','Y'),('LP002739','Male','Yes','0','Not Graduate','No',1,'Rural','low','N'),('LP002449','Male','Yes','0','Graduate','No',0,'Rural','low','Y'),('LP002453','Male','No','0','Graduate','Yes',1,'Semiurban','medium','Y'),('LP001765','Male','Yes','1','Graduate','No',1,'Semiurban','low','Y'),('LP001954','Female','Yes','1','Graduate','No',1,'Urban','medium','Y'),('LP001770','Male','No','0','Not Graduate','No',1,'Rural','low','Y'),('LP001003','Male','Yes','1','Graduate','No',1,'Rural','medium','N'),('LP001005','Male','Yes','0','Graduate','Yes',1,'Urban','low','Y'),('LP001776','Female','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001006','Male','Yes','0','Not Graduate','No',1,'Urban','low','Y'),('LP001955','Female','No','0','Graduate','No',1,'Rural','medium','N'),('LP001248','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP001963','Male','Yes','1','Graduate','No',1,'Urban','low','N'),('LP001008','Male','No','0','Graduate','No',1,'Urban','medium','Y'),('LP001250','Male','Yes','3+','Not Graduate','No',0,'Semiurban','medium','N'),('LP001778','Male','Yes','1','Graduate','No',1,'Semiurban','low','Y'),('LP001964','Male','Yes','0','Not Graduate','No',0,'Urban','low','N'),('LP001253','Male','Yes','3+','Graduate','Yes',1,'Semiurban','medium','Y'),('LP001011','Male','Yes','2','Graduate','Yes',1,'Urban','medium','Y'),('LP001784','Male','Yes','1','Graduate','No',1,'Rural','medium','Y'),('LP001974','Female','No','0','Graduate','No',1,'Rural','medium','Y'),('LP001255','Male','No','0','Graduate','No',1,'Urban','low','N'),('LP001013','Male','Yes','0','Not Graduate','No',1,'Urban','low','Y'),('LP001790','Female','No','1','Graduate','No',1,'Rural','low','Y'),('LP001256','Male','No','0','Graduate','No',1,'Urban','low','N'),('LP001977','Male','Yes','1','Graduate','No',1,'Urban','low','Y'),('LP001014','Male','Yes','3+','Graduate','No',0,'Semiurban','low','N'),('LP001792','Male','Yes','1','Graduate','No',1,'Semiurban','low','Y'),('LP001259','Male','Yes','1','Graduate','Yes',1,'Urban','low','N'),('LP001018','Male','Yes','2','Graduate','No',1,'Urban','medium','Y'),('LP001978','Male','No','0','Graduate','No',1,'Rural','medium','Y'),('LP001263','Male','Yes','3+','Graduate','No',0,'Semiurban','low','N'),('LP001798','Male','Yes','2','Graduate','No',1,'Rural','medium','Y'),('LP001265','Female','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP001020','Male','Yes','1','Graduate','No',1,'Semiurban','high','N'),('LP001800','Male','Yes','1','Not Graduate','No',1,'Urban','low','N'),('LP001990','Male','No','0','Not Graduate','No',1,'Urban','low','N'),('LP002740','Male','Yes','3+','Graduate','No',1,'Rural','medium','Y'),('LP001266','Male','Yes','1','Graduate','Yes',1,'Semiurban','low','Y'),('LP001024','Male','Yes','2','Graduate','No',1,'Urban','low','Y'),('LP001806','Male','No','0','Graduate','No',1,'Urban','low','Y'),('LP001993','Female','No','0','Graduate','No',1,'Rural','low','Y'),('LP001267','Female','Yes','2','Graduate','No',1,'Urban','low','N'),('LP001028','Male','Yes','2','Graduate','No',1,'Urban','low','Y'),('LP001994','Female','No','0','Graduate','No',0,'Urban','low','N'),('LP001807','Male','Yes','2','Graduate','Yes',1,'Rural','medium','Y'),('LP002741','Female','Yes','1','Graduate','No',1,'Semiurban','medium','Y'),('LP001275','Male','Yes','1','Graduate','No',1,'Urban','low','Y'),('LP001029','Male','No','0','Graduate','No',1,'Rural','low','N'),('LP001996','Male','No','0','Graduate','No',1,'Rural','high','N'),('LP001811','Male','Yes','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP001030','Male','Yes','2','Graduate','No',1,'Urban','low','Y'),('LP001279','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP002002','Female','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP001813','Male','No','0','Graduate','Yes',1,'Urban','medium','N'),('LP002743','Female','No','0','Graduate','No',0,'Semiurban','low','N'),('LP001032','Male','No','0','Graduate','No',1,'Urban','medium','Y'),('LP001282','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP002004','Male','No','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP001814','Male','Yes','2','Graduate','No',1,'Urban','medium','Y'),('LP001036','Female','No','0','Graduate','No',0,'Urban','low','N'),('LP001289','Male','No','0','Graduate','No',1,'Urban','medium','Y'),('LP002006','Female','No','0','Graduate','No',1,'Rural','low','Y'),('LP002755','Male','Yes','1','Not Graduate','No',1,'Urban','low','Y'),('LP001819','Male','Yes','1','Not Graduate','No',1,'Urban','medium','Y'),('LP001038','Male','Yes','0','Not Graduate','No',1,'Rural','medium','N'),('LP002031','Male','Yes','1','Not Graduate','No',1,'Urban','low','Y'),('LP001310','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001824','Male','Yes','1','Graduate','No',1,'Semiurban','low','Y'),('LP002035','Male','Yes','2','Graduate','No',1,'Semiurban','low','Y'),('LP001316','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001043','Male','Yes','0','Not Graduate','No',0,'Urban','medium','N'),('LP001825','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP002767','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002050','Male','Yes','1','Graduate','Yes',1,'Rural','high','N'),('LP001318','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP001046','Male','Yes','1','Graduate','No',1,'Urban','medium','Y'),('LP001835','Male','Yes','0','Not Graduate','No',0,'Semiurban','low','N'),('LP002051','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001319','Male','Yes','2','Not Graduate','No',1,'Urban','low','Y'),('LP001836','Female','No','2','Graduate','No',1,'Urban','low','N'),('LP001047','Male','Yes','0','Not Graduate','No',0,'Semiurban','low','N'),('LP001322','Male','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002053','Male','Yes','3+','Graduate','No',1,'Semiurban','medium','Y'),('LP001841','Male','No','0','Not Graduate','Yes',1,'Rural','low','Y'),('LP001066','Male','Yes','0','Graduate','Yes',1,'Semiurban','medium','Y'),('LP002768','Male','No','0','Not Graduate','No',1,'Semiurban','low','N'),('LP002054','Male','Yes','2','Not Graduate','No',1,'Rural','low','Y'),('LP001325','Male','No','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP001843','Male','Yes','1','Not Graduate','No',1,'Semiurban','low','Y'),('LP001068','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP002065','Male','Yes','3+','Graduate','No',1,'Rural','high','Y'),('LP001844','Male','No','0','Graduate','Yes',0,'Urban','high','N'),('LP001327','Female','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001073','Male','Yes','2','Not Graduate','No',1,'Urban','medium','Y'),('LP002067','Male','Yes','1','Graduate','Yes',0,'Rural','medium','N'),('LP001846','Female','No','3+','Graduate','No',1,'Rural','low','Y'),('LP002772','Male','No','0','Graduate','No',1,'Rural','low','Y'),('LP001333','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001086','Male','No','0','Not Graduate','No',1,'Urban','low','N'),('LP002068','Male','No','0','Graduate','No',0,'Rural','medium','Y'),('LP001849','Male','No','0','Not Graduate','No',0,'Rural','medium','N'),('LP001334','Male','Yes','0','Not Graduate','No',1,'Semiurban','medium','Y'),('LP001095','Male','No','0','Graduate','No',1,'Urban','low','N'),('LP002082','Male','Yes','0','Graduate','Yes',1,'Semiurban','medium','Y'),('LP002776','Female','No','0','Graduate','No',0,'Semiurban','medium','N'),('LP001343','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001097','Male','No','1','Graduate','Yes',1,'Rural','medium','N'),('LP001345','Male','Yes','2','Not Graduate','No',1,'Urban','medium','Y'),('LP002086','Female','Yes','0','Graduate','No',1,'Urban','medium','N'),('LP002777','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP001098','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001854','Male','Yes','3+','Graduate','No',1,'Urban','medium','N'),('LP001349','Male','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002087','Female','No','0','Graduate','No',1,'Urban','low','Y'),('LP002778','Male','Yes','2','Graduate','Yes',0,'Rural','medium','N'),('LP001100','Male','No','3+','Graduate','No',1,'Rural','high','N'),('LP001859','Male','Yes','0','Graduate','No',1,'Rural','high','N'),('LP001356','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002097','Male','No','1','Graduate','No',1,'Urban','medium','Y'),('LP002784','Male','Yes','1','Not Graduate','No',1,'Rural','low','Y'),('LP001868','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP001367','Male','Yes','1','Graduate','No',1,'Urban','low','Y'),('LP001106','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP002098','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP001870','Female','No','1','Graduate','No',1,'Semiurban','low','N'),('LP001369','Male','Yes','2','Graduate','No',1,'Urban','high','Y'),('LP001109','Male','Yes','0','Graduate','No',0,'Urban','low','N'),('LP002785','Male','Yes','1','Graduate','No',1,'Urban','low','Y'),('LP002112','Male','Yes','2','Graduate','Yes',1,'Rural','low','Y'),('LP001379','Male','Yes','2','Graduate','No',0,'Urban','low','N'),('LP001112','Female','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001871','Female','No','0','Graduate','No',1,'Rural','medium','Y'),('LP002788','Male','Yes','0','Not Graduate','No',0,'Urban','low','N'),('LP001384','Male','Yes','3+','Not Graduate','No',1,'Semiurban','low','Y'),('LP002113','Female','No','3+','Not Graduate','No',0,'Urban','low','N'),('LP001114','Male','No','0','Graduate','No',1,'Urban','medium','Y'),('LP002789','Male','Yes','0','Graduate','No',0,'Rural','low','N'),('LP001872','Male','No','0','Graduate','Yes',1,'Semiurban','medium','Y'),('LP001385','Male','No','0','Graduate','No',1,'Urban','medium','Y'),('LP002114','Female','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001116','Male','No','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP001875','Male','No','0','Graduate','No',1,'Rural','medium','Y'),('LP002792','Male','Yes','1','Graduate','No',1,'Semiurban','medium','Y'),('LP001391','Male','Yes','0','Not Graduate','No',0,'Rural','low','N'),('LP002115','Male','Yes','3+','Not Graduate','No',1,'Rural','low','N'),('LP001119','Male','No','0','Graduate','No',1,'Urban','low','N'),('LP001877','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP002795','Male','Yes','3+','Graduate','Yes',1,'Semiurban','high','Y'),('LP001392','Female','No','1','Graduate','Yes',1,'Semiurban','medium','Y'),('LP002116','Female','No','0','Graduate','No',1,'Rural','low','N'),('LP001120','Male','No','0','Graduate','No',1,'Urban','low','Y'),('LP002798','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001401','Male','Yes','1','Graduate','No',1,'Rural','high','Y'),('LP001882','Male','Yes','3+','Graduate','No',0,'Urban','medium','Y'),('LP002119','Male','Yes','1','Not Graduate','No',1,'Urban','medium','Y'),('LP001131','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001404','Female','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001884','Female','No','1','Graduate','No',1,'Urban','low','Y'),('LP002804','Female','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002126','Male','Yes','3+','Not Graduate','No',1,'Semiurban','low','Y'),('LP001421','Male','Yes','0','Graduate','No',1,'Rural','medium','N'),('LP001136','Male','Yes','0','Not Graduate','Yes',1,'Urban','medium','Y'),('LP001888','Female','No','0','Graduate','No',1,'Urban','low','Y'),('LP002807','Male','Yes','2','Not Graduate','No',1,'Semiurban','low','Y'),('LP001422','Female','No','0','Graduate','No',1,'Urban','high','Y'),('LP002129','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001137','Female','No','0','Graduate','No',1,'Urban','low','Y'),('LP002813','Female','Yes','1','Graduate','Yes',1,'Semiurban','high','Y'),('LP001891','Male','Yes','0','Graduate','No',1,'Urban','high','Y'),('LP001430','Female','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001138','Male','Yes','1','Graduate','No',1,'Urban','medium','Y'),('LP002131','Male','Yes','2','Not Graduate','No',1,'Urban','low','Y'),('LP002820','Male','Yes','0','Graduate','No',1,'Rural','medium','Y'),('LP001892','Male','No','0','Graduate','No',1,'Rural','low','Y'),('LP002455','Male','Yes','2','Graduate','No',1,'Semiurban','low','Y'),('LP001144','Male','Yes','0','Graduate','No',1,'Urban','medium','Y'),('LP001431','Female','No','0','Graduate','No',0,'Semiurban','low','Y'),('LP002821','Male','No','0','Not Graduate','Yes',1,'Semiurban','medium','Y'),('LP002138','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP001552','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001146','Female','Yes','0','Graduate','No',0,'Urban','low','N'),('LP001432','Male','Yes','2','Graduate','No',1,'Semiurban','low','Y'),('LP002832','Male','Yes','2','Graduate','No',0,'Urban','medium','N'),('LP002139','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001151','Female','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP001560','Male','Yes','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP001439','Male','Yes','0','Not Graduate','No',1,'Rural','medium','Y'),('LP002836','Male','No','0','Graduate','No',1,'Urban','low','Y'),('LP002140','Male','No','0','Graduate','No',1,'Rural','medium','N'),('LP001562','Male','Yes','0','Graduate','No',1,'Urban','medium','N'),('LP002837','Male','Yes','3+','Graduate','No',0,'Rural','low','N'),('LP001449','Male','No','0','Graduate','No',1,'Rural','low','Y'),('LP002141','Male','Yes','3+','Graduate','No',1,'Rural','low','Y'),('LP001894','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001565','Male','Yes','1','Graduate','No',0,'Semiurban','low','N'),('LP002142','Female','Yes','0','Graduate','Yes',0,'Rural','medium','N'),('LP001451','Male','Yes','1','Graduate','Yes',0,'Urban','high','N'),('LP002840','Female','No','0','Graduate','No',1,'Urban','low','N'),('LP002841','Male','Yes','0','Graduate','No',0,'Urban','low','N'),('LP001473','Male','No','0','Graduate','No',1,'Urban','low','Y'),('LP002459','Male','Yes','0','Graduate','No',1,'Urban','medium','Y'),('LP002143','Female','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001478','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP001570','Male','Yes','2','Graduate','No',1,'Rural','medium','Y'),('LP001482','Male','Yes','0','Graduate','Yes',1,'Semiurban','low','Y'),('LP002467','Male','Yes','0','Graduate','No',1,'Urban','low','N'),('LP002149','Male','Yes','2','Graduate','No',1,'Rural','medium','Y'),('LP002842','Male','Yes','1','Graduate','No',1,'Urban','low','Y'),('LP001572','Male','Yes','0','Graduate','No',1,'Urban','medium','Y'),('LP001487','Male','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002472','Male','No','2','Graduate','No',1,'Rural','medium','Y'),('LP002151','Male','Yes','1','Graduate','No',1,'Urban','low','N'),('LP001896','Male','Yes','2','Graduate','No',1,'Semiurban','low','Y'),('LP002855','Male','Yes','2','Graduate','No',1,'Urban','high','Y'),('LP001574','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP001488','Male','Yes','3+','Graduate','No',1,'Semiurban','medium','N'),('LP002473','Male','Yes','0','Graduate','No',1,'Semiurban','medium','N'),('LP002158','Male','Yes','0','Not Graduate','No',0,'Urban','low','N'),('LP002862','Male','Yes','2','Not Graduate','No',1,'Semiurban','medium','N'),('LP001577','Female','Yes','0','Graduate','No',1,'Rural','medium','N'),('LP002160','Male','Yes','3+','Graduate','No',1,'Semiurban','medium','Y'),('LP002484','Male','Yes','3+','Graduate','No',1,'Urban','medium','Y'),('LP001489','Female','Yes','0','Graduate','No',1,'Rural','medium','N'),('LP002863','Male','Yes','3+','Graduate','No',1,'Semiurban','medium','N'),('LP001578','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP001491','Male','Yes','2','Graduate','Yes',1,'Urban','low','Y'),('LP002161','Female','No','1','Graduate','No',1,'Semiurban','medium','N'),('LP002487','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002868','Male','Yes','2','Graduate','No',1,'Urban','low','Y'),('LP001579','Male','No','0','Graduate','No',0,'Semiurban','low','N'),('LP002170','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP002493','Male','No','0','Graduate','No',0,'Semiurban','medium','N'),('LP001492','Male','No','0','Graduate','No',0,'Semiurban','high','N'),('LP002874','Male','No','0','Graduate','No',1,'Urban','low','Y'),('LP001580','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP002175','Male','Yes','0','Graduate','No',1,'Urban','medium','Y'),('LP002494','Male','No','0','Graduate','No',1,'Rural','medium','Y'),('LP001493','Male','Yes','2','Not Graduate','No',1,'Rural','medium','N'),('LP002877','Male','Yes','1','Graduate','No',1,'Rural','low','Y'),('LP001586','Male','Yes','3+','Not Graduate','No',1,'Rural','low','N'),('LP002180','Male','No','0','Graduate','Yes',1,'Rural','medium','Y'),('LP002892','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP002500','Male','Yes','3+','Not Graduate','No',0,'Urban','low','N'),('LP001497','Male','Yes','2','Graduate','No',1,'Rural','medium','N'),('LP001594','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002181','Male','No','0','Not Graduate','No',1,'Rural','medium','N'),('LP002505','Male','Yes','0','Graduate','No',1,'Urban','medium','N'),('LP001498','Male','No','0','Graduate','No',1,'Urban','medium','Y'),('LP002893','Male','No','0','Graduate','No',1,'Urban','low','N'),('LP001900','Male','Yes','1','Graduate','No',1,'Semiurban','low','Y'),('LP002515','Male','Yes','1','Graduate','Yes',1,'Semiurban','low','Y'),('LP002187','Male','No','0','Graduate','No',1,'Semiurban','low','N'),('LP001603','Male','Yes','0','Not Graduate','Yes',1,'Semiurban','medium','N'),('LP001504','Male','No','0','Graduate','Yes',1,'Semiurban','medium','Y'),('LP002894','Female','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001903','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP002911','Male','Yes','1','Graduate','No',0,'Rural','low','N'),('LP002517','Male','Yes','1','Not Graduate','No',0,'Rural','low','N'),('LP002912','Male','Yes','1','Graduate','No',1,'Rural','medium','N'),('LP001904','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP002519','Male','Yes','3+','Graduate','No',1,'Semiurban','medium','Y'),('LP002916','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP001907','Male','Yes','0','Graduate','No',1,'Semiurban','high','Y'),('LP001910','Male','No','1','Not Graduate','Yes',0,'Urban','medium','N'),('LP001606','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002917','Female','No','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP001914','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001608','Male','Yes','2','Graduate','No',1,'Rural','low','Y'),('LP001915','Male','Yes','2','Graduate','No',1,'Urban','low','Y'),('LP002926','Male','Yes','2','Graduate','Yes',0,'Semiurban','low','N'),('LP001610','Male','Yes','3+','Graduate','No',0,'Semiurban','medium','N'),('LP001917','Female','No','0','Graduate','No',1,'Urban','low','Y'),('LP001155','Female','Yes','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP002524','Male','No','2','Graduate','No',1,'Rural','medium','Y'),('LP002188','Male','No','0','Graduate','No',0,'Rural','medium','N'),('LP002928','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001507','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP002527','Male','Yes','2','Graduate','Yes',1,'Rural','high','Y'),('LP001508','Male','Yes','2','Graduate','No',1,'Urban','high','Y'),('LP002529','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP001616','Male','Yes','1','Graduate','No',1,'Semiurban','low','Y'),('LP001922','Male','Yes','0','Graduate','No',1,'Rural','high','N'),('LP002531','Male','Yes','1','Graduate','Yes',1,'Semiurban','high','Y'),('LP001630','Male','No','0','Not Graduate','No',0,'Urban','low','N'),('LP002190','Male','Yes','1','Graduate','No',1,'Semiurban','medium','Y'),('LP001924','Male','No','0','Graduate','No',1,'Rural','low','Y'),('LP002533','Male','Yes','2','Graduate','No',1,'Urban','low','N'),('LP001633','Male','Yes','1','Graduate','No',0,'Urban','medium','N'),('LP002191','Male','Yes','0','Graduate','No',1,'Rural','high','N'),('LP001925','Female','No','0','Graduate','Yes',1,'Semiurban','low','N'),('LP002534','Female','No','0','Not Graduate','No',1,'Rural','medium','Y'),('LP001636','Male','Yes','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002194','Female','No','0','Graduate','Yes',1,'Semiurban','high','Y'),('LP001926','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002536','Male','Yes','3+','Not Graduate','No',1,'Rural','low','Y'),('LP001637','Male','Yes','1','Graduate','No',1,'Semiurban','high','N'),('LP002197','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP001931','Female','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002537','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001639','Female','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP002201','Male','Yes','2','Graduate','Yes',1,'Rural','medium','Y'),('LP002541','Male','Yes','0','Graduate','No',1,'Semiurban','high','Y'),('LP001935','Male','No','0','Graduate','No',1,'Rural','medium','Y'),('LP001640','Male','Yes','0','Graduate','Yes',1,'Semiurban','high','Y'),('LP002205','Male','No','1','Graduate','No',0,'Urban','low','N'),('LP002543','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP001936','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP001641','Male','Yes','1','Graduate','Yes',0,'Rural','low','N'),('LP002211','Male','Yes','0','Graduate','No',1,'Urban','medium','Y'),('LP002544','Male','Yes','1','Not Graduate','No',1,'Rural','low','Y'),('LP001938','Male','Yes','2','Graduate','No',0,'Semiurban','medium','N'),('LP002219','Male','Yes','3+','Graduate','No',1,'Rural','medium','Y'),('LP001647','Male','Yes','0','Graduate','No',1,'Rural','medium','Y'),('LP002545','Male','No','2','Graduate','No',0,'Rural','low','N'),('LP001940','Male','Yes','2','Graduate','No',1,'Urban','low','Y'),('LP001653','Male','No','0','Not Graduate','No',1,'Rural','medium','Y'),('LP002547','Male','Yes','1','Graduate','No',1,'Urban','high','N'),('LP001157','Female','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP001947','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001656','Male','No','0','Graduate','No',1,'Semiurban','high','N'),('LP002555','Male','Yes','2','Graduate','Yes',1,'Semiurban','medium','Y'),('LP001657','Male','Yes','0','Not Graduate','No',1,'Urban','medium','N'),('LP002556','Male','No','0','Graduate','No',1,'Urban','low','N'),('LP001658','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP002571','Male','No','0','Not Graduate','No',1,'Rural','low','Y'),('LP001664','Male','No','0','Graduate','No',1,'Rural','medium','Y'),('LP002582','Female','No','0','Not Graduate','Yes',1,'Semiurban','high','Y'),('LP001164','Female','No','0','Graduate','No',1,'Semiurban','medium','N'),('LP001665','Male','Yes','1','Graduate','No',1,'Semiurban','low','N'),('LP002585','Male','Yes','0','Graduate','No',0,'Rural','low','N'),('LP001666','Male','No','0','Graduate','No',1,'Rural','medium','Y'),('LP002586','Female','Yes','1','Graduate','No',1,'Semiurban','low','Y'),('LP001669','Female','No','0','Not Graduate','No',1,'Urban','low','Y'),('LP002931','Male','Yes','2','Graduate','Yes',1,'Semiurban','medium','N'),('LP002587','Male','Yes','0','Not Graduate','No',1,'Rural','low','Y'),('LP001673','Male','No','0','Graduate','Yes',1,'Urban','high','N'),('LP002936','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002600','Male','Yes','1','Graduate','Yes',1,'Semiurban','low','Y'),('LP001514','Female','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001674','Male','Yes','1','Not Graduate','No',1,'Semiurban','low','Y'),('LP002938','Male','Yes','0','Graduate','Yes',1,'Urban','high','Y'),('LP002602','Male','No','0','Graduate','No',0,'Rural','medium','N'),('LP001677','Male','No','2','Graduate','No',0,'Semiurban','medium','Y'),('LP001516','Female','Yes','2','Graduate','No',1,'Urban','high','Y'),('LP002940','Male','No','0','Not Graduate','No',1,'Rural','low','Y'),('LP002603','Female','No','0','Graduate','No',1,'Rural','low','Y'),('LP001179','Male','Yes','2','Graduate','No',1,'Urban','medium','N'),('LP001682','Male','Yes','3+','Not Graduate','No',1,'Urban','low','N'),('LP002941','Male','Yes','2','Not Graduate','Yes',1,'Rural','medium','N'),('LP002606','Female','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP001518','Male','Yes','1','Graduate','No',1,'Urban','low','Y'),('LP001688','Male','Yes','1','Not Graduate','No',1,'Urban','low','Y'),('LP002945','Male','Yes','0','Graduate','Yes',1,'Rural','medium','Y'),('LP002615','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP001691','Male','Yes','2','Not Graduate','No',1,'Semiurban','low','Y'),('LP001519','Female','No','0','Graduate','No',1,'Rural','high','N'),('LP002948','Male','Yes','2','Graduate','No',1,'Urban','medium','Y'),('LP002619','Male','Yes','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP001692','Female','No','0','Not Graduate','No',1,'Semiurban','medium','Y'),('LP002953','Male','Yes','3+','Graduate','No',1,'Urban','medium','Y'),('LP002622','Male','Yes','2','Graduate','No',1,'Rural','low','Y'),('LP001693','Female','No','0','Graduate','No',1,'Urban','low','Y'),('LP001186','Female','Yes','1','Graduate','Yes',0,'Urban','high','N'),('LP002958','Male','No','0','Graduate','No',1,'Rural','low','Y'),('LP002626','Male','Yes','0','Graduate','Yes',1,'Urban','low','Y'),('LP001698','Male','No','0','Not Graduate','No',1,'Rural','low','Y'),('LP002959','Female','Yes','1','Graduate','No',1,'Semiurban','high','Y'),('LP002634','Female','No','1','Graduate','No',1,'Urban','high','Y'),('LP001194','Male','Yes','2','Graduate','No',1,'Semiurban','low','Y'),('LP002960','Male','Yes','0','Not Graduate','No',1,'Urban','low','N'),('LP002637','Male','No','0','Not Graduate','No',1,'Rural','low','N'),('LP001195','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP002961','Male','Yes','1','Graduate','No',1,'Semiurban','low','Y'),('LP002640','Male','Yes','1','Graduate','No',1,'Semiurban','medium','Y'),('LP002964','Male','Yes','2','Not Graduate','No',1,'Rural','low','Y'),('LP001197','Male','Yes','0','Graduate','No',1,'Rural','low','N'),('LP002643','Male','Yes','2','Graduate','No',1,'Urban','low','Y'),('LP002974','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002648','Male','Yes','0','Graduate','No',1,'Semiurban','low','N'),('LP001198','Male','Yes','1','Graduate','No',1,'Urban','medium','Y'),('LP002652','Male','No','0','Graduate','No',1,'Rural','medium','N'),('LP002978','Female','No','0','Graduate','No',1,'Rural','low','Y'),('LP001199','Male','Yes','2','Not Graduate','No',1,'Urban','low','Y'),('LP002659','Male','Yes','3+','Graduate','No',1,'Rural','low','Y'),('LP002979','Male','Yes','3+','Graduate','No',1,'Rural','medium','Y'),('LP001205','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP002670','Female','Yes','2','Graduate','No',1,'Semiurban','low','Y'),('LP002983','Male','Yes','1','Graduate','No',1,'Urban','medium','Y'),('LP001206','Male','Yes','3+','Graduate','No',1,'Urban','low','Y'),('LP002683','Male','No','0','Graduate','No',1,'Semiurban','medium','N'),('LP002684','Female','No','0','Not Graduate','No',1,'Rural','low','N'),('LP001207','Male','Yes','0','Not Graduate','Yes',0,'Rural','low','N'),('LP002984','Male','Yes','2','Graduate','No',1,'Urban','medium','Y'),('LP002689','Male','Yes','2','Not Graduate','No',1,'Semiurban','low','Y'),('LP001213','Male','Yes','1','Graduate','No',0,'Rural','medium','N'),('LP002690','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP002990','Female','No','0','Graduate','Yes',0,'Semiurban','medium','N'),('LP002692','Male','Yes','3+','Graduate','Yes',1,'Rural','medium','Y'),('LP001222','Female','No','0','Graduate','No',0,'Semiurban','medium','N'),('LP002693','Male','Yes','2','Graduate','Yes',1,'Rural','medium','Y'),('LP001225','Male','Yes','0','Graduate','No',1,'Semiurban','medium','N'),('LP002697','Male','No','0','Graduate','No',1,'Semiurban','medium','N'),('LP001228','Male','No','0','Not Graduate','No',0,'Urban','low','N'),('LP002699','Male','Yes','2','Graduate','Yes',1,'Rural','high','Y'),('LP002705','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001233','Male','Yes','1','Graduate','No',1,'Urban','high','Y'),('LP002706','Male','Yes','1','Not Graduate','No',0,'Semiurban','medium','Y'),('LP001238','Male','Yes','3+','Not Graduate','Yes',1,'Urban','medium','Y'),('LP001241','Female','No','0','Graduate','No',0,'Semiurban','medium','N'),('LP001699','Male','No','0','Graduate','No',1,'Urban','low','Y'),('LP001243','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP001702','Male','No','0','Graduate','No',1,'Semiurban','low','N'),('LP001708','Female','No','0','Graduate','No',1,'Semiurban','high','N'),('LP001711','Male','Yes','3+','Graduate','No',0,'Semiurban','low','N'),('LP001713','Male','Yes','1','Graduate','Yes',1,'Urban','medium','Y'),('LP001715','Male','Yes','3+','Not Graduate','Yes',1,'Rural','medium','Y'),('LP001716','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP001720','Male','Yes','3+','Not Graduate','No',1,'Semiurban','low','Y'),('LP001722','Male','Yes','0','Graduate','No',1,'Rural','low','N'),('LP001726','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP001736','Male','Yes','0','Graduate','No',0,'Urban','low','N'),('LP001743','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP002224','Male','No','0','Graduate','No',1,'Urban','low','N'),('LP002225','Male','Yes','2','Graduate','No',1,'Urban','medium','Y'),('LP002229','Male','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002231','Female','No','0','Graduate','No',1,'Urban','medium','Y'),('LP002234','Male','No','0','Graduate','Yes',1,'Urban','medium','Y'),('LP002236','Male','Yes','2','Graduate','No',1,'Urban','medium','N'),('LP002239','Male','No','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP002243','Male','Yes','0','Not Graduate','No',0,'Urban','low','N'),('LP002244','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP002250','Male','Yes','0','Graduate','No',1,'Rural','medium','Y'),('LP002255','Male','No','3+','Graduate','No',1,'Rural','medium','Y'),('LP002262','Male','Yes','3+','Graduate','No',1,'Rural','medium','Y'),('LP002265','Male','Yes','2','Not Graduate','No',1,'Semiurban','low','Y'),('LP002266','Male','Yes','2','Graduate','No',1,'Urban','low','Y'),('LP002277','Female','No','0','Graduate','No',0,'Urban','low','N'),('LP002281','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP002284','Male','No','0','Not Graduate','No',1,'Rural','low','Y'),('LP002287','Female','No','0','Graduate','No',0,'Semiurban','low','N'),('LP002288','Male','Yes','2','Not Graduate','No',0,'Urban','low','N'),('LP002296','Male','No','0','Not Graduate','No',1,'Rural','low','N'),('LP002297','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP002300','Female','No','0','Not Graduate','No',1,'Semiurban','low','Y'),('LP002301','Female','No','0','Graduate','Yes',1,'Rural','medium','N'),('LP002305','Female','No','0','Graduate','No',1,'Semiurban','medium','Y'),('LP002308','Male','Yes','0','Not Graduate','No',1,'Urban','low','Y'),('LP002314','Female','No','0','Not Graduate','No',1,'Rural','low','Y'),('LP002315','Male','Yes','1','Graduate','No',0,'Semiurban','medium','N'),('LP002317','Male','Yes','3+','Graduate','No',0,'Rural','high','N'),('LP002318','Female','No','1','Not Graduate','Yes',1,'Semiurban','low','N'),('LP002328','Male','Yes','0','Not Graduate','No',0,'Rural','medium','N'),('LP002332','Male','Yes','0','Not Graduate','No',1,'Rural','low','Y'),('LP002335','Female','Yes','0','Not Graduate','No',0,'Semiurban','low','N'),('LP002337','Female','No','0','Graduate','No',1,'Urban','low','Y'),('LP002341','Female','No','1','Graduate','No',1,'Urban','low','N'),('LP002342','Male','Yes','2','Graduate','Yes',1,'Urban','low','N'),('LP002345','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002347','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP002348','Male','Yes','0','Graduate','No',1,'Rural','medium','Y'),('LP002357','Female','No','0','Not Graduate','No',0,'Urban','low','N'),('LP002361','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP002362','Male','Yes','1','Graduate','No',0,'Urban','medium','N'),('LP002364','Male','Yes','0','Graduate','No',1,'Semiurban','high','Y'),('LP002366','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002367','Female','No','1','Not Graduate','No',1,'Rural','medium','N'),('LP002368','Male','Yes','2','Graduate','No',1,'Semiurban','medium','Y'),('LP002369','Male','Yes','0','Graduate','No',1,'Rural','low','Y'),('LP002370','Male','No','0','Not Graduate','No',1,'Urban','low','Y'),('LP002377','Female','No','1','Graduate','Yes',1,'Semiurban','medium','Y'),('LP002379','Male','No','0','Graduate','No',0,'Rural','medium','N'),('LP002387','Male','Yes','0','Graduate','No',1,'Semiurban','low','Y'),('LP002390','Male','No','0','Graduate','No',1,'Urban','low','Y'),('LP002398','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP002401','Male','Yes','0','Graduate','No',1,'Urban','low','Y'),('LP002403','Male','No','0','Graduate','Yes',0,'Urban','high','N'),('LP002407','Female','Yes','0','Not Graduate','Yes',1,'Rural','medium','Y'),('LP002408','Male','No','0','Graduate','No',1,'Semiurban','low','Y'),('LP002409','Male','Yes','0','Graduate','No',1,'Rural','medium','Y'),('LP002418','Male','No','3+','Not Graduate','No',1,'Semiurban','medium','Y'),('LP002422','Male','No','1','Graduate','No',1,'Semiurban','high','Y'),('LP002429','Male','Yes','1','Graduate','Yes',1,'Rural','low','Y'),('LP002434','Male','Yes','2','Not Graduate','No',1,'Rural','medium','Y'),('LP002443','Male','Yes','2','Graduate','No',0,'Rural','low','N'),('LP002446','Male','Yes','2','Not Graduate','No',0,'Rural','low','N');
/*!40000 ALTER TABLE `cdw-sapp_loan_application` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-10-19  5:13:44
