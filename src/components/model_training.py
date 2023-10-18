from entity.config_entity import TrainingConfig
import tensorflow as tf
import os, time
from pathlib import Path
from src.utils.common import save_model

class Training:
    def __init__(self, config: TrainingConfig):
        self.config = config

    def get_base_model(self):
        self.model = tf.keras.models.load_model(self.config.updated_base_model_path)   

    def train_valid_generator(self):

        """
        This method is responsible for setting up data generators for training and validation. 
        These generators are commonly used in deep learning workflows for loading and augmenting
        data during the training process.
        """
        
        data_generator_kwargs = dict(
            rescale = 1./255,
            validation_split = 0.20
        )    

        """
        This creates a dictionary datagenerator_kwargs containing configuration parameters for the 
        data generator. rescale is set to normalize pixel values to the range [0, 1], and 
        validation_split specifies that 20% of the data will be used for validation.
        """

        dataflow_kwargs = dict(
            target_size = self.config.params_image_size[:-1],
            batch_size = self.config.params_batch_size,
            interpolation = 'bilinear'
        )

        """
        dataflow_kwargs is created to store parameters related to the data flow. 
        """

        valid_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
            **data_generator_kwargs
        )

        self.valid_generator = valid_data_generator.flow_from_directory(
            directory = self.config.training_data,
            subset = 'validation',
            shuffle = False,
            **dataflow_kwargs
        )

        """
        The flow_from_directory method is used to create a generator for validation data.
        It reads images from the specified directory (self.config.training_data) for the
        "validation" subset, with no shuffling. Configuration parameters are passed using **dataflow_kwargs
        """

        if self.config.params_is_augmentation:
            train_data_generator = tf.keras.preprocessing.image.ImageDataGenerator(
                rotation_range = 40,
                shear_range = 0.2,
                width_shift_range = 0.2,
                height_shift_range = 0.2,
                zoom_range = 0.2,
                horizontal_flip = True,
                **data_generator_kwargs
            )

        else:
            train_data_generator = valid_data_generator

        """
        Depending on the value of params_is_augmentation in the configuration (self.config), 
        either an augmented training data generator is created with additional augmentation 
        parameters or it's set to the same generator as the validation generator (valid_datagenerator).
        """    

        self.train_generator = train_data_generator.flow_from_directory(
            directory = self.config.training_data,
            subset = 'training',
            shuffle = True,
            **dataflow_kwargs
        )    

    def train(self):
        self.steps_per_epoch = self.train_generator.samples // self.train_generator.batch_size
        self.validation_steps = self.valid_generator.samples // self.valid_generator.batch_size

        self.model.fit(
            self.train_generator,
            epochs = self.config.params_epochs,
            steps_per_epoch=self.steps_per_epoch,
            validation_steps=self.validation_steps,
            validation_data=self.valid_generator
            )

        save_model(path=self.config.trained_model_path,
                model = self.model)
            
