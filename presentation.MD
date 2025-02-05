# GreenThumb Project

## Short Description of the Project and Team
GreenThumb is an innovative project aimed at promoting sustainable gardening practices through the use of technology. Our team consists of passionate developers, designers, and environmental enthusiasts dedicated to making gardening more accessible and eco-friendly.

## Demo
You can view a live demo of our project [here](http://greenthumb-demo.com) or watch a recorded demo on [YouTube](https://youtube.com/greenthumb-demo).

## Architecture
The architecture of GreenThumb is designed to be scalable and efficient. It includes:
- **Frontend**: Built with React.js for a responsive and interactive user interface.
- **Backend**: Powered by Node.js and Express.js to handle API requests and business logic.
- **Database**: MongoDB is used for storing user data and gardening tips.
- **Hosting**: Deployed on AWS for reliable and scalable hosting.

## Technologies and Third-Party Services Used
- **React.js**: For building the user interface.
- **Node.js**: For server-side scripting.
- **Express.js**: For creating RESTful APIs.
- **MongoDB**: For database management.
- **AWS**: For cloud hosting and deployment.
- **Google Maps API**: For location-based gardening tips.
- **Twilio**: For sending SMS notifications to users.

## Report of Developments

### Successes
- Successfully implemented a user-friendly interface.
- Integrated Google Maps API for location-based services.
- Achieved seamless communication between frontend and backend.

### Failures
- Initial issues with database schema design.
- Encountered challenges with real-time data updates.

### Improvements
- Optimize database queries for better performance.
- Enhance user authentication and security measures.

### Learnings
- Gained experience in full-stack development.
- Improved skills in API integration and cloud deployment.

### Next Steps
- Implement advanced features like AI-based gardening tips.
- Expand the user base and gather more feedback for improvements.

## Ethical Implications
- Ensuring user data privacy and security.
- Promoting sustainable and eco-friendly gardening practices.

## Summary/Conclusion
GreenThumb is a project that leverages technology to make gardening more accessible and sustainable. Through continuous development and user feedback, we aim to create a platform that benefits both users and the environment.
## Machine Learning Models

### Models Used
- **Plant Disease Detection Model**: A convolutional neural network (CNN) model trained to identify common plant diseases from leaf images.
- **Gardening Tips Recommendation Model**: A collaborative filtering model that suggests personalized gardening tips based on user preferences and behavior.

### CSV Files Used
- **Plant Disease Dataset**: Contains labeled images of healthy and diseased plant leaves used to train the disease detection model.
- **User Preferences Dataset**: Includes user interactions and preferences data used to train the recommendation model.

## Technologies and Architecture for Machine Learning

### Technologies Used
- **TensorFlow**: For building and training the machine learning models.
- **Keras**: A high-level neural networks API used with TensorFlow.
- **Pandas**: For data manipulation and analysis.
- **NumPy**: For numerical computations.

### Architecture
- **Data Preprocessing**: Raw data from CSV files is cleaned and preprocessed using Pandas and NumPy.
- **Model Training**: Machine learning models are built and trained using TensorFlow and Keras.
- **Model Deployment**: Trained models are deployed as microservices using Flask, allowing integration with the main application.
- **Inference**: The deployed models provide real-time predictions and recommendations to users through API endpoints.

## Summary/Conclusion
GreenThumb is a project that leverages technology, including machine learning, to make gardening more accessible and sustainable. Through continuous development and user feedback, we aim to create a platform that benefits both users and the environment.