from src.CreditCardDefaulter.components.data_ingestion import DataIngestion


import os
import sys
from src.CreditCardDefaulter.logger import logging
from src.CreditCardDefaulter.exception import customexception
import pandas as pd

obj=DataIngestion()

obj.initiate_data_ingestion()
