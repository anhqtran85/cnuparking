from django.test import SimpleTestCase
from django.urls import reverse, resolve
from main.views import home,leave,user_login,user,parkinga,parkingb,parkingc1,parkingc2,parkingd,parkinge1,parkinge2,parkinge3,parkinge4,parkingf,parkingg,parkingh,parkingi,parkingj,parkingk,parkingl,parkingm
from main.views import update, updateb,updatec1,updatec2,updated,updatee1,updatee2,updatee3,updatee4,updatef,updateg,updateh,updatei,updatej,updatek,updatel,updatem
from main.views import deletea,deleteb,deletec1,deletec2,deleted,deletee1,deletee2,deletee3,deletee4,deletef,deleteg,deleteh,deletei,deletej,deletek,deletel,deletem


class TestUrls(SimpleTestCase):

	def test_home_page(self):
		url = reverse('home')
		self.assertEqual(resolve(url).func, home)

	def test_login_page(self):
		url = reverse('login')
		self.assertEqual(resolve(url).func, user_login)

	def test_user_page(self):
		url = reverse('user')
		self.assertEqual(resolve(url).func, user)

	def test_leave_page(self):
		url = reverse('leave')
		self.assertEqual(resolve(url).func, leave)

	def test_parkinga_page(self):
		url = reverse('parkinga')
		self.assertEqual(resolve(url).func, parkinga)

	def test_parkingb_page(self):
		url = reverse('parkingb')
		self.assertEqual(resolve(url).func, parkingb)

	def test_parkingc1_page(self):
		url = reverse('parkingc1')
		self.assertEqual(resolve(url).func, parkingc1)

	def test_parkingc2_page(self):
		url = reverse('parkingc2')
		self.assertEqual(resolve(url).func, parkingc2)

	def test_parkingd_page(self):
		url = reverse('parkingd')
		self.assertEqual(resolve(url).func, parkingd)

	def test_parkinge1_page(self):
		url = reverse('parkinge1')
		self.assertEqual(resolve(url).func, parkinge1)

	def test_parkinge2_page(self):
		url = reverse('parkinge2')
		self.assertEqual(resolve(url).func, parkinge2)

	def test_parkinge3_page(self):
		url = reverse('parkinge3')
		self.assertEqual(resolve(url).func, parkinge3)

	def test_parkinge4_page(self):
		url = reverse('parkinge4')
		self.assertEqual(resolve(url).func, parkinge4)

	def test_parkingf_page(self):
		url = reverse('parkingf')
		self.assertEqual(resolve(url).func, parkingf)

	def test_parkingg_page(self):
		url = reverse('parkingg')
		self.assertEqual(resolve(url).func, parkingg)

	def test_parkingh_page(self):
		url = reverse('parkingh')
		self.assertEqual(resolve(url).func, parkingh)

	def test_parkingi_page(self):
		url = reverse('parkingi')
		self.assertEqual(resolve(url).func, parkingi)

	def test_parkingj_page(self):
		url = reverse('parkingj')
		self.assertEqual(resolve(url).func, parkingj)

	def test_parkingk_page(self):
		url = reverse('parkingk')
		self.assertEqual(resolve(url).func, parkingk)

	def test_parkingl_page(self):
		url = reverse('parkingl')
		self.assertEqual(resolve(url).func, parkingl)

	def test_parkingm_page(self):
		url = reverse('parkingm')
		self.assertEqual(resolve(url).func, parkingm)

	def test_update_page(self):
		url = reverse('update', args=['parking_spot'])
		self.assertEqual(resolve(url).func, update)

	def test_updateb_page(self):
		url = reverse('updateb', args=['parkingb_spot'])
		self.assertEqual(resolve(url).func, updateb)

	def test_updatec1_page(self):
		url = reverse('updatec1', args=['parkingc1_spot'])
		self.assertEqual(resolve(url).func, updatec1)

	def test_updatec2_page(self):
		url = reverse('updatec2', args=['parkingc2_spot'])
		self.assertEqual(resolve(url).func, updatec2)

	def test_updated_page(self):
		url = reverse('updated', args=['parkingd_spot'])
		self.assertEqual(resolve(url).func, updated)

	def test_updatee1_page(self):
		url = reverse('updatee1', args=['parkinge1_spot'])
		self.assertEqual(resolve(url).func, updatee1)

	def test_updatee2_page(self):
		url = reverse('updatee2', args=['parkinge2_spot'])
		self.assertEqual(resolve(url).func, updatee2)

	def test_updatee3_page(self):
		url = reverse('updatee3', args=['parkinge3_spot'])
		self.assertEqual(resolve(url).func, updatee3)

	def test_updatee4_page(self):
		url = reverse('updatee4', args=['parkinge4_spot'])
		self.assertEqual(resolve(url).func, updatee4)

	def test_updatef_page(self):
		url = reverse('updatef', args=['parkingf_spot'])
		self.assertEqual(resolve(url).func, updatef)

	def test_updateg_page(self):
		url = reverse('updateg', args=['parkingg_spot'])
		self.assertEqual(resolve(url).func, updateg)

	def test_updateh_page(self):
		url = reverse('updateh', args=['parkingh_spot'])
		self.assertEqual(resolve(url).func, updateh)

	def test_updatei_page(self):
		url = reverse('updatei', args=['parkingi_spot'])
		self.assertEqual(resolve(url).func, updatei)

	def test_updatej_page(self):
		url = reverse('updatej', args=['parkingj_spot'])
		self.assertEqual(resolve(url).func, updatej)

	def test_updatek_page(self):
		url = reverse('updatek', args=['parkingk_spot'])
		self.assertEqual(resolve(url).func, updatek)

	def test_updatel_page(self):
		url = reverse('updatel', args=['parkingl_spot'])
		self.assertEqual(resolve(url).func, updatel)

	def test_updatem_page(self):
		url = reverse('updatem', args=['parkingm_spot'])
		self.assertEqual(resolve(url).func, updatem)

	def test_deletea_page(self):
		url = reverse('delete', args=['parking_spot'])
		self.assertEqual(resolve(url).func, deletea)

	def test_deleteb_page(self):
		url = reverse('deleteb', args=['parkingb_spot'])
		self.assertEqual(resolve(url).func, deleteb)

	def test_deletec1_page(self):
		url = reverse('deletec1', args=['parkingc1_spot'])
		self.assertEqual(resolve(url).func, deletec1)

	def test_deletec2_page(self):
		url = reverse('deletec2', args=['parkingc2_spot'])
		self.assertEqual(resolve(url).func, deletec2)

	def test_deleted_page(self):
		url = reverse('deleted', args=['parkingd_spot'])
		self.assertEqual(resolve(url).func, deleted)

	def test_deletee1_page(self):
		url = reverse('deletee1', args=['parkinge1_spot'])
		self.assertEqual(resolve(url).func, deletee1)

	def test_deletee2_page(self):
		url = reverse('deletee2', args=['parkinge2_spot'])
		self.assertEqual(resolve(url).func, deletee2)

	def test_deletee3_page(self):
		url = reverse('deletee3', args=['parkinge3_spot'])
		self.assertEqual(resolve(url).func, deletee3)

	def test_deletee4_page(self):
		url = reverse('deletee4', args=['parkinge4_spot'])
		self.assertEqual(resolve(url).func, deletee4)

	def test_deletef_page(self):
		url = reverse('deletef', args=['parkingf_spot'])
		self.assertEqual(resolve(url).func, deletef)

	def test_deleteg_page(self):
		url = reverse('deleteg', args=['parkingg_spot'])
		self.assertEqual(resolve(url).func, deleteg)

	def test_deleteg_page(self):
		url = reverse('deleteg', args=['parkingg_spot'])
		self.assertEqual(resolve(url).func, deleteg)

	def test_deleteh_page(self):
		url = reverse('deleteh', args=['parkingh_spot'])
		self.assertEqual(resolve(url).func, deleteh)

	def test_deletei_page(self):
		url = reverse('deletei', args=['parkingi_spot'])
		self.assertEqual(resolve(url).func, deletei)

	def test_deletej_page(self):
		url = reverse('deletej', args=['parkingj_spot'])
		self.assertEqual(resolve(url).func, deletej)

	def test_deletel_page(self):
		url = reverse('deletel', args=['parkingl_spot'])
		self.assertEqual(resolve(url).func, deletel)

	def test_deletem_page(self):
		url = reverse('deletem', args=['parkingm_spot'])
		self.assertEqual(resolve(url).func, deletem)





