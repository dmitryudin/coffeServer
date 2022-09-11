#!/bin/bash
cp ./coffe.service /lib/systemd/system/
systemctl daemon-reload
systemctl enable coffe.service