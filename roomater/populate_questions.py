project_home="/Users/jackmoxon/Programming/Roomater/rommater/"

import sys, os
sys.path.append(project_home)
os.environ['DJANGO_SETTINGS_MODULE'] = 'settings'

from backend.models import *

questions = (
    "When eating at home do you prefer eating alone or in groups?",
    "Do you have any pets?",
    "Do you cook meat at home?",
    "Why are you looking for a new apartment?",
    "Do you often have a partner sleeping over? How many nights, on average?",
    "How many nights a week do you typically spend away from home?",
    "Do you watch TV? How much /what shows?",
    "Do you like to share food?",
    "What's your idea of a fun night out?",
    "Do you prefer a big clean every now and then, or do you prefer we do a bit of a clean every day?",
    "Do you like to cook? Would you want to share cooking duties or just cook for yourself?",
    "Are you a morning person or a night person?",
    "How many (non-sleeping) hours do you typically spend at home?",
    "What time do you usually get up/shower?",
)

jack = User.objects.get(username="jackmoxon")

question_list = Question.objects.all()
list = []
for q in question_list:
    list.append(q.text)

for question in questions:
    if question not in list:
        q = Question(questioner=jack, text=question, standard=True)
        q.save()
