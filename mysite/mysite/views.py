from django.http import HttpResponse
from django.shortcuts import render
import requests
# from django.conf import settings
import logging
# from django.shortcuts import render, Http404


logger = logging.getLogger(__name__)


def home(request):
    """Fetch and display countries data."""
    try:
        response = requests.get(
            "https://restcountries.com/v3.1/all",
            timeout=10  # Add timeout for better error handling
        )
        response.raise_for_status()
        countries = response.json()
        # Sort countries by name for better UX
        countries.sort(key=lambda x: x.get('name', {}).get('common', ''))
    except requests.RequestException as e:
        logger.error(f"Error fetching countries data: {str(e)}")
        countries = []
        # Add error message to display to user
        return render(request, 'home.html', {
            'countries': countries,
            'error_message': 'Unable to fetch countries data. Please try again later.'
        })

    return render(request, 'home.html', {'countries': countries})


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


def data_render(request):
    data = 'steve'
    return render(request, 'mydata.html', {'data': data})


def country_selection(request):
    """Handle country selection form submission."""
    if request.method == 'POST':
        selected_country = request.POST.get('country')
        # Process the selected country
        return render(request, 'country_details.html', {'country': selected_country})
    return HttpResponse("Invalid request method", status=400)


def d_view(request, id):
    return render(request, 'ddata.html', {'ddata': id})


students = [
    {'name': 'John', 'id': 1, 'marks': [10, 20, 30]},
    {'name': 'Steve', 'id': 2, 'marks': [40, 50, 60]},
    {'name': 'Sarah', 'id': 3, 'marks': [75, 85, 90]},
    {'name': 'Mike', 'id': 4, 'marks': [65, 70, 75]},
    {'name': 'Lisa', 'id': 5, 'marks': [30, 25, 35]},
    {'name': 'David', 'id': 6, 'marks': [55, 60, 65]},
    {'name': 'Emma', 'id': 7, 'marks': [80, 85, 90]},
    {'name': 'Tom', 'id': 8, 'marks': [45, 50, 40]},
    {'name': 'Anna', 'id': 9, 'marks': [70, 75, 80]},
    {'name': 'James', 'id': 10, 'marks': [20, 25, 30]}
]


# get each student marks by their id and know if the student is pass or fail in each subject if the stdent get marks >20?
# views.py
# def student_detail(request, marks):
#     status = "Pass" if marks > 50 else "Fail"
#     return render(request, "student_detail.html", {"status": status})
# def student_detail(request, student_id):
#     student = next((s for s in students if s['id'] == student_id), None)
#     if student:
#         total_marks = sum(student['marks'])
#         status = "Pass" if total_marks > 50 else "Fail"
#         context = {
#             "student": student,
#             "total_marks": total_marks,
#             "status": status,
#         }
#         return render(request, "student_detail.html", context)
#     else:
#         return render(request, "student_detail.html", {"error": "Student not found"})


students = [
    {'name': 'kartikey', 'id': 1, 'marks': [-1, -2, -3]},
    {'name': 'Steve', 'id': 2, 'marks': [40, 50, 60]},
    {'name': 'Sarah', 'id': 3, 'marks': [75, 85, 90]},
    {'name': 'Mike', 'id': 4, 'marks': [65, 70, 75]},
    {'name': 'Lisa', 'id': 5, 'marks': [30, 25, 35]},
    {'name': 'David', 'id': 6, 'marks': [55, 60, 65]},
    {'name': 'Emma', 'id': 7, 'marks': [80, 85, 90]},
    {'name': 'Tom', 'id': 8, 'marks': [45, 50, 40]},
    {'name': 'Anna', 'id': 9, 'marks': [70, 75, 80]},
    {'name': 'James', 'id': 10, 'marks': [20, 25, 30]}
]


def student_detail(request, student_id):
    student = next((s for s in students if s['id'] == student_id), None)

    if student:
        total_marks = sum(student['marks'])
        num_subjects = len(student['marks'])
        # Avoid division by zero
        avg_marks = total_marks / num_subjects if num_subjects > 0 else 0

        overall_status = "Pass" if avg_marks > 50 else "Fail"

        subject_statuses = ["Pass" if mark >
                            20 else "Fail" for mark in student['marks']]

        context = {
            "student": student,
            "total_marks": total_marks,
            "avg_marks": avg_marks,
            "overall_status": overall_status,
            "subject_statuses": subject_statuses,
        }
        return render(request, "student_detail.html", context)
    else:
        return render(request, "student_detail.html", {"error": "Student not found"})
