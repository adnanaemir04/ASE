from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect
from .forms import CourseForm,LectureForm
from article.models import Article


from .models import Course, Lecture

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/courses.html', {'courses': courses})

def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    lectures = course.lectures.all().order_by('order_index')
    return render(request, 'courses/course_detail.html', {
        'course': course,
        'lectures': lectures,
    })

def lecture_detail(request, pk):
    lecture = get_object_or_404(Lecture, pk=pk)
    return render(request, 'courses/lecture_detail.html', {
        'lecture': lecture
    })
    
@login_required
def add_course(request):
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            course = form.save(commit=False)
            course.author = request.user
            course.save()
            return redirect('courses:course_detail', pk=course.id)
    else:
        form = CourseForm()
    return render(request, 'courses/add_course.html', {'form': form})

@login_required
def add_lecture(request, pk):
    course = get_object_or_404(Course, pk=pk)

    # sadece kursun sahibi ders ekleyebilir
    if course.author != request.user:
        return redirect('courses:dashboard')

    if request.method == 'POST':
        form = LectureForm(request.POST, request.FILES)
        if form.is_valid():
            lecture = form.save(commit=False)
            lecture.course = course
            lecture.save()
            return redirect('courses:course_detail', pk=course.id)
    else:
        form = LectureForm()

    return render(request, 'courses/add_lecture.html', {
        'form': form,
        'course': course
    })



@login_required
def instructor_dashboard(request):
    all_courses = Course.objects.filter(author=request.user)
    user_articles = Article.objects.filter(author=request.user)

    return render(request, 'courses/dashboard.html', {
        'courses': all_courses,
        'articles': user_articles
    })
