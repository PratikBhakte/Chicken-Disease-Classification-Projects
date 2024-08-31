from cnnClassifier import logger
from cnnClassifier.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipleline
from cnnClassifier.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>> stage : {STAGE_NAME} started <<<<\n")
    data_ingestion = DataIngestionTrainingPipleline()
    data_ingestion.main()
    logger.info(f">>>> stage : {STAGE_NAME} completed <<<<\n")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Prepare base model"

try:
    logger.info(f">>>> stage : {STAGE_NAME} started <<<<\n")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>> stage : {STAGE_NAME} completed <<<<\n")
except Exception as e:
    logger.exception(e)
    raise e