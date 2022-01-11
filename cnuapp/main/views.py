from django.contrib import messages
from django.shortcuts import render, redirect
from datetime import datetime
from .models import Parking_A, Parking_B, Parking_C1, Parking_C2, Parking_D, Parking_E1, Parking_E2, Parking_E3, \
    Parking_E4, Parking_F, Parking_G, Parking_H, Parking_I, Parking_J, Parking_K, Parking_L, Parking_M, log
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm
from .forms import ParkingForm, ParkingBForm, ParkingC1Form, ParkingC2Form, ParkingDForm, ParkingE1Form, ParkingE2Form, \
    ParkingE3Form, ParkingE4Form, ParkingFForm, ParkingGForm, ParkingHForm, ParkingIForm, ParkingJForm, ParkingKForm, \
    ParkingLForm, ParkingMForm


def home(request):
    if request.user.is_authenticated:
        logout(request)
        return render(request, 'home.html', {})
    else:
        return render(request, 'home.html', {})


def user_login(request):
    if request.method == "POST":
        user = authenticate(request, username=request.POST.get('username'), password=request.POST.get('password'))
        if user is None:
            error = 'Invalid username or password.'
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': error})
        else:
            login(request, user)
            return redirect('map')
    return render(request, 'login.html', {'form': AuthenticationForm()})


def user(request):
    logs = log.objects.all()

    if request.user.is_authenticated:
        context = {'log': logs}
        return render(request, 'user.html', context)
    else:
        return redirect('login')


def map(request):
    logs = log.objects.all()
    if request.user.is_authenticated:
        return render(request, 'map.html', {'log': logs})
    else:
        return redirect('login')


def leave(request):
    if request.user.is_authenticated:
        return render(request, 'leave.html')
    else:
        return redirect('login')


def parkinga(request):
    parking_spots = Parking_A.objects.all()
    logs = log.objects.all()
    if request.user.is_authenticated:
        context = {'parking_spot': parking_spots, 'log': logs}
        return render(request, 'parkinga.html', context)
    else:
        return redirect('login')


def parkingb(request):
    logs = log.objects.all()
    parkingb_spots = Parking_B.objects.all()

    if request.user.is_authenticated:
        context = {'parkingb_spot': parkingb_spots, 'log': logs}

        return render(request, 'parkingb.html', context)
    else:
        return redirect('login')


def parkingc1(request):
    logs = log.objects.all()
    parkingc1_spots = Parking_C1.objects.all()

    if request.user.is_authenticated:
        context = {'parkingc1_spot': parkingc1_spots, 'log': logs}

        return render(request, 'parkingc1.html', context)
    else:
        return redirect('login')


def parkingc2(request):
    logs = log.objects.all()
    parkingc2_spots = Parking_C2.objects.all()

    if request.user.is_authenticated:
        context = {'parkingc2_spot': parkingc2_spots, 'log': logs}

        return render(request, 'parkingc2.html', context)
    else:
        return redirect('login')


def parkingd(request):
    logs = log.objects.all()
    parkingd_spots = Parking_D.objects.all()

    if request.user.is_authenticated:
        context = {'parkingd_spot': parkingd_spots, 'log': logs}

        return render(request, 'parkingd.html', context)
    else:
        return redirect('login')


def parkinge1(request):
    logs = log.objects.all()
    parkinge1_spots = Parking_E1.objects.all()

    if request.user.is_authenticated:
        context = {'parkinge1_spot': parkinge1_spots, 'log': logs}

        return render(request, 'parkinge1.html', context)
    else:
        return redirect('login')


def parkinge2(request):
    logs = log.objects.all()
    parkinge2_spots = Parking_E2.objects.all()

    if request.user.is_authenticated:
        context = {'parkinge2_spot': parkinge2_spots, 'log': logs}

        return render(request, 'parkinge2.html', context)
    else:
        return redirect('login')


def parkinge3(request):
    logs = log.objects.all()
    parkinge3_spots = Parking_E3.objects.all()

    if request.user.is_authenticated:
        context = {'parkinge3_spot': parkinge3_spots, 'log': logs}

        return render(request, 'parkinge3.html', context)
    else:
        return redirect('login')


def parkinge4(request):
    logs = log.objects.all()
    parkinge4_spots = Parking_E4.objects.all()

    if request.user.is_authenticated:
        context = {'parkinge4_spot': parkinge4_spots, 'log': logs}

        return render(request, 'parkinge4.html', context)
    else:
        return redirect('login')


def parkingf(request):
    logs = log.objects.all()
    parkingf_spots = Parking_F.objects.all()

    if request.user.is_authenticated:
        context = {'parkingf_spot': parkingf_spots, 'log': logs}

        return render(request, 'parkingf.html', context)
    else:
        return redirect('login')


def parkingg(request):
    logs = log.objects.all()
    parkingg_spots = Parking_G.objects.all()

    if request.user.is_authenticated:
        context = {'parkingg_spot': parkingg_spots, 'log': logs}

        return render(request, 'parkingg.html', context)
    else:
        return redirect('login')


def parkingh(request):
    logs = log.objects.all()
    parkingh_spots = Parking_H.objects.all()

    if request.user.is_authenticated:
        context = {'parkingh_spot': parkingh_spots, 'log': logs}

        return render(request, 'parkingh.html', context)
    else:
        return redirect('login')


def parkingi(request):
    logs = log.objects.all()
    parkingi_spots = Parking_I.objects.all()

    if request.user.is_authenticated:
        context = {'parkingi_spot': parkingi_spots, 'log': logs}

        return render(request, 'parkingi.html', context)
    else:
        return redirect('login')


def parkingj(request):
    logs = log.objects.all()
    parkingj_spots = Parking_J.objects.all()

    if request.user.is_authenticated:
        context = {'parkingj_spot': parkingj_spots, 'log': logs}

        return render(request, 'parkingj.html', context)
    else:
        return redirect('login')


def parkingk(request):
    logs = log.objects.all()
    parkingk_spots = Parking_K.objects.all()

    if request.user.is_authenticated:
        context = {'parkingk_spot': parkingk_spots, 'log': logs}

        return render(request, 'parkingk.html', context)
    else:
        return redirect('login')


def parkingl(request):
    logs = log.objects.all()
    parkingl_spots = Parking_L.objects.all()

    if request.user.is_authenticated:
        context = {'parkingl_spot': parkingl_spots, 'log': logs}

        return render(request, 'parkingl.html', context)
    else:
        return redirect('login')


def parkingm(request):
    logs = log.objects.all()
    parkingm_spots = Parking_M.objects.all()

    if request.user.is_authenticated:
        context = {'parkingm_spot': parkingm_spots, 'log': logs}

        return render(request, 'parkingm.html', context)
    else:
        return redirect('login')


def update(request, parking_spot):
    update_spot = Parking_A.objects.get(pk=parking_spot)
    form = ParkingForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parking_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkinga')
            else:
                form.save()
                updates = log.objects.create(username=request.user, time_parked=datetime.now(),parking_spot=Parking_A.objects.get(
                    parking_spot=parking_spot,
                    parking_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': update, 'form': form})


def updateb(request, parkingb_spot):
    update_spot = Parking_B.objects.get(pk=parkingb_spot)
    form = ParkingBForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingb_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingb')
            else:
                form.save()
                updates = log(username=request.user, parking_spotB=Parking_B.objects.get(parkingb_spot=parkingb_spot,
                                                                                         parkingb_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updateb, 'form': form})


def updatec1(request, parkingc1_spot):
    update_spot = Parking_C1.objects.get(pk=parkingc1_spot)
    form = ParkingC1Form(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingc1_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingc1')
            else:
                form.save()
                updates = log(username=request.user, parking_spotC1=Parking_C1.objects.get(parkingc1_spot=parkingc1_spot,
                                                                                           parkingc1_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatec1, 'form': form})


def updatec2(request, parkingc2_spot):
    update_spot = Parking_C2.objects.get(pk=parkingc2_spot)
    form = ParkingC2Form(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingc2_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingc2')
            else:
                form.save()
                updates = log(username=request.user, parking_spotC2=Parking_C2.objects.get(parkingc2_spot=parkingc2_spot,
                                                                                           parkingc2_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatec2, 'form': form})


def updated(request, parkingd_spot):
    update_spot = Parking_D.objects.get(pk=parkingd_spot)
    form = ParkingDForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingd_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingd')
            else:
                form.save()
                updates = log(username=request.user, parking_spotD=Parking_D.objects.get(parkingd_spot=parkingd_spot,
                                                                                         parkingd_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updated, 'form': form})


def updatee1(request, parkinge1_spot):
    update_spot = Parking_E1.objects.get(pk=parkinge1_spot)
    form = ParkingE1Form(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkinge1_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkinge1')
            else:
                form.save()
                updates = log(username=request.user, parking_spotE1=Parking_E1.objects.get(parkinge1_spot=parkinge1_spot,
                                                                                           parkinge1_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatee1, 'form': form})


def updatee2(request, parkinge2_spot):
    update_spot = Parking_E2.objects.get(pk=parkinge2_spot)
    form = ParkingE2Form(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkinge2_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkinge2')
            else:
                form.save()
                updates = log(username=request.user, parking_spotE2=Parking_E2.objects.get(parkinge2_spot=parkinge2_spot,
                                                                                           parkinge2_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatee2, 'form': form})


def updatee3(request, parkinge3_spot):
    update_spot = Parking_E3.objects.get(pk=parkinge3_spot)
    form = ParkingE3Form(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkinge3_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkinge3')
            else:
                form.save()
                updates = log(username=request.user, parking_spotE3=Parking_E3.objects.get(parkinge3_spot=parkinge3_spot,
                                                                                           parkinge3_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatee3, 'form': form})


def updatee4(request, parkinge4_spot):
    update_spot = Parking_E4.objects.get(pk=parkinge4_spot)
    form = ParkingE4Form(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkinge4_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkinge4')
            else:
                form.save()
                updates = log(username=request.user, parking_spotE4=Parking_E4.objects.get(parkinge4_spot=parkinge4_spot,
                                                                                           parkinge4_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatee4, 'form': form})


def updatef(request, parkingf_spot):
    update_spot = Parking_F.objects.get(pk=parkingf_spot)
    form = ParkingFForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingf_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingf')
            else:
                form.save()
                updates = log(username=request.user, parking_spotF=Parking_F.objects.get(parkingf_spot=parkingf_spot,
                                                                                         parkingf_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatef, 'form': form})


def updateg(request, parkingg_spot):
    update_spot = Parking_G.objects.get(pk=parkingg_spot)
    form = ParkingGForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingg_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingg')
            else:
                form.save()
                updates = log(username=request.user, parking_spotG=Parking_G.objects.get(parkingg_spot=parkingg_spot,
                                                                                         parkingg_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updateg, 'form': form})


def updateh(request, parkingh_spot):
    update_spot = Parking_H.objects.get(pk=parkingh_spot)
    form = ParkingHForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingh_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingh')
            else:
                form.save()
                updates = log(username=request.user, parking_spotH=Parking_H.objects.get(parkingh_spot=parkingh_spot,
                                                                                         parkingh_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updateh, 'form': form})


def updatei(request, parkingi_spot):
    update_spot = Parking_I.objects.get(pk=parkingi_spot)
    form = ParkingIForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingi_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingi')
            else:
                form.save()
                updates = log(username=request.user, parking_spotI=Parking_I.objects.get(parkingi_spot=parkingi_spot,
                                                                                         parkingi_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatei, 'form': form})


def updatej(request, parkingj_spot):
    update_spot = Parking_J.objects.get(pk=parkingj_spot)
    form = ParkingJForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingj_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingj')
            else:
                form.save()
                updates = log(username=request.user, parking_spotJ=Parking_J.objects.get(parkingj_spot=parkingj_spot,
                                                                                         parkingj_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatej, 'form': form})


def updatek(request, parkingk_spot):
    update_spot = Parking_K.objects.get(pk=parkingk_spot)
    form = ParkingKForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingk_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingk')
            else:
                form.save()
                updates = log(username=request.user, parking_spotK=Parking_K.objects.get(parkingk_spot=parkingk_spot,
                                                                                         parkingk_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatek, 'form': form})


def updatel(request, parkingl_spot):
    update_spot = Parking_L.objects.get(pk=parkingl_spot)
    form = ParkingLForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingl_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingl')
            else:
                form.save()
                updates = log(username=request.user, parking_spotL=Parking_L.objects.get(parkingl_spot=parkingl_spot,
                                                                                         parkingl_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatel, 'form': form})


def updatem(request, parkingm_spot):
    update_spot = Parking_M.objects.get(pk=parkingm_spot)
    form = ParkingMForm(request.POST or None, instance=update_spot)
    if form.is_valid():
        try:
            if log.objects.get(username=request.user, currently_parked_here=True):
                messages.error(request, "Please leave your current parking spot to continue")
                return redirect('map')
        except Exception:
            data = form.cleaned_data.get("parkingm_status")
            if data is True:
                messages.error(request, "You did not update your parking spot. Please choose a parking spot "
                                        "below and select 'Parked here' when submitting your form.")
                return redirect('parkingm')
            else:
                form.save()
                updates = log(username=request.user, parking_spotM=Parking_M.objects.get(parkingm_spot=parkingm_spot,
                                                                                         parkingm_status=False))
                updates.save()
                messages.success(request, "Parking spot updated successfully!")
                return redirect('map')

    return render(request, "update.html", {'updated': updatem, 'form': form})


def deletea(request, parking_spot):
    delete_spot = Parking_A.objects.get(pk=parking_spot)
    form = ParkingForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parking_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkinga')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spot=Parking_A.objects.get(
                parking_spot=parking_spot,
                parking_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletea, 'form': form})


def deleteb(request, parkingb_spot):
    delete_spot = Parking_B.objects.get(pk=parkingb_spot)
    form = ParkingBForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingb_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingb')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotB=Parking_B.objects.get(
                parkingb_spot=parkingb_spot,
                parkingb_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deleteb, 'form': form})


def deletec1(request, parkingc1_spot):
    delete_spot = Parking_C1.objects.get(pk=parkingc1_spot)
    form = ParkingC1Form(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingc1_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingc1')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotC1=Parking_C1.objects.get(
                parkingc1_spot=parkingc1_spot,
                parkingc1_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletec1, 'form': form})


def deletec2(request, parkingc2_spot):
    delete_spot = Parking_C2.objects.get(pk=parkingc2_spot)
    form = ParkingC2Form(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingc2_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingc2')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotC2=Parking_C2.objects.get(
                parkingc2_spot=parkingc2_spot,
                parkingc2_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletec2, 'form': form})


def deleted(request, parkingd_spot):
    delete_spot = Parking_D.objects.get(pk=parkingd_spot)
    form = ParkingDForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingd_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingd')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotD=Parking_D.objects.get(
                parkingd_spot=parkingd_spot,
                parkingd_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deleted, 'form': form})


def deletee1(request, parkinge1_spot):
    delete_spot = Parking_E1.objects.get(pk=parkinge1_spot)
    form = ParkingE1Form(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkinge1_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkinge1')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotE1=Parking_E1.objects.get(
                parkinge1_spot=parkinge1_spot,
                parkinge1_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletee1, 'form': form})


def deletee2(request, parkinge2_spot):
    delete_spot = Parking_E2.objects.get(pk=parkinge2_spot)
    form = ParkingE2Form(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkinge2_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkinge2')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotE2=Parking_E2.objects.get(
                parkinge2_spot=parkinge2_spot,
                parkinge2_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletee2, 'form': form})


def deletee3(request, parkinge3_spot):
    delete_spot = Parking_E3.objects.get(pk=parkinge3_spot)
    form = ParkingE3Form(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkinge3_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkinge3')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotE3=Parking_E3.objects.get(
                parkinge3_spot=parkinge3_spot,
                parkinge3_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletee3, 'form': form})


def deletee4(request, parkinge4_spot):
    delete_spot = Parking_E4.objects.get(pk=parkinge4_spot)
    form = ParkingE4Form(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkinge4_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkinge4')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotE4=Parking_E4.objects.get(
                parkinge4_spot=parkinge4_spot,
                parkinge4_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletee4, 'form': form})


def deletef(request, parkingf_spot):
    delete_spot = Parking_F.objects.get(pk=parkingf_spot)
    form = ParkingFForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingf_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingf')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotF=Parking_F.objects.get(
                parkingf_spot=parkingf_spot,
                parkingf_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletef, 'form': form})


def deleteg(request, parkingg_spot):
    delete_spot = Parking_G.objects.get(pk=parkingg_spot)
    form = ParkingGForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingg_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingg')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotG=Parking_G.objects.get(
                parkingg_spot=parkingg_spot,
                parkingg_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deleteg, 'form': form})


def deleteh(request, parkingh_spot):
    delete_spot = Parking_H.objects.get(pk=parkingh_spot)
    form = ParkingHForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingh_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingh')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotH=Parking_H.objects.get(
                parkingh_spot=parkingh_spot,
                parkingh_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deleteh, 'form': form})


def deletei(request, parkingi_spot):
    delete_spot = Parking_I.objects.get(pk=parkingi_spot)
    form = ParkingIForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingi_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingi')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotI=Parking_I.objects.get(
                parkingi_spot=parkingi_spot,
                parkingi_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletei, 'form': form})


def deletej(request, parkingj_spot):
    delete_spot = Parking_J.objects.get(pk=parkingj_spot)
    form = ParkingJForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingj_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingj')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotJ=Parking_J.objects.get(
                parkingj_spot=parkingj_spot,
                parkingj_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletej, 'form': form})


def deletek(request, parkingk_spot):
    delete_spot = Parking_K.objects.get(pk=parkingk_spot)
    form = ParkingKForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingk_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingk')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotK=Parking_K.objects.get(
                parkingk_spot=parkingk_spot,
                parkingk_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletek, 'form': form})


def deletel(request, parkingl_spot):
    delete_spot = Parking_L.objects.get(pk=parkingl_spot)
    form = ParkingLForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingl_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingl')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotL=Parking_L.objects.get(
                parkingl_spot=parkingl_spot,
                parkingl_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletel, 'form': form})


def deletem(request, parkingm_spot):
    delete_spot = Parking_M.objects.get(pk=parkingm_spot)
    form = ParkingMForm(request.POST or None, instance=delete_spot)
    if form.is_valid():
        data = form.cleaned_data.get("parkingm_status")
        if data is False:
            messages.error(request, "You are already parked here.  Please click 'Leave my spot' and select 'Cancel' "
                                    "when submitting your form.")
            return redirect('parkingm')
        else:
            form.save()
            log_update = log.objects.get(username=request.user, parking_spotM=Parking_M.objects.get(
                parkingm_spot=parkingm_spot,
                parkingm_status=True), currently_parked_here=True)
            log_update.currently_parked_here = False
            log_update.time_left = datetime.now()
            log_update.save()
            messages.success(request, "Parking spot updated successfully!")
            return redirect('map')

    return render(request, "delete.html", {'deleted': deletem, 'form': form})
