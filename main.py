from src import logger
from src.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline
from src.pipeline.stage02_prepare_base_model import PrepareBaseModelTrainingPipeline
from src.pipeline.stage03_model_training import TrainingPipeline

STAGE_NAME = "Data Ingestion stage"
try:
    logger.info(f">>>>>> {STAGE_NAME} started <<<<<<") 
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


STAGE_NAME = "Prepare base model"
try: 
    logger.info(f"*******************")
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    prepare_base_model = PrepareBaseModelTrainingPipeline()
    prepare_base_model.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Training"

if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>{STAGE_NAME} stage started")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} stage completed")
    except Exception as e:
        logger.exception(e) 

