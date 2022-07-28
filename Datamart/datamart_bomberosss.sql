CREATE SCHEMA IF NOT EXISTS `datamart_bombero` DEFAULT CHARACTER SET utf8 ;
USE `datamart_bombero` ;

-- -----------------------------------------------------
-- Table `datamart_bombero`.`dim_emergencias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `datamart_bombero`.`dim_emergencias` (
  `id` INT NOT NULL,
  `descripcion` VARCHAR(45) NOT NULL,
  `caso` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `datamart_bombero`.`dim_estacion`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `datamart_bombero`.`dim_estacion` (
  `id` INT NOT NULL,
  `direccion` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `datamart_bombero`.`dim_tiempo`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `datamart_bombero`.`dim_tiempo` (
  `fecha` DATE NOT NULL,
  `mes` INT NOT NULL,
  `año` INT NOT NULL,
  PRIMARY KEY (`fecha`))
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `datamart_bombero`.`hecho_incidencias`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `datamart_bombero`.`hecho_incidencias` (
  `dim_emergencias_id` INT NOT NULL,
  `dim_estacion_id` INT NOT NULL,
  `dim_tiempo_fecha` DATE NOT NULL,
  `hecho` INT NOT NULL,
  INDEX `fk_hecho_incidencias_dim_emergencias_idx` (`dim_emergencias_id` ASC) VISIBLE,
  INDEX `fk_hecho_incidencias_dim_estacion1_idx` (`dim_estacion_id` ASC) VISIBLE,
  PRIMARY KEY (`dim_emergencias_id`, `dim_estacion_id`, `dim_tiempo_fecha`),
  INDEX `fk_hecho_incidencias_dim_tiempo1_idx` (`dim_tiempo_fecha` ASC) VISIBLE,
  CONSTRAINT `fk_hecho_incidencias_dim_emergencias`
    FOREIGN KEY (`dim_emergencias_id`)
    REFERENCES `datamart_bombero`.`dim_emergencias` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_hecho_incidencias_dim_estacion1`
    FOREIGN KEY (`dim_estacion_id`)
    REFERENCES `datamart_bombero`.`dim_estacion` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION,
  CONSTRAINT `fk_hecho_incidencias_dim_tiempo1`
    FOREIGN KEY (`dim_tiempo_fecha`)
    REFERENCES `datamart_bombero`.`dim_tiempo` (`fecha`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


