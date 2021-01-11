from django.shortcuts import render, redirect, get_object_or_404
from .forms import AddHiveForm, editHiveForm, addHiveDocumentsForm
from .models import Apiary_details, hive_details, hiveDocuments
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from datetime import date
from django.conf import settings
import boto3
import json
import requests
import sys


@login_required
def hive(request, apiary_id):
    """ A view to display the Users list of hives page """
    apiary = get_object_or_404(Apiary_details, id=apiary_id)
    apiaryID = apiary_id
    hives = hive_details.objects.filter(apiary_id=apiaryID)
    try:
        # -------------- get the exact geolocation ----------------------
        apiarypostcode = apiary.postcode
        key = settings.KEYGEO
        responsegeo = requests.get(
            f"https://api.opencagedata.com/geocode/v1/json?q={apiarypostcode},UK&key={key}"
        )
        geo = responsegeo.json()
        geofomat_str = json.dumps(geo, indent=2)
        geodata = json.loads(geofomat_str)
        for georesults in geodata["results"]:
            originallng = georesults["geometry"]["lng"]
            originallat = georesults["geometry"]["lat"]
            areapreslice = georesults["formatted"]
        # split area at the comma then get the first word
        area = areapreslice.split(",")[0].split(" ")[0]
        # get the exact long and lat to 2 decimal places
        exactlng = "%.2f" % originallng
        exactlat = "%.2f" % originallat

        # -------------- get the exact weatherwith forcast----------------

        queryweather = "lat=" + exactlat + "&lon=" + exactlng
        exclude = "&exclude=" + "minutely," + "alerts"
        units = "&units=" + "metric"
        keyweatherapi = "&appid=" + settings.KEYWEATHER
        response = requests.get(
            f"https://api.openweathermap.org/data/2.5/onecall?{queryweather}{exclude}{units}{keyweatherapi}"
        )
        weatherresp = response.json()
        weather_formatted_str = json.dumps(weatherresp, indent=2)
        weatherdata = json.loads(weather_formatted_str)
        # probability of rain 1-0 pop times by 100 so 1=100 0.50=50
        chanceofprecip = weatherdata["daily"][0]["pop"] * 100
        percipnow = "%.0f" % chanceofprecip

        for wdata in weatherdata["current"]["weather"]:
            dec = wdata["description"]
            icon = wdata["icon"]

        iconnow = f"http://openweathermap.org/img/wn/{icon}.png"
        current_temp = weatherdata["current"]["temp"]
        feels_like = weatherdata["daily"][0]["feels_like"]["day"]
        current_min = weatherdata["daily"][0]["temp"]["min"]
        current_max = weatherdata["daily"][0]["temp"]["max"]
        # if the key is not always availble use .get it will return none if the
        # key not present
        alertcurrent = weatherdata["current"].get("alert")

        # forcast days
        day1min = weatherdata["daily"][1]["temp"]["min"]
        day1max = weatherdata["daily"][1]["temp"]["max"]
        for weatherday1 in weatherdata["daily"][1]["weather"]:
            day1desc = weatherday1["description"]
            day1icon = weatherday1["icon"]
        day1pop = weatherdata["daily"][1]["pop"] * 100
        icon1 = f"http://openweathermap.org/img/wn/{day1icon}.png"

        day2min = weatherdata["daily"][2]["temp"]["min"]
        day2max = weatherdata["daily"][2]["temp"]["max"]
        for weatherday2 in weatherdata["daily"][2]["weather"]:
            day2desc = weatherday2["description"]
            day2icon = weatherday2["icon"]
        day2pop = weatherdata["daily"][2]["pop"]
        icon2 = f"http://openweathermap.org/img/wn/{day2icon}.png"

        day3min = weatherdata["daily"][3]["temp"]["min"]
        day3max = weatherdata["daily"][3]["temp"]["max"]
        for weatherday3 in weatherdata["daily"][3]["weather"]:
            day3desc = weatherday3["description"]
            day3icon = weatherday3["icon"]
        day3pop = weatherdata["daily"][3]["pop"]
        icon3 = f"http://openweathermap.org/img/wn/{day3icon}.png"

        day4min = weatherdata["daily"][4]["temp"]["min"]
        day4max = weatherdata["daily"][4]["temp"]["max"]
        for weatherday4 in weatherdata["daily"][4]["weather"]:
            day4desc = weatherday4["description"]
            day4icon = weatherday4["icon"]
        day4pop = weatherdata["daily"][4]["pop"]
        icon4 = f"http://openweathermap.org/img/wn/{day4icon}.png"

        day5min = weatherdata["daily"][5]["temp"]["min"]
        day5max = weatherdata["daily"][5]["temp"]["max"]
        for weatherday5 in weatherdata["daily"][5]["weather"]:
            day5desc = weatherday5["description"]
            day5icon = weatherday5["icon"]
        day5pop = weatherdata["daily"][5]["pop"]
        icon5 = f"http://openweathermap.org/img/wn/{day5icon}.png"

        context = {
            "apiary": apiary,
            "apiaryID": apiaryID,
            "hives": hives,
            #  Weather
            "dec": dec,
            "area": area,
            "iconnow": iconnow,
            "percipnow": percipnow,
            "current_temp": "%.0f" % current_temp,
            "current_min": "%.0f" % current_min,
            "current_max": "%.0f" % current_max,
            "feels_like": round(feels_like),
            "alertcurrent": alertcurrent,
            "day1min": "%.0f" % day1min,
            "day1max": "%.0f" % day1max,
            "day1desc": day1desc,
            "icon1": icon1,
            "day1pop": "%.0f" % day1pop,
            "day2min": "%.0f" % day2min,
            "day2max": "%.0f" % day2max,
            "day2desc": day2desc,
            "icon2": icon2,
            "day2pop": "%.0f" % day2pop,
            "day3min": "%.0f" % day3min,
            "day3max": "%.0f" % day3max,
            "day3desc": day3desc,
            "icon3": icon3,
            "day3pop": "%.0f" % day3pop,
            "day4min": "%.0f" % day4min,
            "day4max": "%.0f" % day4max,
            "day4desc": day4desc,
            "icon4": icon4,
            "day4pop": "%.0f" % day4pop,
            "day5min": "%.0f" % day5min,
            "day5max": "%.0f" % day5max,
            "day5desc": day5desc,
            "icon5": icon5,
            "day5pop": "%.0f" % day5pop,
        }
    except Exception as ex:
        print("**ERROR**", sys.exc_info()[0], "@", ex)
        # if there is an error with the weather app run
        # hives context regardless.
        context = {
            "apiary": apiary,
            "apiaryID": apiaryID,
            "hives": hives,
        }
    return render(request, "hives/hive.html", context)


@login_required
def addHive(request, apiary_id, pk=None):
    """ A view to display the add hives page """
    ap = apiary_id
    # get an instance of the apiary pk
    instofID = get_object_or_404(Apiary_details, id=apiary_id)
    hive_details = get_object_or_404(hive, pk=pk) if pk else None
    if request.method == "POST":
        form = AddHiveForm(request.POST)
        if form.is_valid():
            hive_details = form.save(commit=False)
            hive_details.user = request.user.id
            hive_details.apiary_id = instofID
            hive_details.hive_old_apiary = instofID.full_name
            hive_details.save()
            messages.success(
                request,
                f"Added {hive_details.hive_name}\
                             To your Apiary",
            )
            return redirect("hive", ap)
        else:
            messages.error(request, "Your hive was not valid")
    else:
        form = AddHiveForm()
        context = {
            "ap": ap,
            "form": form,
        }
        return render(request, "hives/addHive.html", context)


@login_required
def editHive(request, apiaryID, pk=None):
    """ A view to display the Edit hives page """
    ap = apiaryID
    currentApiary = get_object_or_404(Apiary_details, pk=apiaryID)
    edithive = get_object_or_404(hive_details, pk=pk) if pk else None
    if request.method == "POST":
        form = editHiveForm(request.user, request.POST, instance=edithive)
        if form.is_valid():
            new = str(edithive.apiary_id)
            current = str(currentApiary.full_name)
            edithive = form.save(commit=False)
            # If the new apiary is not the same as the currenty apiary if
            # there is one.
            # else if its null or blank move to the next statement
            if new != current:
                edithive.hive_new_apiary = new
                edithive.hive_old_apiary = current
                edithive.hive_move_date = date.today()
                messages.success(
                    request,
                    f"Hive: {edithive.hive_name.capitalize()} was\
                     Updated And Moved To Apiary: {edithive.apiary_id}!",
                )
            else:
                messages.success(
                    request,
                    f"Hive: {edithive.hive_name.capitalize()} was\
                             Updated!",
                )
            edithive.save()
            return redirect("hive", ap)
        else:
            messages.error(request, "Error Hive Was Not Updated!")
    else:
        # Send in request.user to so the queryset can be set so only the
        # logged in user can see apiarys that belong to them.
        form = editHiveForm(request.user, instance=edithive)
        messages.info(
            request,
            f"You are editing\
                      Hive: {edithive.hive_name.capitalize()}!",
        )
        context = {
            "ap": ap,
            "form": form,
            "currentApiary": currentApiary,
        }
        return render(request, "hives/editHive.html", context)


@login_required
def deleteHive(request, apiaryID, pk):
    """ A view to delete Hives Sites """
    apiary_id = apiaryID
    nameapiary = get_object_or_404(Apiary_details, pk=apiaryID)
    hivedel = get_object_or_404(hive_details, pk=pk)
    if request.method == "POST":
        messages.warning(
            request,
            f"You have Deleted {hivedel.hive_name} From \
                     Apiary {nameapiary.full_name}",
        )
        hivedel.delete()
        return redirect("hive", apiary_id)
    context = {
        "hivedel": hivedel,
        "apiary_id": apiary_id,
    }
    return render(request, "hives/confirm_hive_delete.html", context)


@login_required
def hiveDocs(request, apiaryPK, pk):
    """ A view to display the Hive Documents relevent to the hive PK """
    docs = hiveDocuments.objects.filter(hivenumber=pk)
    hivename = get_object_or_404(hive_details, pk=pk)
    context = {
        "docs": docs,
        "hivename": hivename,
        "apiaryPK": apiaryPK,
    }
    return render(request, "hives/hiveDocs.html", context)


@login_required
def addhiveDoc(request, apiaryPK, pk=None):
    """ A view to display the add Hive Documents """
    instofID = get_object_or_404(hive_details, pk=pk)
    if request.method == "POST":
        form = addHiveDocumentsForm(request.POST, request.FILES)
        if form.is_valid():
            hiveDocuments = form.save(commit=False)
            hiveDocuments.hivenumber = instofID
            hiveDocuments.beekeepername = request.user
            hiveDocuments.date = date.today()
            hiveDocuments.save()
            messages.success(
                request,
                f"Hive Record Was\
                           Added {instofID.hive_name}",
            )
            return redirect("hiveDocs", apiaryPK, pk)
        else:
            messages.error(
                request,
                f"Error New Hive Record: {instofID.hive_name} Was\
                           Not Added!",
            )
    else:
        form = addHiveDocumentsForm()
        context = {
            "form": form,
        }
        return render(request, "hives/addHiveDoc.html", context)


@login_required
def editHiveDoc(request, apiaryPK, hive_id, pk):
    """ A view to display the Edit Hive Documents """
    hiveid = hive_id
    docid = pk
    instdoc = get_object_or_404(hiveDocuments, pk=pk)
    if request.method == "POST":
        form = addHiveDocumentsForm(request.POST, request.FILES,
                                    instance=instdoc)
        if form.is_valid():
            instdoc.save()
            messages.success(
                request,
                f"Log Number: {instdoc.pk} Was\
                             Updated!",
            )
            return redirect("hiveDocs", apiaryPK, hiveid)
        else:
            messages.error(
                request,
                f"Error Log Number: {instdoc.pk} Was\
                           Not Updated!",
            )
    else:
        form = addHiveDocumentsForm(instance=instdoc)
        messages.info(request, f"You Are Editing {instdoc.pk}!")
        context = {
            "form": form,
            "docid": docid,
            "instdoc": instdoc,
        }
        return render(request, "hives/editHiveDoc.html", context)


@login_required
def deleteHivedoc(request, apiaryPK, hive_id, pk):
    """ A view to delete Hives Sites """
    hiveid = hive_id
    hivedetail = get_object_or_404(hive_details, pk=hive_id)
    hivedocdel = get_object_or_404(hiveDocuments, pk=pk)
    bucketname = settings.AWS_STORAGE_BUCKET_NAME
    s3 = boto3.resource("s3")
    if request.method == "POST":
        # if there is an image1 or 2 delete them from the s3 storage bucket
        if hivedocdel.image1.name:
            s3.Object(bucketname, hivedocdel.image1.name).delete()
        if hivedocdel.image2.name:
            s3.Object(bucketname, hivedocdel.image2.name).delete()
        messages.warning(
            request,
            f"You Have Deleted Hive Record: {hivedocdel.pk} From\
                     Hive: {hivedetail.hive_name}",
        )
        hivedocdel.delete()
        return redirect("hiveDocs", apiaryPK, hiveid)
    context = {
        "hivedocdel": hivedocdel,
        "hiveid": hiveid,
        "apiaryPK": apiaryPK,
    }
    return render(request, "hives/confirm_hive_record_delete.html", context)
