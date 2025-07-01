# Skin Cancer Detection - JavaScript-Free Django Web Application


https://github.com/user-attachments/assets/cb563445-9e3e-4080-b6ed-14a66bf0df54




## Overview
Our project utilizes deep CNNs to extract features from skin cancer images on Kaggle, enhancing classification accuracy. These features are then employed by traditional ML algorithms for effective skin cancer diagnosis. The entire system is deployed seamlessly in Django, providing users with a user-friendly web interface for real-time predictions and early detection.

This Django-based web application has been designed to work entirely with HTML and CSS, removing all JavaScript dependencies while maintaining full functionality and providing a modern, responsive user interface.

## Features
- **Deep Learning Integration**: Utilizes deep CNNs to extract features from skin cancer images, enhancing classification accuracy
- **Hybrid ML Approach**: Combines CNN feature extraction with traditional ML algorithms (XGBoost) for effective diagnosis
- **JavaScript-Free Design**: Pure HTML/CSS implementation with no JavaScript dependencies
- **AI-Powered Detection**: Uses XGBoost machine learning model trained on CNN-extracted features for skin lesion classification
- **Real-Time Predictions**: Upload images and get instant skin cancer classification results with early detection capabilities
- **Modern UI**: Clean, responsive design with gradient backgrounds and smooth transitions
- **Image Upload**: Drag-and-drop file upload interface with seamless Django integration
- **Results Display**: Clear visualization of prediction results (Benign/Malignant)
- **Image Gallery**: View previously analyzed images with database management
- **Responsive Design**: Works seamlessly on desktop, tablet, and mobile devices
- **Accessibility**: Proper focus states and keyboard navigation support

## Technical Stack
- **Backend**: Django (Python Web Framework)
- **Frontend**: HTML5, CSS3 (No JavaScript)
- **Machine Learning**: 
  - Deep CNNs for feature extraction from Kaggle skin cancer datasets
  - XGBoost for traditional ML classification
  - TensorFlow/Keras for CNN implementation
  - scikit-learn for additional ML utilities
- **Image Processing**: Pillow (PIL) for image handling and preprocessing
- **Styling**: Custom CSS with Bootstrap (CSS only)
- **Icons**: Font Awesome
- **Database**: SQLite (Django default)

## Project Structure
```
├── manage.py
├── db.sqlite3
├── firstApp/                 # Django app
│   ├── views.py             # Main application logic
│   ├── models.py
│   └── ...
├── imageclassification/      # Django project settings
├── template/                 # HTML templates
│   ├── headerPage.html      # Base template with navigation
│   ├── index.html           # Main detection page
│   └── viewDB.html          # Image gallery
├── static/
│   ├── css/
│   │   ├── bootstrap.min.css
│   │   ├── font-awesome.min.css
│   │   └── custom-styles.css # Custom CSS styles
│   └── js/                  # (Removed - not used)
├── media/                   # Uploaded images
└── models/                  # ML model files
    └── xgboost_model.joblib
```

## Installation & Setup

### Prerequisites
- Python 3.8+
- Django 4.0+
- Required Python packages (see requirements.txt)

### Installation Steps
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd Django-Skin-Cancer-Detection-Project-main
   ```

2. Create virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
   
   Required packages:
   - Django>=4.0.0
   - tensorflow>=2.8.0
   - scikit-learn>=1.0.0
   - joblib>=1.1.0
   - Pillow>=9.0.0
   - numpy>=1.21.0
   - xgboost>=1.6.0

4. Run migrations:
   ```bash
   python manage.py migrate
   ```

5. Start the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000`

## Usage
1. **Upload Image**: Click on the upload area or drag and drop a skin lesion image
2. **CNN Feature Extraction**: The system automatically processes the image using deep CNNs to extract relevant features
3. **ML Classification**: XGBoost model analyzes the CNN-extracted features for accurate diagnosis
4. **View Results**: The system displays whether the lesion is Benign (0) or Malignant (1) with enhanced accuracy
5. **Early Detection**: Real-time predictions enable early detection and timely medical intervention
6. **Gallery**: Visit the gallery page to view previously analyzed images and track analysis history

## Model Information
The application uses a hybrid approach combining deep learning and traditional machine learning:

**Feature Extraction Process:**
- Deep CNNs extract features from skin cancer images sourced from Kaggle datasets
- Images are preprocessed to 150x150 pixels for optimal CNN feature extraction
- CNN features are flattened to a 100-dimensional feature vector

**Classification Process:**
- XGBoost model trained on CNN-extracted features for enhanced classification accuracy
- Traditional ML algorithms provide robust and interpretable predictions
- Model classifies skin lesions as:
  - **0 (Benign)**: Non-cancerous lesion
  - **1 (Malignant)**: Potentially cancerous lesion

**Pipeline:**
1. Image Upload → 2. CNN Feature Extraction → 3. Feature Vector Creation → 4. XGBoost Classification → 5. Prediction Result

## Design Philosophy
This version prioritizes:
- **Performance**: No JavaScript means faster loading and better performance
- **Accessibility**: Pure HTML/CSS ensures better screen reader compatibility
- **Simplicity**: Easier maintenance without complex JavaScript dependencies
- **Security**: Reduced attack surface by eliminating client-side scripts
- **Compatibility**: Works on all browsers without JavaScript support

## CSS Features
- Modern gradient backgrounds
- Smooth CSS transitions and hover effects
- Responsive grid layouts
- Custom file upload styling
- Pure CSS animations
- Mobile-first responsive design

## Important Disclaimer
This application is for educational and screening purposes only. The AI predictions should not replace professional medical advice. Always consult with a qualified dermatologist for proper diagnosis and treatment of skin conditions.

## Browser Support
- Chrome/Chromium 60+
- Firefox 55+
- Safari 12+
- Edge 79+
- Works without JavaScript enabled

## Contributing
1. Fork the repository
2. Create a feature branch
3. Make your changes (maintaining the no-JavaScript principle)
4. Test thoroughly
5. Submit a pull request

## License
This project is open source and available under the [MIT License](LICENSE).

## Contact
For questions or support, please open an issue in the GitHub repository.

---
**Note**: This version has been specifically designed to work without JavaScript while maintaining all functionality and providing an enhanced user experience through modern CSS techniques.

# Django-Skin-Cancer-Detection
