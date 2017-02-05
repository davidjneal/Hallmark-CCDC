#!/bin/bash

chattr -i /etc/sudoers

chattr -i /etc/security/*

chattr -i /etc/passwd

chattr -i /etc/shadow

chattr -i /etc/hosts

chattr -i /etc/hosts.allow

chattr -i /etc/hosts.deny

chattr -i /var/spool/cron/*
