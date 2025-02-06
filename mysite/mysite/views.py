from django.http import HttpResponse
from django.shortcuts import render
import requests
from django.conf import settings
import logging
from django.shortcuts import render, Http404


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


students_data = [
    {
        'name': 'John',
        'id': 1,
        'marks': [10, 20, 30]
    },
    {
        'name': 'Steve',
        'id': 2,
        'marks': [40, 50, 60]
    },
    {
        'name': 'Sarah',
        'id': 3,
        'marks': [75, 85, 90]
    },
    {
        'name': 'Mike',
        'id': 4,
        'marks': [65, 70, 75]
    },
    {
        'name': 'Lisa',
        'id': 5,
        'marks': [30, 25, 35]
    },
    {
        'name': 'David',
        'id': 6,
        'marks': [55, 60, 65]
    },
    {
        'name': 'Emma',
        'id': 7,
        'marks': [80, 85, 90]
    },
    {
        'name': 'Tom',
        'id': 8,
        'marks': [45, 50, 40]
    },
    {
        'name': 'Anna',
        'id': 9,
        'marks': [70, 75, 80]
    },
    {
        'name': 'James',
        'id': 10,
        'marks': [20, 25, 30]
    }
]


def student_detail(request, student_id):
    # Find student with matching ID
    student = next((s for s in students_data if s['id'] == student_id), None)

    if student is None:
        raise Http404("Student not found")

    # Calculate total and average marks
    total_marks = sum(student['marks'])
    avg_marks = total_marks / len(student['marks'])

    # Determine pass/fail status (passing mark is 50)
    status = 'Pass' if avg_marks >= 50 else 'Fail'

    context = {
        'student': student,
        'total_marks': total_marks,
        'average_marks': round(avg_marks, 2),
        'status': status,
        'subjects': ['Math', 'Science', 'English']
    }

    return render(request, 'student_marks.html', context)
