# Create a simple program that would log all inputs from the terminal. Configs must show all additional data (time, date, level etc.)


import logging


logging.basicConfig(level= logging.DEBUG, format= "%(levelname)s | %(asctime)s|%(filename)s |%(lineno)d| %(message)s", datefmt= "%d/%b/%y %H:%M:%S" , filename= "paskaita.log" , filemode= "a")
#level = logging.DEBUG galima keisti i reikiama lygi iki CRITICAL.
#levelname = duoda info apie erroro leveli
#format = filename koks failo pavadinimas
#asctime = laikas
#datefmt = galima savo formata sukurti pagal lentele
#message = zinute kuria paraseme
#lineno = eilutes skaicius
#filename = sukuria faila kad saugotu visa info
#filemide = iraso i faila (w - write, a - append)


# logging.debug("This is debug message") # serenity level 10 It is used for diagnosing the problem. It gives a piece of detailed information about the problem
# logging.info("This is info message") # serenity level 20 It gives the confirmation message of the successful execution of the program
# logging.warning("This is warning message ive typed") # The message is for when an unexpected situation occurs. serenity level 30
# logging.error("This is error message ive typed") # It is due to a more serious problem than a warning. It can be due to some inbuilt error Like syntax or logical error. serenity level 40
# logging.critical("This is critical message ive typed") #It occurs when the program execution stops and it can not run itself anymore.  serenity level 50
# #
logging.info(f"Prasideda programa")
def sum(a, b):
    logging.warning(f"Atliekamas veiksas {a} + {b}")
    return a + b
a = 2
b = 3
sum(1, 2)
logging.debug(f" a kitamasis {a}")
logging.debug(f" b kitamasis {b}")

logging.info(f"Baigiasi programa")

v = 10
z = 0
try:
    c = v / z
except ZeroDivisionError as e:
    logging.error(f"Dalyba is nulio: Python aprasymas: {e}", exc_info= True)
    #jei norim viso erroro galim rasyti exc_info = True, galime ir be e