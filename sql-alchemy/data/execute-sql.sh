#!/bin/bash
clear
@echo off
echo execute school-database.sql...
mysql -u root -padmin < school-database.sql
echo execute student-table.sql...
mysql -u root -padmin < student-table.sql

# echo property to user root
# mysql -u root -padmin < ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'admin';