import pytest
from flask import Flask, render_template_string
from flask_testing import TestCase
from app_api import app
from unittest.mock import patch, Mock

class TestApp(TestCase):
    
    def create_app(self):
        app.config['TESTING'] = True
        return app


    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)


    def test_home_template(self):
        response = self.client.get('/')
        self.assert_template_used('index.html')
        
        
    def test_submit_template(self):
        response = self.client.get('/submit/')
        self.assert_template_used('submit.html')
        assert response.status_code == 200


    def test_submit_route_post(self):
        response = self.client.post('/submit/', data={'input_text': './static/assets/img.jpg'})
        self.assertEqual(response.status_code, 200)


    def test_submit_route_get(self):
        img_url = "https://github.com/heidisbk/MuspellheimGnistor/blob/dev_traitement_dataset/data_constellations/data_collection/leo/leo0.png?raw=true" 
        response = self.client.get(f"/http://127.0.0.1:8000/predict?img_url={img_url}")
        assert response.status_code == 200
        data = response.json()
        assert "Prediction" in data
        assert "Probabilité" in data