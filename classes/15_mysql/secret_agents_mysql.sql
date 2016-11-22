
CREATE DATABASE `secret_agents`;
USE secret_agents;

DROP TABLE IF EXISTS `agents`;
SET @saved_cs_client     = @@character_set_client;
SET character_set_client = utf8;

CREATE TABLE `agents` (
    `agentID` int(11) NOT NULL auto_increment,
    `code_name` varchar(3) NOT NULL default '007',
    `name` varchar(30) NOT NULL default 'James Bond',
    PRIMARY KEY (`agentID`)
) ENGINE=MyISAM AUTO_INCREMENT=27 DEFAULT
CHARSET=latin1;
SET character_set_client = @saved_cs_client;

LOCK TABLES `agents` WRITE;
INSERT INTO `agents` VALUES (1,'001','Edward Donne');
UNLOCK TABLES;
