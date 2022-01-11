from django.contrib.auth.models import User
from django.db import models
from django.utils.timezone import now


class Parking_A(models.Model):
    parking_spot = models.CharField("Parking spot", max_length=20, null=False, primary_key=True,
                                    unique=True)
    parking_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parking_spot


class Parking_B(models.Model):
    parkingb_spot = models.CharField("Parkingb spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingb_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingb_spot


class Parking_C1(models.Model):
    parkingc1_spot = models.CharField("Parkingc1 spot", max_length=20, null=False, primary_key=True,
                                      unique=True)
    parkingc1_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingc1_spot


class Parking_C2(models.Model):
    parkingc2_spot = models.CharField("Parkingc2 spot", max_length=20, null=False, primary_key=True,
                                      unique=True)
    parkingc2_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingc2_spot


class Parking_D(models.Model):
    parkingd_spot = models.CharField("Parkingd spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingd_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingd_spot


class Parking_E1(models.Model):
    parkinge1_spot = models.CharField("Parkinge1 spot", max_length=20, null=False, primary_key=True,
                                      unique=True)
    parkinge1_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkinge1_spot


class Parking_E2(models.Model):
    parkinge2_spot = models.CharField("Parkinge2 spot", max_length=20, null=False, primary_key=True,
                                      unique=True)
    parkinge2_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkinge2_spot


class Parking_E3(models.Model):
    parkinge3_spot = models.CharField("Parkinge3 spot", max_length=20, null=False, primary_key=True,
                                      unique=True)
    parkinge3_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkinge3_spot


class Parking_E4(models.Model):
    parkinge4_spot = models.CharField("Parkinge4 spot", max_length=20, null=False, primary_key=True,
                                      unique=True)
    parkinge4_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkinge4_spot


class Parking_F(models.Model):
    parkingf_spot = models.CharField("Parkingf spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingf_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingf_spot


class Parking_G(models.Model):
    parkingg_spot = models.CharField("Parkingg spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingg_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingg_spot


class Parking_H(models.Model):
    parkingh_spot = models.CharField("Parkingh spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingh_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingh_spot


class Parking_I(models.Model):
    parkingi_spot = models.CharField("Parkingi spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingi_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingi_spot


class Parking_J(models.Model):
    parkingj_spot = models.CharField("Parkingj spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingj_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingj_spot


class Parking_K(models.Model):
    parkingk_spot = models.CharField("Parkingk spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingk_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingk_spot


class Parking_L(models.Model):
    parkingl_spot = models.CharField("Parkingl spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingl_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingl_spot


class Parking_M(models.Model):
    parkingm_spot = models.CharField("Parkingm spot", max_length=20, null=False, primary_key=True,
                                     unique=True)
    parkingm_status = models.BooleanField(null=True)

    def __str__(self):
        return self.parkingm_spot


class log(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.ForeignKey(User, related_name="parking_spotA_log", on_delete=models.CASCADE)
    time_parked = models.DateTimeField(default=now)

    parking_spot = models.ForeignKey(Parking_A, related_name="parking_spotA_log", on_delete=models.CASCADE, null=True,
                                     default=None)
    parking_spotB = models.ForeignKey(Parking_B, related_name="parking_spotB_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotC1 = models.ForeignKey(Parking_C1, related_name="parking_spotC1_log", on_delete=models.CASCADE,
                                       null=True,
                                       default=None)
    parking_spotC2 = models.ForeignKey(Parking_C2, related_name="parking_spotC2_log", on_delete=models.CASCADE,
                                       null=True,
                                       default=None)
    parking_spotD = models.ForeignKey(Parking_D, related_name="parking_spotD_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotE1 = models.ForeignKey(Parking_E1, related_name="parking_spotE1_log", on_delete=models.CASCADE,
                                       null=True,
                                       default=None)
    parking_spotE2 = models.ForeignKey(Parking_E2, related_name="parking_spotE2_log", on_delete=models.CASCADE,
                                       null=True,
                                       default=None)
    parking_spotE3 = models.ForeignKey(Parking_E3, related_name="parking_spotE3_log", on_delete=models.CASCADE,
                                       null=True,
                                       default=None)
    parking_spotE4 = models.ForeignKey(Parking_E4, related_name="parking_spotE4_log", on_delete=models.CASCADE,
                                       null=True,
                                       default=None)
    parking_spotF = models.ForeignKey(Parking_F, related_name="parking_spotF_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotG = models.ForeignKey(Parking_G, related_name="parking_spotG_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotH = models.ForeignKey(Parking_H, related_name="parking_spotH_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotI = models.ForeignKey(Parking_I, related_name="parking_spotI_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotJ = models.ForeignKey(Parking_J, related_name="parking_spotJ_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotK = models.ForeignKey(Parking_K, related_name="parking_spotK_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotL = models.ForeignKey(Parking_L, related_name="parking_spotL_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    parking_spotM = models.ForeignKey(Parking_M, related_name="parking_spotM_log", on_delete=models.CASCADE, null=True,
                                      default=None)
    currently_parked_here = models.BooleanField(null=True, default=True)
    time_left = models.DateTimeField(unique=True, null=True)

    def __str__(self):
        return str(self.username)
