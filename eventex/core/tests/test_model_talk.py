from django.test import TestCase
from eventex.core.managers import StartQuerySet
from eventex.core.models import Talk, Speaker, Course


class TalkeModelTest(TestCase):
    def setUp(self):
        self.talke = Talk.objects.create(
            title='Título da Palestra',
        )
    def test_create(self):
        self.assertTrue(Talk.objects.exists())

    def test_has_speakers(self):
        """Talk han many Speakers and vice-versa"""
        self.talke.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            website='http://henriquebastos.net'
        )
        self.assertEqual(1,self.talke.speakers.count())

    def test_description_blank(self):
        field = Talk._meta.get_field('description')
        self.assertTrue(field.blank)

    def test_speakers_black(self):
        field = Talk._meta.get_field('speakers')
        self.assertTrue(field.blank)

    def test_start_black(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.blank)

    def test_start_null(self):
        field = Talk._meta.get_field('start')
        self.assertTrue(field.null)

    def test_str(self):
        self.assertEqual('Título da Palestra',str(self.talke))

class TalkManagerTest(TestCase):
    def setUp(self):
        speaker = Speaker.objects.create(name='Luiz Olimpio', slug='luiz-olimpio',
                                         photo='http://hbn.link/arnaldinho-pic')
        talk_morning = Talk.objects.create(title='titulo da palestra', start='11:59')
        talk_morning.speakers.add(speaker)

        talk_afternoon = Talk.objects.create(title='titulo da palestra', start='12:01')
        talk_afternoon.speakers.add(speaker)

    def test_manager(self):
        self.assertIsInstance(Talk.objects, StartQuerySet)

    def test_start_morning(self):
        qs = Talk.objects.morning()
        expectd = ['11:59:00']
        self.assertQuerysetEqual(qs, expectd, lambda o: str(o.start))

    def test_start_afternoon(self):
        qs = Talk.objects.afternoon()
        expectd = ['12:01:00']
        self.assertQuerysetEqual(qs, expectd, lambda o: str(o.start))

class CourseModelTest(TestCase):
    def setUp(self):
        self.course = Course.objects.create(title='Titulo do Curso',start='09:00',description='Descricao do Curso',slots=20)
        self.speaker = self.course.speakers.create(
            name='Henrique Bastos',
            slug='henrique-bastos',
            photo='henrique-bastos'
        )


    def test_model_course(self):
        self.assertTrue(Course.objects.all().exists())

    def test_relacion_course(self):
        self.assertEqual(1,self.course.speakers.all().count())

    def test_str(self):
        self.assertEqual('Titulo do Curso',str(self.course))

    def test_manage(self):
        self.assertIsInstance(Course.objects,StartQuerySet)
