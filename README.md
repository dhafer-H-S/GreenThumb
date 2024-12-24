# GreenThumb

## Authors:
**Dhafer Hamza Sfaxi**
- Leads development of machine learning models (plant health verification, recommendation systems) and backend integration.
- Assists in image preprocessing, data validation, and performance evaluation of models.

## Introduction:
GreenThumb leverages machine learning to:
- Verify the health status of plants through image processing.
- Recommend plants suitable for specific environmental conditions.
- Provide detailed care instructions through AI-generated recommendations.

## Description:
The machine learning system offers the following functionalities:
- **Plant Health Verification:** Users upload images of plants; the system evaluates health using image classification.
- **Plant Recommendations:** Users input preferences and environmental factors to receive tailored plant suggestions.
- **AI-Generated Responses:** A language model generates explanations, tips, and care guidelines for users.

## Data:
### Required Data Sources:
#### Plant Health Data:
- Machine learning in agriculture 🍇🎾
- ML Projects in Agriculture Domain Area | Kaggle
- Plant Disease Detection using Keras
- Top Agriculture Datasets on Kaggle 🎾 [2023] | Kaggle
- CNN - Disease Detection
- Plant Disease Analytics
- PlantVillage Dataset
- AlexNet1_Plant_Disease_Classification

#### Key Datasets:
1. **PlantVillage Dataset**
   - Description: Over 50,000 images of healthy and diseased plants, categorized by disease type and plant species.
2. **Plants Disease Detection Dataset**
   - Description: Contains multiple labeled plant health images for classification tasks.
3. **GeoPlant Dataset**
   - Description: Provides spatial plant species data linked to environmental conditions.
4. **Earth Surface Temperature Data**
   - Description: Offers historical temperature data crucial for climate pattern analysis.
5. **Environment Climate Dataset**
   - Description: Contains rainfall, temperature, and humidity data for various regions.
6. **Soil Moisture and Type Dataset**
   - Description: Detailed information about soil types and their suitability for different plants.

## Machine Learning Algorithms:
### Plant Health Verification:
- **OpenCV:** For preprocessing (e.g., resizing, augmentation).
- **Convolutional Neural Networks (CNNs):** Image classification for plant health.

### Recommendation System:
- **Random Forest** or **K-Nearest Neighbors (KNN):** Multiclass classification to recommend plants based on environmental factors.
- **Collaborative Filtering:** Personalize recommendations based on user inputs and preferences.

### AI-Generated Recommendations:
- **Language Models:** Use GPT-based APIs or open-source tools like Hugging Face Transformers to generate user-friendly responses with planting tips and explanations.

## Ethics:
- **Transparency:** Recommendations and diagnoses will be clearly explained.
- **Fairness:** Models will be trained on diverse datasets to ensure equitable suggestions across regions.
- **Privacy:** User-uploaded images and data will be anonymized and securely stored.

## Platform:
- **Devices:** Android and iOS apps using React Native or Flutter.
- **Backend:** Deployed with Django/Flask on AWS or Azure.

## Schedule:
**Week 1:**
- Collect datasets from Kaggle.
- Preprocess images using OpenCV (resize, augment).
- Normalize environmental data and encode categorical variables.

**Week 2:**
- Train CNNs for plant health verification.
- Train Random Forest or KNN for plant recommendations.
- Validate models using metrics (accuracy, F1-score).

**Week 3:**
- Deploy machine learning models via RESTful APIs.
- Integrate LLMs to generate recommendation messages.

**Week 4:**
- Conduct end-to-end testing of health verification and recommendation systems.
- Optimize model performance based on feedback.

## Mentor/Reviewer:
- **Ms. Malek Mrabti** and **Mr. Khaled Haguiga**: Experts in machine learning and computer vision to review model performance and ensure ethical considerations.
