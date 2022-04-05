CREATE DATABASE Discord;

CREATE USER 'python'@'localhost' IDENTIFIED BY 'Chb4ug8h#d';
GRANT DELETE, UPDATE, INSERT, SELECT ON Discord.* TO 'python'@'localhost';
FLUSH PRIVILEGES;

USE Discord;

CREATE TABLE AuthChannels(
    ChannelId bigint,
    Region varchar(3)
);
CREATE TABLE BannedUser(
    UserId bigint
);
CREATE TABLE Busy(
    UserId bigint
);
CREATE TABLE Working(
    UserId bigint
);
CREATE TABLE UserInfo(
    UserId bigint,
    Name varchar(255)
);

