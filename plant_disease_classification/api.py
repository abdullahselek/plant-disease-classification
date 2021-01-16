#!/usr/bin/env python

from typing import Optional

try:
    import plant_disease_classification_models
except Exception:
    print(
        "Please install `plant-disease-classification-models` with this command before using `plant-disease-classification`:\n"
    )
    print("pip install plant-disease-classification-models\n")
    print(
        "pip install git+https://github.com/abdullahselek/plant-disease-classification-models"
    )
    quit()

from .plant_disease_classifier import PlantDiseaseClassifier


model = plant_disease_classification_models.model_one()
plant_disease_classifier = PlantDiseaseClassifier(model_path=model)


def classify(image_path: Optional[str] = None, image_data: Optional[bytes] = None):
    if image_path:
        return plant_disease_classifier.classify(image_path=image_path)
    elif image_data:
        return plant_disease_classifier.classify(image_data=image_data)
    else:
        raise Exception("Please provide image path or data of your image!")
