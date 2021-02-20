CREATE TABLE `artigos` (
  `id` int NOT NULL AUTO_INCREMENT,
  `titulo` varchar(500) NOT NULL,
  `data` date NOT NULL,
  `base_dados` varchar(500) NOT NULL,
  `tecnica` varchar(500) NOT NULL,
  `acuracia` varchar(500) NOT NULL,
  `precisao` varchar(500) NOT NULL,
  `deficiencia` varchar(500) NOT NULL,
  `desafio` varchar(500) NOT NULL,
  PRIMARY KEY (`id`)
)
