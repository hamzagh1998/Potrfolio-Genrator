from django.contrib import messages
from django.views.generic import ListView
from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from .forms import RegisterationForm, LoginForm, ProfileForm, UserForm
from jobs.models import UserJob
from .models import Profile

class UsersListView(ListView):

    model = Profile
    template_name = "users/index.html"
    context_object_name = "profile"
    ordering = ['-id']
    paginate_by = 10

class SearchListView(ListView):
    model = Profile
    template_name = 'blog/search_result.html'
    context_object_name = 'profile'
    ordering = ['-id']
    paginate_by = 10

    def get_queryset(self): # new
        query = self.request.GET.get('q')
        result = Profile.objects.filter(Q(user__icontains=query) | Q(job__icontains=query) |
                                        Q(school__icontains=query) | Q(country__icontains=query))

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['query'] = self.request.GET.get('q')
        return context


def register(request):

    if request.user.is_authenticated:
        return redirect('index')

    if request.method == 'POST':
        form = RegisterationForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return redirect('users:login')

    else:
        form = RegisterationForm()

    return render(request, 'users/register.html', {'form':form})


def log_in(request):
    if request.user.is_authenticated:
        return redirect('index')

    if request.POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user:
                login(request, user)
                return redirect('index')
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {'form':form})

@login_required(login_url='users:login')
def log_out(request):

    logout(request)
    return redirect('index')

def userProfile(request, slug):

    profile = get_object_or_404(Profile, slug=slug)
    jobs = UserJob.objects.filter(profile_id=profile)

    return render(request, 'users/user_profile.html', {'profile':profile, 'jobs':jobs})

def userJob(request, id):

    job = get_object_or_404(UserJob, id=id)

    return render(request, 'users/job_detail.html', {'job':job})

def profileFormView(request):

    if not request.user.is_authenticated:
        return redirect("users:login")

    if request.POST:
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save(commit=True)
            profile_form.save(commit=True)

            return redirect("users:user_profile", request.user.profile.slug)
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)

    return render(request, 'users/profile_form.html', {'user_form':user_form, 'profile_form':profile_form})

def accounFormView(request):

    if not request.user.is_authenticated:
        return redirect("users:login")

    if request.POST:
        account_form = UserForm(request.POST, instance=request.user)
        if account_form.is_valid():
            account_form.save(commit=True)
            return redirect("users:user_profile", request.user.profile.slug)
    else:
        account_form = UserForm(instance=request.user)

    return render(request, "users/user_account.html", {"form":account_form})

def deletePortfolio(request, id):

    if not request.user.is_authenticated:
        return redirect("users:login")

    portfolio = get_object_or_404(Profile, id=id)
    if request.user != portfolio.user:
        return HttpResponse('You are not the author of this portfolio')

    portfolio.delete()
    portfolio.user.delete()

    return redirect('users:logout')
