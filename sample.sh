#!/bin/bash

logit() {
  severity=${1:-INFO}
  msg=$2
  >&2 echo "$severity $(date -u +'%Y-%m-%d-%H:%M:%S') $msg"
}

call_l9iac(){
 
    stats="total_actions=25 failed_actions=5 reconcile=3 total_create_update_delete=4 create=10 update=5 delete=6"    
    logit "INFO" "$stats"
}


call_l9iac 

