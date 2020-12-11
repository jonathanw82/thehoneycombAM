from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import get_template
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from xhtml2pdf import pisa
from hives.models import hiveDocuments, hive_details
from datetime import date
from django.conf import settings
from django.contrib.staticfiles import finders
import os


@login_required
def hive_record_pdf_view(request, *args, **kwargs):
    pk = kwargs.get("pk")
    todaysDate = date.today()
    hiveRecords = hiveDocuments.objects.filter(hivenumber=pk)
    hivename = get_object_or_404(hive_details, pk=pk)
    template_path = "pdf/pdfHiveRecords.html"
    context = {
        "todaysDate": todaysDate,
        "hiveRecords": hiveRecords,
        "hivename": hivename,
    }
    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type="application/pdf")
    # if download:
    # response['Content-Disposition'] = 'attachment; filename="report.pdf"'
    # if diaplay:
    response[
        "Content-Disposition"
    ] = f'filename="hiveRecords-{hivename}-{todaysDate}.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render(context)
    # create a pdf
    pisa_status = pisa.CreatePDF(html, dest=response,
                                 link_callback=link_callback)
    # if error then show some funy view
    if pisa_status.err:
        return HttpResponse("We had some errors <pre>" + html + "</pre>")
    return response


@login_required
def link_callback(uri, rel):
    """
    Convert HTML URIs to absolute system paths so xhtml2pdf can access those
    resources
    """
    result = finders.find(uri)
    if result:
        if not isinstance(result, (list, tuple)):
            result = [result]
        result = list(os.path.realpath(path) for path in result)
        path = result[0]
    else:
        # Typically /static/
        sUrl = settings.STATIC_URL
        # Typically /home/userX/project_static/
        sRoot = settings.STATIC_ROOT
        # Typically /media/
        mUrl = settings.MEDIA_URL
        # Typically /home/userX/project_static/media/
        mRoot = settings.MEDIA_ROOT

        if uri.startswith(mUrl):
            path = os.path.join(mRoot, uri.replace(mUrl, ""))
        elif uri.startswith(sUrl):
            path = os.path.join(sRoot, uri.replace(sUrl, ""))
        else:
            return uri

    # make sure that file exists
    if not os.path.isfile(path):
        raise Exception("media URI must start with %s or %s" % (sUrl, mUrl))
    return path
