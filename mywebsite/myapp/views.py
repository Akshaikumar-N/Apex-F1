import os
from google import genai
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .models import Driver, Team, Track, Rating, Prediction
from .forms import RatingForm, PredictionForm

# Configure Gemini
client = genai.Client(api_key="AIzaSyBH4Zeou49SLMivx8qebvsikVugAcMeFHM")

def home(request):
    drivers = Driver.objects.all().order_by('-points')
    teams = Team.objects.all()
    tracks = Track.objects.all()
    
    context = {
        'drivers': drivers,
        'teams': teams,
        'tracks': tracks,
    }
    return render(request, 'myapp/index.html', context)

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect('home')
        messages.error(request, "Unsuccessful registration. Invalid information.")
    else:
        form = UserCreationForm()
    return render(request, 'myapp/register.html', {"form":form})

@login_required
def rate_driver(request, driver_id):
    driver = get_object_or_404(Driver, id=driver_id)
    # Check if user already rated
    try:
        rating = Rating.objects.get(user=request.user, driver=driver)
        form = RatingForm(instance=rating)
    except Rating.DoesNotExist:
        rating = None
        form = RatingForm()

    if request.method == 'POST':
        form = RatingForm(request.POST, instance=rating)
        if form.is_valid():
            new_rating = form.save(commit=False)
            new_rating.user = request.user
            new_rating.driver = driver
            new_rating.save()
            messages.success(request, f"Rating for {driver.name} saved!")
            return redirect('home')

    return render(request, 'myapp/rate.html', {'form': form, 'driver': driver})

@login_required
def predict_winner(request, track_id):
    track = get_object_or_404(Track, id=track_id)
    try:
        prediction = Prediction.objects.get(user=request.user, track=track)
        form = PredictionForm(instance=prediction)
    except Prediction.DoesNotExist:
        prediction = None
        form = PredictionForm()

    if request.method == 'POST':
        form = PredictionForm(request.POST, instance=prediction)
        if form.is_valid():
            new_prediction = form.save(commit=False)
            new_prediction.user = request.user
            new_prediction.track = track
            new_prediction.save()
            messages.success(request, f"Prediction for {track.name} saved!")
            return redirect('home')

    return render(request, 'myapp/predict.html', {'form': form, 'track': track})

def quiz(request):
    import json
    quiz_data = None
    error_message = None

    if request.method == 'POST':
        topic = request.POST.get('topic')
        if topic:
            prompt = (
                f"Generate a short, fun 3-question trivia quiz about Formula 1 focusing on {topic}. "
                "Output ONLY a valid JSON array with 3 objects. "
                "Each object must have exactly these keys: 'question' (string), 'options' (array of 4 strings), and 'answer' (string, must exactly match one of the options). "
                "Do NOT include any markdown formatting like ```json or ```, just the raw JSON."
            )
            try:
                response = client.models.generate_content(
                    model='gemini-2.5-flash',
                    contents=prompt
                )
                raw_text = response.text.strip()
                # Clean up potential markdown formatting just in case
                if raw_text.startswith('```json'):
                    raw_text = raw_text[7:]
                elif raw_text.startswith('```'):
                    raw_text = raw_text[3:]
                if raw_text.endswith('```'):
                    raw_text = raw_text[:-3]
                raw_text = raw_text.strip()
                
                quiz_data = json.loads(raw_text)
            except Exception as e:
                error_message = "Failed to generate quiz. Please try again with another topic."
            
    return render(request, 'myapp/quiz.html', {'quiz_data': quiz_data, 'error_message': error_message})
