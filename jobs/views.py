from django.shortcuts import render, redirect, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import DeleteView
from .forms import JobForm, JobUpdateForm
from.models import UserJob

def jobFormView(request):

    if request.method == 'POST':
        form = JobForm(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            user = request.user.profile
            obj.profile_id = user
            obj.save()
            form = JobForm()

            return redirect('users:user_profile', request.user.profile.slug)
    else:
        form = JobForm()

    return render(request, 'jobs/job_form.html', {'form':form})

def jobUpdateFormView(request, id):

    if not request.user.is_authenticated:
        return redirect("users:login")

    user_job = get_object_or_404(UserJob, id=id)

    if request.user.profile != user_job.profile_id:
        return HttpResponse("You're not the author of this job!")

    if request.POST:
        form = JobUpdateForm(request.POST or None, request.FILES or None, instance=user_job)
        if form.is_valid():
            form.save(commit=True)
            return redirect("users:user_profile", request.user.profile.slug)
    else:
        form = JobUpdateForm(initial={"title":user_job.title,
                                      "image":user_job.image,
                                      "body":user_job.body,
                                      "url":user_job.url
                                     })

    return render(request, 'jobs/job_update_form.html', {'form':form})


class DeleteJob(LoginRequiredMixin, UserPassesTestMixin, DeleteView):

    model = UserJob
    success_url = '/'

    def test_func(self):
        job = self.get_object()
        if self.request.user.profile == job.profile_id:
            return True
        return False
