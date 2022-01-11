from main.models import Parking_A, Parking_B, Parking_C1, Parking_C2, Parking_D, Parking_E1, Parking_E2, Parking_E3, \
    Parking_E4, Parking_F, Parking_G, Parking_H, Parking_I, Parking_J, Parking_K, Parking_L, Parking_M
from django.test import TestCase


class TestModel(TestCase):

    def test_parkinga_true(self):
        parkinga = Parking_A(parking_status=True)
        parkinga.save()
        self.assertEqual(parkinga.parking_status, True)

    def test_parkinga_false(self):
        parkinga = Parking_A(parking_status=False)
        parkinga.save()
        self.assertEqual(parkinga.parking_status, False)

    def test_parkinga_none(self):
        parkinga = Parking_A(parking_status=None)
        parkinga.save()
        self.assertEqual(parkinga.parking_status, None)

    def test_parkingb_false(self):
        parkingb = Parking_B(parkingb_status=False)
        parkingb.save()
        self.assertEqual(parkingb.parkingb_status, False)

    def test_parkingb_true(self):
        parkingb = Parking_B(parkingb_status=True)
        parkingb.save()
        self.assertEqual(parkingb.parkingb_status, True)

    def test_parkingb_none(self):
        parkingb = Parking_B(parkingb_status=None)
        parkingb.save()
        self.assertEqual(parkingb.parkingb_status, None)

    def test_parkingc1_true(self):
        parkingc1 = Parking_C1(parkingc1_status=True)
        parkingc1.save()
        self.assertEqual(parkingc1.parkingc1_status, True)

    def test_parkingc1_false(self):
        parkingc1 = Parking_C1(parkingc1_status=False)
        parkingc1.save()
        self.assertEqual(parkingc1.parkingc1_status, False)

    def test_parkingc1_none(self):
        parkingc1 = Parking_C1(parkingc1_status=None)
        parkingc1.save()
        self.assertEqual(parkingc1.parkingc1_status, None)

    def test_parkingc2_false(self):
        parkingc2 = Parking_C2(parkingc2_status=False)
        parkingc2.save()
        self.assertEqual(parkingc2.parkingc2_status, False)

    def test_parkingc2_true(self):
        parkingc2 = Parking_C2(parkingc2_status=True)
        parkingc2.save()
        self.assertEqual(parkingc2.parkingc2_status, True)

    def test_parkingc2_none(self):
        parkingc2 = Parking_C2(parkingc2_status=None)
        parkingc2.save()
        self.assertEqual(parkingc2.parkingc2_status, None)

    def test_parkingd_true(self):
        parkingd = Parking_D(parkingd_status=True)
        parkingd.save()
        self.assertEqual(parkingd.parkingd_status, True)

    def test_parkingd_false(self):
        parkingd = Parking_D(parkingd_status=False)
        parkingd.save()
        self.assertEqual(parkingd.parkingd_status, False)

    def test_parkingd_none(self):
        parkingd = Parking_D(parkingd_status=None)
        parkingd.save()
        self.assertEqual(parkingd.parkingd_status, None)

    def test_parkinge1_false(self):
        parkinge1 = Parking_E1(parkinge1_status=False)
        parkinge1.save()
        self.assertEqual(parkinge1.parkinge1_status, False)

    def test_parkinge1_true(self):
        parkinge1 = Parking_E1(parkinge1_status=True)
        parkinge1.save()
        self.assertEqual(parkinge1.parkinge1_status, True)

    def test_parkinge1_none(self):
        parkinge1 = Parking_E1(parkinge1_status=None)
        parkinge1.save()
        self.assertEqual(parkinge1.parkinge1_status, None)

    def test_parkinge2_false(self):
        parkinge2 = Parking_E2(parkinge2_status=False)
        parkinge2.save()
        self.assertEqual(parkinge2.parkinge2_status, False)

    def test_parkinge2_true(self):
        parkinge2 = Parking_E2(parkinge2_status=True)
        parkinge2.save()
        self.assertEqual(parkinge2.parkinge2_status, True)

    def test_parkinge2_none(self):
        parkinge2 = Parking_E2(parkinge2_status=None)
        parkinge2.save()
        self.assertEqual(parkinge2.parkinge2_status, None)

    def test_parkinge3_true(self):
        parkinge3 = Parking_E3(parkinge3_status=True)
        parkinge3.save()
        self.assertEqual(parkinge3.parkinge3_status, True)

    def test_parkinge3_false(self):
        parkinge3 = Parking_E3(parkinge3_status=False)
        parkinge3.save()
        self.assertEqual(parkinge3.parkinge3_status, False)

    def test_parkinge3_none(self):
        parkinge3 = Parking_E3(parkinge3_status=None)
        parkinge3.save()
        self.assertEqual(parkinge3.parkinge3_status, None)

    def test_parkinge4_true(self):
        parkinge4 = Parking_E4(parkinge4_status=True)
        parkinge4.save()
        self.assertEqual(parkinge4.parkinge4_status, True)

    def test_parkinge4_false(self):
        parkinge4 = Parking_E4(parkinge4_status=False)
        parkinge4.save()
        self.assertEqual(parkinge4.parkinge4_status, False)

    def test_parkinge4_none(self):
        parkinge4 = Parking_E4(parkinge4_status=None)
        parkinge4.save()
        self.assertEqual(parkinge4.parkinge4_status, None)

    def test_parkingf_none(self):
        parkingf = Parking_F(parkingf_status=None)
        parkingf.save()
        self.assertEqual(parkingf.parkingf_status, None)

    def test_parkingf_true(self):
        parkingf = Parking_F(parkingf_status=True)
        parkingf.save()
        self.assertEqual(parkingf.parkingf_status, True)

    def test_parkingf_false(self):
        parkingf = Parking_F(parkingf_status=False)
        parkingf.save()
        self.assertEqual(parkingf.parkingf_status, False)

    def test_parkingg_true(self):
        parkingg = Parking_G(parkingg_status=True)
        parkingg.save()
        self.assertEqual(parkingg.parkingg_status, True)

    def test_parkingg_false(self):
        parkingg = Parking_G(parkingg_status=False)
        parkingg.save()
        self.assertEqual(parkingg.parkingg_status, False)

    def test_parkingg_none(self):
        parkingg = Parking_G(parkingg_status=None)
        parkingg.save()
        self.assertEqual(parkingg.parkingg_status, None)

    def test_parkingh_true(self):
        parkingh = Parking_H(parkingh_status=True)
        parkingh.save()
        self.assertEqual(parkingh.parkingh_status, True)

    def test_parkingh_false(self):
        parkingh = Parking_H(parkingh_status=False)
        parkingh.save()
        self.assertEqual(parkingh.parkingh_status, False)

    def test_parkingh_none(self):
        parkingh = Parking_H(parkingh_status=None)
        parkingh.save()
        self.assertEqual(parkingh.parkingh_status, None)

    def test_parkingi_true(self):
        parkingi = Parking_I(parkingi_status=True)
        parkingi.save()
        self.assertEqual(parkingi.parkingi_status, True)

    def test_parkingi_false(self):
        parkingi = Parking_I(parkingi_status=False)
        parkingi.save()
        self.assertEqual(parkingi.parkingi_status, False)

    def test_parkingi_none(self):
        parkingi = Parking_I(parkingi_status=None)
        parkingi.save()
        self.assertEqual(parkingi.parkingi_status, None)

    def test_parkingj_true(self):
        parkingj = Parking_J(parkingj_status=True)
        parkingj.save()
        self.assertEqual(parkingj.parkingj_status, True)

    def test_parkingj_false(self):
        parkingj = Parking_J(parkingj_status=False)
        parkingj.save()
        self.assertEqual(parkingj.parkingj_status, False)

    def test_parkingj_none(self):
        parkingj = Parking_J(parkingj_status=None)
        parkingj.save()
        self.assertEqual(parkingj.parkingj_status, None)

    def test_parkingk_true(self):
        parkingk = Parking_K(parkingk_status=True)
        parkingk.save()
        self.assertEqual(parkingk.parkingk_status, True)

    def test_parkingk_false(self):
        parkingk = Parking_K(parkingk_status=False)
        parkingk.save()
        self.assertEqual(parkingk.parkingk_status, False)

    def test_parkingk_none(self):
        parkingk = Parking_K(parkingk_status=None)
        parkingk.save()
        self.assertEqual(parkingk.parkingk_status, None)

    def test_parkingl_true(self):
        parkingl = Parking_L(parkingl_status=True)
        parkingl.save()
        self.assertEqual(parkingl.parkingl_status, True)

    def test_parkingl_false(self):
        parkingl = Parking_L(parkingl_status=False)
        parkingl.save()
        self.assertEqual(parkingl.parkingl_status, False)

    def test_parkingl_none(self):
        parkingl = Parking_L(parkingl_status=None)
        parkingl.save()
        self.assertEqual(parkingl.parkingl_status, None)

    def test_parkingm_true(self):
        parkingm = Parking_M(parkingm_status=True)
        parkingm.save()
        self.assertEqual(parkingm.parkingm_status, True)

    def test_parkingm_false(self):
        parkingm = Parking_M(parkingm_status=False)
        parkingm.save()
        self.assertEqual(parkingm.parkingm_status, False)

    def test_parkingm_none(self):
        parkingm = Parking_M(parkingm_status=None)
        parkingm.save()
        self.assertEqual(parkingm.parkingm_status, None)
