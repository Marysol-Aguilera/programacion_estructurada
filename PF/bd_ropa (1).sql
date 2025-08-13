-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 07-08-2025 a las 09:34:08
-- Versión del servidor: 10.4.32-MariaDB
-- Versión de PHP: 8.2.12

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `bd_ropa`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `prendas`
--

CREATE TABLE `prendas` (
  `id_prenda` int(11) NOT NULL,
  `marca` varchar(100) NOT NULL,
  `tipo` varchar(100) NOT NULL,
  `talla` varchar(100) NOT NULL,
  `precio` varchar(100) NOT NULL,
  `color` varchar(100) NOT NULL,
  `id_proveedor` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `prendas`
--

INSERT INTO `prendas` (`id_prenda`, `marca`, `tipo`, `talla`, `precio`, `color`, `id_proveedor`) VALUES
(1, 'PRUEBA3', 'PRUEBA3', 'PRUEBA3', 'PRUEBA3', 'PRUEBA3', 0),
(4, 'GUCCI', 'PLAYERA', 'M', '1500', 'NEGRO', 0),
(5, 'LEVIS', 'PANTALON', 'M', '1500', 'AZUL', 0),
(8, 'PRUEBA MARLEN 2', 'P M 2', 'P M 2', 'p m 2', 'P M 2', 0),
(10, 'pm7', 'pm7', 'pm7', 'pm7', 'pm7', 4),
(12, 'prueba 10', 'prueba 10', 'prueba 10', 'prueba 10', 'prueba 10', 4),
(13, 'p12', 'p12', 'p12', 'p12', 'p12', 4);

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `proveedores`
--

CREATE TABLE `proveedores` (
  `id_proveedor` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `telefono` varchar(10) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `proveedores`
--

INSERT INTO `proveedores` (`id_proveedor`, `nombre`, `telefono`, `email`, `password`) VALUES
(1, 'Dulce', '6181761987', 'dulce@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(4, 'marlene', '6181091866', 'marlen@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4'),
(5, 'marysol@gmail.com', '6180985476', 'marysol@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `roles`
--

CREATE TABLE `roles` (
  `id_admin` int(11) NOT NULL,
  `nombre` varchar(100) NOT NULL,
  `email` varchar(100) NOT NULL,
  `password` varchar(255) NOT NULL,
  `rol` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Volcado de datos para la tabla `roles`
--

INSERT INTO `roles` (`id_admin`, `nombre`, `email`, `password`, `rol`) VALUES
(1, 'marysol aguilera', 'marysol@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'admin'),
(2, 'marlen', 'marlen@gmail.com', '03ac674216f3e15c761ee1a5e255f067953623c8b388b4459e13f978d7c846f4', 'supervisor');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `prendas`
--
ALTER TABLE `prendas`
  ADD PRIMARY KEY (`id_prenda`);

--
-- Indices de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD PRIMARY KEY (`id_proveedor`);

--
-- Indices de la tabla `roles`
--
ALTER TABLE `roles`
  ADD PRIMARY KEY (`id_admin`),
  ADD UNIQUE KEY `email` (`email`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `prendas`
--
ALTER TABLE `prendas`
  MODIFY `id_prenda` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;

--
-- AUTO_INCREMENT de la tabla `proveedores`
--
ALTER TABLE `proveedores`
  MODIFY `id_proveedor` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=6;

--
-- AUTO_INCREMENT de la tabla `roles`
--
ALTER TABLE `roles`
  MODIFY `id_admin` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- Restricciones para tablas volcadas
--

--
-- Filtros para la tabla `proveedores`
--
ALTER TABLE `proveedores`
  ADD CONSTRAINT `proveedores_ibfk_1` FOREIGN KEY (`id_proveedor`) REFERENCES `prendas` (`id_prenda`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
