from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from apiary.models import Apiary_details
from hives.models import hive_details, hiveDocuments
from medical.models import hiveMedical, hiveMedicalRecords
from hives import views as hiveViews


@login_required
def profile(request):
    user = request.user
    imageQuoter = hiveViews.imageQuoter
    apiaries_number = Apiary_details.objects.filter(user=user.id).count()
    hives_number = hive_details.objects.filter(user=user.id).count()
    docs_number = hiveDocuments.objects.filter(user=user.id).count()
    purchased_meds = hiveMedical.objects.filter(user=user).count()
    used_meds = hiveMedicalRecords.objects.filter(user=user.id).count()
    up_img_1 = hiveDocuments.objects.filter(user=user.id).values("image1")
    up_img_2 = hiveDocuments.objects.filter(user=user.id).values("image2")
    totalUploadedImages = hiveViews.image_counter(up_img_1, "image1") + hiveViews.image_counter(
        up_img_2, "image2")

    context = {
        "user": user,
        "apiaries_number": apiaries_number,
        "hives_number": hives_number,
        "docs_number": docs_number,
        "purchased_meds": purchased_meds,
        "used_meds": used_meds,
        "totalUploadedImages": totalUploadedImages,
        "imageQuoter": imageQuoter
    }
    return render(request, "profiles/user_profile.html", context)


