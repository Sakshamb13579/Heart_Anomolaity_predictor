from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .forms import *
from .models import *

import configparser

# Create your views here.
def signup(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)
        if form.is_valid():
            form.save()

            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username = username, password = password)

            login(request, user)
            return redirect('dashboard')
        else:
            return render(request, 'signup.html', {'form': form})
    else:
        form = RegisterUserForm()
        return render(request, 'signup.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password = password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else: 
            return render(request, 'login.html', {'message': 'Incorrect username or password. Please try again.'})
    else:
        return render(request, 'login.html')

def logout_user(request):
    logout(request)
    return redirect('index')

def additional_form(request):
    config = configparser.ConfigParser()
    config.read('config.ini')
    
    option_list1 = config.get('Bool', 'list').split(', ')
    option_list2 = config.get('Gender', 'list').split(', ')
    option_list3 = config.get('Blood_Group', 'list').split(', ')
    option_list4 = config.get('Often', 'list').split(', ')
    option_list5 = config.get('Smoker_State', 'list').split(', ')
    options = [option_list1, option_list2, option_list3, option_list4, option_list5]

    if request.method == 'POST':
        print(request.POST)
        user = request.user
        age = request.POST['age']
        gender = request.POST['gender']
        blood_group = request.POST['blood_group']
        height = request.POST['height']
        weight = request.POST['weight']
        smoker_status = request.POST['smoker_status']
        heart_rate = request.POST['heart_rate']
        alcoholic = request.POST['alcoholic']
        balenced_diet = request.POST['balenced_diet']
        exercise = request.POST['exercise']
        pre_heart_cond = request.POST['pre_heart_cond']
        family_heart_cond = request.POST['family_heart_cond']
        diabetic = request.POST['diabetic']
        sugar_level = request.POST['sugar_level']
        blood_pressure = request.POST['blood_pressure']
        bp_hypert = request.POST['bp_hypert']
        hypert_treatment = request.POST['hypert_treatment']
        asprin_treatment = request.POST['asprin_treatment']
        lipid_level = request.POST['lipid_level']
        statin = request.POST['statin']
        non_cardiac_ailment = request.POST['non_cardiac_ailment']
        non_cardiac_treatment = request.POST['treatment']
        psychiatric_health_cond = request.POST['psychiatric_health_cond']
        psychiatric_health_cond_name = request.POST['psychiatric_cond_name']

        UserHealthStats_instance = UserHealthStats.objects.create(user = user,
        age = age,
        gender = gender,
        blood_group = blood_group,
        height = height,
        weight = weight,
        smoker_status = smoker_status,
        heart_rate = heart_rate,
        alcoholic = alcoholic,
        balenced_diet = balenced_diet,
        exercise = exercise,
        pre_heart_cond = pre_heart_cond,
        family_heart_cond = family_heart_cond,
        diabetic = diabetic,
        sugar_level = sugar_level,
        blood_pressure = blood_pressure,
        bp_hypert = bp_hypert,
        hypert_treatment = hypert_treatment,
        asprin_treatment = asprin_treatment,
        lipid_level = lipid_level,
        statin = statin,
        non_cardiac_ailment = non_cardiac_ailment,
        non_cardiac_treatment = non_cardiac_treatment,
        psychiatric_health_cond = psychiatric_health_cond,
        psychiatric_health_cond_name = psychiatric_health_cond_name)

        return redirect('dashboard')
    return render(request, 'additional_form.html', {'options': options})