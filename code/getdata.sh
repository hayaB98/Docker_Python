#!/usr/bin/env sh

cpu_usage() {
     top -bn2 -p1 | grep 'Cpu' | tail -1 | awk '{ print $8 }'
}

mem_usage() {
    free -b | grep 'Mem' | awk '{ print $3 }'
}

mem_free() {
    free -b | grep 'Mem' | awk '{ print $7 }'
}

disk_usage() {
     df -B1 | grep 'centos.*root' | awk '{ print $3 }'
}

disk_free() {
     df -B1 | grep 'centos.*root' | awk '{ print $4 }'
}
