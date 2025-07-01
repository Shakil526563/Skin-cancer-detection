from django.shortcuts import render
from django.core.files.storage import FileSystemStorage
import os
import numpy as np
import joblib
from tensorflow.keras.preprocessing import image



# Load the XGBoost model
model = joblib.load('./models/xgboost_model.joblib')

def index(request):
    return render(request, 'index.html')

def predictImage(request):
    fileObj = request.FILES['filePath']
    fs = FileSystemStorage()
    filePathName = fs.save(fileObj.name, fileObj)
    filePathName = fs.url(filePathName)
    testimage = '.' + filePathName

    # Load and preprocess the image
    img = image.load_img(testimage, target_size=(150, 150))
    x = image.img_to_array(img)
    x = x.flatten()[:100]  # Flatten the image to 1D array with 100 features
    x /= 255.0

    # Ensure the input shape matches the expected shape used for training
    if x.shape[0] != 100:
        raise ValueError(f"Feature shape mismatch, expected: 100, got: {x.shape[0]}")

    # Make a prediction using the loaded model
    final_prediction = model.predict(x.reshape(1, -1))

    context = {
        'filePathName': filePathName,
        'predictedScore': final_prediction[0],
    }
    return render(request, 'index.html', context)

def viewDataBase(request):
    listOfImages = os.listdir('./media/')
    listOfImagesPath = ['./media/' + i for i in listOfImages]
    context = {'listOfImagesPath': listOfImagesPath}
    return render(request, 'viewDB.html', context)
