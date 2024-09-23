Create Database	Prueba;

CREATE TABLE `prueba`.`personas` (
  personaspersonas`id` INT NOT NULL,
  `nombre` VARCHAR(45) NULL,
  `edad` INT NULL,
  `ciudad` VARCHAR(45) NULL,
  `salario` DECIMAL NULL,
  PRIMARY KEY (`id`));

INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('1', 'CHRISTIAN', '20', 'LIMA', '7500');
INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('2', 'ALEX', '25', 'ICA', '3500');
INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('3', 'MARIA', '40', 'ICA', '5849');
INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('4', 'JUANA', '25', 'ICA', '3045');
INSERT INTO `prueba`.`personas` (`id`, `nombre`, `edad`, `ciudad`, `salario`) VALUES ('5', 'ELIZABETH', '30', 'ICA', '2345');

