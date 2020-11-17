#!/bin/bash

. ./getdata.sh

echo "cpu_usage: `cpu_usage`"
echo "used_Disk: `disk_usage`"
echo "free_Disk: `disk_free`"
echo "used_mem: `mem_usage`"
echo "free_mem: `mem_free`"
