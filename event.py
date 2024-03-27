import sys
import logging
import argparse

def return_args(args):

    file = open("myfile.txt","w")
    L = ["This is dummy logging  \n","to check github workflow \n"]


    file.write("Hello There \n")
    file.writelines(L)
    file.close()
    
    return args
if __name__ == "__main__":
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s.%(msecs)03d %(levelname)s %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )  
    
    logging.info("scrip event or job event")
    parser = argparse.ArgumentParser()
    parser.add_argument("--params",help="provide key for maping pd service with entities",default=None)
    args = vars(parser.parse_args(sys.argv[1:]))
    return_args(args)

   
    logging.info("END")
