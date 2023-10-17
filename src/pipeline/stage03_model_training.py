from src import logger
from src.config.configuration import ConfigurationManager
from src.components.model_training import Training

STAGE_NAME = "Training"

class TrainingPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        training_config = config.get_train_model_config()
        training = Training(config=training_config)
        training.get_base_model()
        training.train_valid_generator()
        training.train()

if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>{STAGE_NAME} stage started")
        obj = TrainingPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} stage completed")
    except Exception as e:
        logger.exception(e)         