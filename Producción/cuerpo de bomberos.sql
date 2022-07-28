-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema cuerpo_bomberos
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema cuerpo_bomberos
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `cuerpo_bomberos` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `cuerpo_bomberos` ;

-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`usuario`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`usuario` (
  `USUARIO_ID` INT NOT NULL,
  `USUARIO_CEDULA` VARCHAR(45) NOT NULL,
  `USUARIO_NOMBRE` VARCHAR(45) NOT NULL,
  `USUARIO_APELLIDO` VARCHAR(45) NOT NULL,
  `USUARIO_GENERO` VARCHAR(45) NOT NULL,
  `USUARIO_DIRECCION` VARCHAR(45) NOT NULL,
  `SUARIO_TELEFONO` VARCHAR(45) NOT NULL,
  `USUARIO_FECHA` DATE NOT NULL,
  `USUARIO_HORA` TIME NOT NULL,
  PRIMARY KEY (`USUARIO_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`puesto_institucional`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`puesto_institucional` (
  `PUESTO_ID` INT NOT NULL,
  `PUESTO_PERTENECE` VARCHAR(45) NOT NULL,
  `PUESTO_CARGO` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`PUESTO_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`estacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`estacion` (
  `ESTACION_ID` INT NOT NULL,
  `ESTACION_DIRECCION` VARCHAR(45) NOT NULL,
  `ESTACION_TELEFONO` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ESTACION_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`bombero`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`bombero` (
  `BOMBERO_ID` INT NOT NULL,
  `ESTACION_ID` INT NOT NULL,
  `PUESTO_ID` INT NOT NULL,
  `BOMBERO_NOMBRE` VARCHAR(45) NOT NULL,
  `BOMBERO_APELLIDO` VARCHAR(45) NOT NULL,
  `BOMBERO_CI` VARCHAR(45) NOT NULL,
  `BOMBERO_GENERO` VARCHAR(45) NOT NULL,
  `BOMBERO_TELEFONO` VARCHAR(45) NOT NULL,
  `BOMBERO_FECHANACIMIENTO` VARCHAR(45) NOT NULL,
  `BOMBERO_CORREO` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`BOMBERO_ID`),
  INDEX `ESTACION_ID_idx` (`ESTACION_ID` ASC) VISIBLE,
  INDEX `PUESTO_ID_idx` (`PUESTO_ID` ASC) VISIBLE,
  CONSTRAINT `ESTACION_ID`
    FOREIGN KEY (`ESTACION_ID`)
    REFERENCES `cuerpo_bomberos`.`estacion` (`ESTACION_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `PUESTO_ID`
    FOREIGN KEY (`PUESTO_ID`)
    REFERENCES `cuerpo_bomberos`.`puesto_institucional` (`PUESTO_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`vehiculo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`vehiculo` (
  `VEHICULO_ID` INT NOT NULL,
  `ESTACION_ID` INT NOT NULL,
  `VEHICULO_PLACA` VARCHAR(45) NOT NULL,
  `VEHICULO_MARCA` VARCHAR(45) NOT NULL,
  `VEHICULO_TIPO` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`VEHICULO_ID`),
  INDEX `ESTACION_ID_idx` (`ESTACION_ID` ASC) VISIBLE,
  CONSTRAINT `ESTACION_ID`
    FOREIGN KEY (`ESTACION_ID`)
    REFERENCES `cuerpo_bomberos`.`estacion` (`ESTACION_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`emergencia`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`emergencia` (
  `EMERGENCIA_ID` INT NOT NULL,
  `EMERGENCIA_TIPO` VARCHAR(45) NOT NULL,
  `EMERGENCIA_DESCRIPCION` VARCHAR(45) NOT NULL,
  `EMERGENCIA_CASO` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`EMERGENCIA_ID`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`informe_de_estacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`informe_de_estacion` (
  `INF_ID` INT NOT NULL,
  `EMERGENCIA_ID` INT NOT NULL,
  `INF_DESCRIPCION` VARCHAR(45) NOT NULL,
  `INF_DEFUNCIONES` VARCHAR(45) NOT NULL,
  `INF_FECHA` DATE NOT NULL,
  PRIMARY KEY (`INF_ID`),
  INDEX `EMERGENCIA_ID_idx` (`EMERGENCIA_ID` ASC) VISIBLE,
  CONSTRAINT `EMERGENCIA_ID`
    FOREIGN KEY (`EMERGENCIA_ID`)
    REFERENCES `cuerpo_bomberos`.`emergencia` (`EMERGENCIA_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`atiende`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`atiende` (
  `ATIENDE_ID` INT NOT NULL,
  `USUARIO_ID` INT NOT NULL,
  `BOMBERO_ID` INT NOT NULL,
  `INF_ID` INT NOT NULL,
  `VEHICULO_ID` INT NOT NULL,
  PRIMARY KEY (`ATIENDE_ID`),
  INDEX `USUARIO_ID_idx` (`USUARIO_ID` ASC) VISIBLE,
  INDEX `BOMBERO_ID_idx` (`BOMBERO_ID` ASC) VISIBLE,
  INDEX `INF_ID_idx` (`INF_ID` ASC) VISIBLE,
  INDEX `VEHICULO_ID_idx` (`VEHICULO_ID` ASC) VISIBLE,
  CONSTRAINT `USUARIO_ID`
    FOREIGN KEY (`USUARIO_ID`)
    REFERENCES `cuerpo_bomberos`.`usuario` (`USUARIO_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `BOMBERO_ID`
    FOREIGN KEY (`BOMBERO_ID`)
    REFERENCES `cuerpo_bomberos`.`bombero` (`BOMBERO_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `INF_ID`
    FOREIGN KEY (`INF_ID`)
    REFERENCES `cuerpo_bomberos`.`informe_de_estacion` (`INF_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `VEHICULO_ID`
    FOREIGN KEY (`VEHICULO_ID`)
    REFERENCES `cuerpo_bomberos`.`vehiculo` (`VEHICULO_ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`dim_tiempo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`dim_tiempo` (
  `fecha` DATE NOT NULL,
  `dia` INT NOT NULL,
  `año` INT NOT NULL,
  PRIMARY KEY (`fecha`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`dim_estacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`dim_estacion` (
  `id` INT NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`dim_emergencias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`dim_emergencias` (
  `id` INT NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `caso` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `cuerpo_bomberos`.`hecho_incidencias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `cuerpo_bomberos`.`hecho_incidencias` (
  `dim_tiempo_fecha` DATE NOT NULL,
  `dim_estacion_id` INT NOT NULL,
  `dim_emergencias_id` INT NOT NULL,
  `hecho` INT NOT NULL,
  INDEX `fk_hecho_incidencias_dim_tiempo1_idx` (`dim_tiempo_fecha` ASC) VISIBLE,
  INDEX `fk_hecho_incidencias_dim_estacion1_idx` (`dim_estacion_id` ASC) VISIBLE,
  INDEX `fk_hecho_incidencias_dim_emergencias1_idx` (`dim_emergencias_id` ASC) VISIBLE,
  PRIMARY KEY (`dim_tiempo_fecha`, `dim_estacion_id`, `dim_emergencias_id`),
  CONSTRAINT `fk_hecho_incidencias_dim_tiempo1`
    FOREIGN KEY (`dim_tiempo_fecha`)
    REFERENCES `cuerpo_bomberos`.`dim_tiempo` (`fecha`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_hecho_incidencias_dim_estacion1`
    FOREIGN KEY (`dim_estacion_id`)
    REFERENCES `cuerpo_bomberos`.`dim_estacion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_hecho_incidencias_dim_emergencias1`
    FOREIGN KEY (`dim_emergencias_id`)
    REFERENCES `cuerpo_bomberos`.`dim_emergencias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
