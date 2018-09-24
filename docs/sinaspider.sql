-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- 主机： localhost
-- 生成日期： 2018-09-24 06:54:49
-- 服务器版本： 10.1.23-MariaDB-9+deb9u1
-- PHP 版本： 7.0.30-0+deb9u1

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- 数据库： `sinaspider`
--

-- --------------------------------------------------------

--
-- 表的结构 `dpzs`
--

CREATE TABLE `dpzs` (
  `id` bigint(20) NOT NULL,
  `symbol` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `price` varchar(20) NOT NULL,
  `buy` varchar(20) NOT NULL,
  `sell` varchar(20) NOT NULL,
  `settlement` varchar(20) NOT NULL,
  `open` varchar(20) NOT NULL,
  `high` varchar(20) NOT NULL,
  `low` varchar(20) NOT NULL,
  `volume` varchar(20) NOT NULL,
  `amount` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `created` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `NodeList`
--

CREATE TABLE `NodeList` (
  `symbol` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `node` varchar(10) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `sh_a`
--

CREATE TABLE `sh_a` (
  `id` bigint(20) NOT NULL,
  `symbol` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `price` varchar(20) NOT NULL,
  `buy` varchar(20) NOT NULL,
  `sell` varchar(20) NOT NULL,
  `settlement` varchar(20) NOT NULL,
  `open` varchar(20) NOT NULL,
  `high` varchar(20) NOT NULL,
  `low` varchar(20) NOT NULL,
  `volume` varchar(20) NOT NULL,
  `amount` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `created` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `sh_b`
--

CREATE TABLE `sh_b` (
  `id` bigint(20) NOT NULL,
  `symbol` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `price` varchar(20) NOT NULL,
  `buy` varchar(20) NOT NULL,
  `sell` varchar(20) NOT NULL,
  `settlement` varchar(20) NOT NULL,
  `open` varchar(20) NOT NULL,
  `high` varchar(20) NOT NULL,
  `low` varchar(20) NOT NULL,
  `volume` varchar(20) NOT NULL,
  `amount` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `created` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `sz_a`
--

CREATE TABLE `sz_a` (
  `id` bigint(20) NOT NULL,
  `symbol` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `price` varchar(20) NOT NULL,
  `buy` varchar(20) NOT NULL,
  `sell` varchar(20) NOT NULL,
  `settlement` varchar(20) NOT NULL,
  `open` varchar(20) NOT NULL,
  `high` varchar(20) NOT NULL,
  `low` varchar(20) NOT NULL,
  `volume` varchar(20) NOT NULL,
  `amount` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `created` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `sz_b`
--

CREATE TABLE `sz_b` (
  `id` bigint(20) NOT NULL,
  `symbol` varchar(20) NOT NULL,
  `name` varchar(30) NOT NULL,
  `price` varchar(20) NOT NULL,
  `buy` varchar(20) NOT NULL,
  `sell` varchar(20) NOT NULL,
  `settlement` varchar(20) NOT NULL,
  `open` varchar(20) NOT NULL,
  `high` varchar(20) NOT NULL,
  `low` varchar(20) NOT NULL,
  `volume` varchar(20) NOT NULL,
  `amount` varchar(20) NOT NULL,
  `date` varchar(20) NOT NULL,
  `time` varchar(20) NOT NULL,
  `created` varchar(20) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转储表的索引
--

--
-- 表的索引 `dpzs`
--
ALTER TABLE `dpzs`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `NodeList`
--
ALTER TABLE `NodeList`
  ADD PRIMARY KEY (`symbol`) USING BTREE;

--
-- 表的索引 `sh_a`
--
ALTER TABLE `sh_a`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `sh_b`
--
ALTER TABLE `sh_b`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `sz_a`
--
ALTER TABLE `sz_a`
  ADD PRIMARY KEY (`id`);

--
-- 表的索引 `sz_b`
--
ALTER TABLE `sz_b`
  ADD PRIMARY KEY (`id`);

--
-- 在导出的表使用AUTO_INCREMENT
--

--
-- 使用表AUTO_INCREMENT `dpzs`
--
ALTER TABLE `dpzs`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `sh_a`
--
ALTER TABLE `sh_a`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `sh_b`
--
ALTER TABLE `sh_b`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `sz_a`
--
ALTER TABLE `sz_a`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;

--
-- 使用表AUTO_INCREMENT `sz_b`
--
ALTER TABLE `sz_b`
  MODIFY `id` bigint(20) NOT NULL AUTO_INCREMENT;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
