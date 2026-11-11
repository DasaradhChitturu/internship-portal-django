import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

logging.debug("Checking application details")
logging.info("Student application submitted successfully")
logging.warning("Application has incomplete optional information")
logging.error("Application submission failed")
logging.critical("Database connection unavailable")



logging.basicConfig(level=logging.INFO)

try:
    result = 10 / 0

except ZeroDivisionError:
    logging.exception("Calculation failed")