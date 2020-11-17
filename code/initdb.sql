USE `newdatabase`;

CREATE TABLE IF NOT EXISTS `cpu_usage`(
     `usage` DECIMAL(5,2) NOT NULL,
     `taken_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX(`taken_at`)
);
CREATE TABLE IF NOT EXISTS `mem_usage`(
     `usage` BIGINT NOT NULL,
     `free` BIGINT NOT NULL,
     `taken_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX(`taken_at`)
);
CREATE TABLE IF NOT EXISTS `disk_usage`(
     `usage` BIGINT NOT NULL,
     `free` BIGINT NOT NULL,
     `taken_at` TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    INDEX(`taken_at`)
);
