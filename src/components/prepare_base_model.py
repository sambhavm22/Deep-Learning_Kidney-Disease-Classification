from entity.config_entity import PrepareBaseModelConfig
from src import logger
import tensorflow as tf
from src.utils.common import save_model



class PrepareBaseModel:
    def __init__(self, config: PrepareBaseModelConfig) -> None:
        self.config = config

    def get_base_model(self):
        self.base_model =  tf.keras.applications.vgg16.VGG16(
            input_shape=self.config.params_image_size,
            weights=self.config.params_weights,
            include_top=self.config.params_include_top)
        
        save_model(path=self.config.base_model_path, model=self.base_model)

    @staticmethod
    def prepare_full_model(model, classes, freeze_all, freeze_till, learning_rate):

        if freeze_all:
            for layer in model.layers:
                model.trainable = False

        elif (freeze_till is not None) and (freeze_till>0):
            for layer in model.layers[:-freeze_till]:
                model.trainable = False  

        flatten_in = tf.keras.layers.Flatten()(model.output)
        prediction = tf.keras.layers.Dense(units=classes, activation='softmax')(flatten_in)

        full_model = tf.keras.models.Model(
            inputs = model.input,
            outputs = prediction
        )

        full_model.compile(optimizer=tf.keras.optimizers.SGD(learning_rate),
                        loss = tf.keras.losses.SparseCategoricalCrossentropy(),
                        metrics=['accuracy'])
        
        full_model.summary()
        
        return full_model
    
    def updated_base_model(self)->tf.keras.Model:
        self.full_model = self.prepare_full_model(
            model = self.base_model,
            classes = self.config.params_classes,
            freeze_all = True,
            freeze_till = None,
            learning_rate = self.config.params_learning_rate
        ) 
        save_model(path=self.config.updated_base_model_path, model=self.full_model)


        
        