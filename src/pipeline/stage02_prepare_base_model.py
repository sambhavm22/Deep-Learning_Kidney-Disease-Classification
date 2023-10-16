from src import logger
from src.config.configuration import ConfigurationManager
from src.components.prepare_base_model import PrepareBaseModel


STAGE_NAME = 'Prepare Base Model'
class PrepareBaseModelTrainingPipeline:
    def __init__(self) -> None:
        pass

    def main(self):
        config = ConfigurationManager()
        prepare_base_model_config = config.get_base_model_config()
        prepare_base_model = PrepareBaseModel(config=prepare_base_model_config)
        prepare_base_model.get_base_model()
        prepare_base_model.updated_base_model()

if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>{STAGE_NAME} stage started")
        obj = PrepareBaseModelTrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} stage completed")
    except Exception as e:
        logger.exception(e)        

