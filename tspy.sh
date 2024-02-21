#!/bin/bash


for interface in dashboard/dto/*.ts;do
  ts2py "$interface"
done
mv dashboard/dto/*.py surveillance/dto/