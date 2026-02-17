from django.contrib import messages
from django.shortcuts import get_object_or_404, redirect, render

from apps.recruit.forms import CVForm
from apps.recruit.models import CV
from apps.recruit.serializers.cv_serializer import CVSerializer


def cv_create_view(request):
    if request.method == "POST":
        form = CVForm(request.POST, request.FILES)
        if form.is_valid():
            cv = form.save()
            messages.success(request, "CV enregistré avec succès.")
            return redirect("recruit:cv_detail", cv_id=cv.id)
    else:
        form = CVForm()

    return render(request, "recruit/cv_form.html", {"form": form})


def cv_detail_view(request, cv_id: int):
    cv = get_object_or_404(CV.objects.prefetch_related("translations", "skills"), pk=cv_id)
    serialized_cv = CVSerializer(cv).data()
    return render(request, "recruit/cv_detail.html", {"cv": serialized_cv})
