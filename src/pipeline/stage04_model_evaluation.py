from src import logger
from src.config.configuration import ConfigurationManager
from src.components.model_evaluation_with_mlflow import Evaluation

STAGE_NAME = "Training"

class EvaluationPipeline:
    def __init__(self) -> None:
        pass
    def main(self):
        config = ConfigurationManager()
        evaluation_config = config.get_model_evaluation_config()
        evaluation = Evaluation(config=evaluation_config)
        evaluation.evaluation()
        evaluation.save_score()
        evaluation.log_into_mlflow()

if __name__ == "__main__":
    try: 
        logger.info(f">>>>>>{STAGE_NAME} stage started")
        obj = EvaluationPipeline()
        obj.main()
        logger.info(f">>>>>>{STAGE_NAME} stage completed")
    except Exception as e:
        logger.exception(e)         