This repository contains code for fine-tuning an image diffusion model on Replicate. The project demonstrates how to leverage Replicate's API to train and run predictions with a custom-trained Stable Diffusion model.

# Overview

The repository provides a scaffolded Node.js project for running AI models with Replicate's API. It includes a script for fine-tuning the model using a set of images and a sample application that generates images based on text prompts.

## Project Structure

-   `fine-tuning/fine-tune.py`: Script for fine-tuning the model.
-   `my-replicate-app/`: Node.js application for running predictions.
-   `data/`: Directory containing training images

## Installation

#### Clone the repository:
```
git clone https://github.com/sundai-club/fine_tuned_sd2_art_hack.git
cd fine_tuned_sd2_art_hack
```

#### Set up your environment variables:
```
export REPLICATE_API_TOKEN=your_replicate_api_token
```

## Usage

### Fine-Tuning the Model

The script for fine-tuning the model is located in `fine-tuning/fine-tune.py`. The script uses Replicate's API to train a Stable Diffusion model with a custom dataset.

To fine-tune the model, run the following command:
```
python fine-tuning/fine-tune.py
```

The script uses the following parameters:

-   `version`: The model version identifier on Replicate.
-   `input_images`: URL to a zip file containing the training images.
-   `destination`: The destination model identifier (this should be your own Model created on [replicate.com](https://replicate.com/))


### Running Predictions

The sample application to run predictions is located in `my-replicate-app/index.js`. The script uses the fine-tuned model to generate images based on text prompts.

To run the application:
```
cd my-replicate-app
npm install
npm start
```

