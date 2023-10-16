from src import logger
from src.pipeline.stage01_data_ingestion import DataIngestionTrainingPipeline

STAGE_NAME = "Data Ingestion"

if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>{STAGE_NAME} stage started")
        obj = DataIngestionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} stage completed")
    except Exception as e:
        logger.exception(e) 