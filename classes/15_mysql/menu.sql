
CREATE DATABASE `menu`;
USE menu;

DROP TABLE IF EXISTS `fish`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;

CREATE TABLE `fish` (
    `ID` int(11) NOT NULL auto_increment,
    `NAME` varchar(30) NOT NULL default '',
    `PRICE` decimal(5,2) NOT NULL default '0.00',
    PRIMARY KEY (`ID`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT
CHARSET=latin1;
SET character_set_client = @saved_cs_client;

LOCK TABLES `fish` WRITE;
INSERT INTO `fish` VALUES
(1,'catfish','8.50'),(2,'catfish','8.50'),(3,'tuna','8.00'),(4,'catfish','5.00'),(5,'bass','6.75'),(6,'haddock','6.50'),(7,'salmon','9.50'),(8,'trout','6.00'),(9,'tuna','7.50'),(10,'yellowfin tuna','12.00'),(11,'yellowfin tuna','13.00'),(12,'tuna','7.50');
UNLOCK TABLES;
