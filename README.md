# Classification of Cyber ​​Threats: NLP approach on MITRE ATT&CK

Our end-of-year project aims to develop a methodology for classifying cyber threats using the NLP (Natural Language Processing) approach of the MITRE ATT&CK framework. By combining machine learning algorithms and transformers, the goal is to create a system capable of efficiently analyzing and categorizing various cyber threats. This approach will enable a better understanding of potential attacks, as well as a faster and more precise identification of security measures to implement.

### Project's architecture
![Alt text](img/1.png)

### NLP Pipeline
![Alt text](img/2.PNG)

## Directory Structure

### Data
- **Processed datasets**: Contains processed data ready for modeling.
- **Raw Data**: Contains raw data files.
- **Final.csv**: The final dataset used for training and evaluation.

### Deployment
- **Model**: Directory containing the model files.
- **static/styles**: Directory for static stylesheets.
- **templates**: Directory for HTML templates.
- **Dockerfile**: Dockerfile for building the Docker image.
- **constante.py**: File containing constant definitions.
- **deploy.py**: Deployment script.
- **docker-compose.yml**: Docker Compose configuration file.
- **heroku.yml**: Heroku deployment configuration.
- **requirements.txt**: List of dependencies.
- **wsgi.py**: WSGI entry point.

### Models
- **ML Models**: Directory containing the trained machine learning model and its vectorizer.

### Notebooks
- **1. scrapping**: Contains the file used for data scrapping
- **2. data preparation.ipynb**: Jupyter notebook for data preparation steps.
- **3. NLP processing and modeling.ipynb**: Jupyter notebook for NLP processing and model training.
- **4. SecBERT.ipynb**: Jupyter notebook for experimenting with the SecBERT model.
- **5. SVC Predictions.ipynb**: Jupyter notebook for generating predictions using a Support Vector Classifier (SVC) model.
- **requirements.txt**: List of dependencies.

# Team Members
- [Nour Amellouk](https://github.com/Amellouk-Nour)
- [Zakaria Baou](https://github.com/zacharyb02)
