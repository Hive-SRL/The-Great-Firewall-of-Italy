create database thegreatfirewall;

create user 'thegreat'@'localhost' identified by 'yhiQi8S84N0V';
grant all privileges on thegreatfirewall.* TO 'thegreat'@'localhost';
flush privileges;