
import os 
import requests 
import logging


if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )  
    
    logging.info("testing just github workflow working one this is script one or job one")

    print({
        "total_count":30,
        "total_failure": 10,
        "total_sucess": 10,
    })
    with open("dummy.txt",'w') as f:
        f.write('{"total_count":30,"total_failure": 10,"total_sucess": 10,}')

   
    logging.info("END")



