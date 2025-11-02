"""
Workout Generator - Web Application
A personalized fitness plan creator with Flask
"""

from flask import Flask, render_template, request, jsonify
import random
import os

app = Flask(__name__)
app.secret_key = os.environ.get('SESSION_SECRET', 'workout-generator-secret-key')

class WorkoutGenerator:
    def __init__(self):
        self.exercises = {
            'warmup': ['Jumping Jacks', 'Arm Circles', 'Leg Swings', 'High Knees', 'Butt Kicks'],
            'cardio_beginner': ['Brisk Walking', 'Light Jogging', 'Dancing', 'Cycling (easy pace)'],
            'cardio_intermediate': ['Running', 'Jump Rope', 'Burpees', 'Mountain Climbers', 'Boxing'],
            'cardio_advanced': ['Sprint Intervals', 'HIIT Sprints', 'Plyometric Jumps', 'Battle Ropes'],
            'strength_beginner': ['Wall Push-ups', 'Bodyweight Squats', 'Lunges', 'Plank (knees down)'],
            'strength_intermediate': ['Push-ups', 'Squats', 'Lunges', 'Plank', 'Crunches', 'Dumbbell Rows'],
            'strength_advanced': ['Weighted Squats', 'Pull-ups', 'Pistol Squats', 'Burpees', 'Deadlifts'],
            'flexibility': ['Hamstring Stretch', 'Quad Stretch', 'Shoulder Stretch', 'Cat-Cow Pose', 'Child\'s Pose'],
            'cooldown': ['Walking', 'Deep Breathing', 'Full Body Stretch', 'Foam Rolling']
        }
    
    def calculate_bmi(self, height_cm, weight_kg):
        height_m = height_cm / 100
        bmi = weight_kg / (height_m ** 2)
        
        if bmi < 18.5:
            category = "Underweight"
        elif 18.5 <= bmi < 25:
            category = "Normal weight"
        elif 25 <= bmi < 30:
            category = "Overweight"
        else:
            category = "Obese"
        
        return round(bmi, 2), category
    
    def generate_plan(self, name, age_range, gender, height, weight, fitness_level):
        bmi, category = self.calculate_bmi(height, weight)
        fitness_lower = fitness_level.lower()
        
        motivational_messages = [
            "💪 You're taking the first step to a healthier you!",
            "🌟 Great things never come from comfort zones!",
            "🔥 The only bad workout is the one you didn't do!",
            "✨ Your body can do it, it's your mind you need to convince!"
        ]
        
        warmup = random.sample(self.exercises['warmup'], 3)
        cardio = random.sample(self.exercises[f'cardio_{fitness_lower}'], 
                              min(3, len(self.exercises[f'cardio_{fitness_lower}'])))
        strength = random.sample(self.exercises[f'strength_{fitness_lower}'], 
                                min(4, len(self.exercises[f'strength_{fitness_lower}'])))
        flexibility = random.sample(self.exercises['flexibility'], 3)
        cooldown = random.sample(self.exercises['cooldown'], 2)
        
        duration_map = {
            'beginner': '5-7 minutes',
            'intermediate': '7-10 minutes',
            'advanced': '10-15 minutes'
        }
        
        reps_map = {
            'beginner': '10-12 reps',
            'intermediate': '12-15 reps',
            'advanced': '15-20 reps'
        }
        
        plan = {
            'profile': {
                'name': name,
                'age_range': age_range,
                'gender': gender,
                'bmi': bmi,
                'category': category,
                'fitness_level': fitness_level
            },
            'motivation': random.choice(motivational_messages),
            'warmup': warmup,
            'cardio': {'exercises': cardio, 'duration': duration_map[fitness_lower]},
            'strength': {'exercises': strength, 'reps': reps_map[fitness_lower]},
            'flexibility': flexibility,
            'cooldown': cooldown
        }
        
        return plan

generator = WorkoutGenerator()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    try:
        data = request.json
        name = data.get('name', '').strip()
        age_range = data.get('age_range')
        gender = data.get('gender')
        height = float(data.get('height'))
        weight = float(data.get('weight'))
        fitness_level = data.get('fitness_level')
        
        if not name or height <= 0 or weight <= 0:
            return jsonify({'error': 'Please enter valid data!'}), 400
        
        plan = generator.generate_plan(name, age_range, gender, height, weight, fitness_level)
        return jsonify(plan)
    
    except (ValueError, TypeError) as e:
        return jsonify({'error': 'Invalid input. Please check your data.'}), 400

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
