from multiselectfield import MultiSelectField
from django.db import models

# Reference: https://docs.djangoproject.com/en/3.2/ref/models/fields/

# Set choices for dropdowns
# Reference: https://stackoverflow.com/questions/31130706/dropdown-in-django-model
ANXIETY_RATE = [(0, '0'),
                (1, '1'),
                (2, '2'),
                (3, '3'),
                (4, '4'),
                (5, '5'),
                (6, '6'),
                (7, '7'),
                (8, '8'),
                (9, '9'),
                (10, '10')]
# Reference: https://stackoverflow.com/a/27442810/8487665
FEELINGS = [('antusias', 'Antusias'),
            ('gembira', 'Gembira'),
            ('takjub', 'Takjub'),
            ('semangat', 'Semangat'),
            ('bangga', 'Bangga'),
            ('cinta', 'Penuh Cinta'),
            ('santai', 'Santai'),
            ('tenang', 'Tenang'),
            ('puas', 'Puas'),
            ('lega', 'Lega'),
            ('marah', 'Marah'),
            ('takut', 'Takut'),
            ('stres', 'Stres'),
            ('waspada', 'Waspada'),
            ('kewalahan', 'Kewalahan'),
            ('kesal', 'Kesal'),
            ('malu', 'Malu'),
            ('cemas', 'Cemas'),
            ('lesu', 'Lesu'),
            ('sedih', 'Sedih'),
            ('duka', 'Duka'),
            ('bosan', 'Bosan'),
            ('kesepian', 'Kesepian'),
            ('bingung', 'Bingung')]

FACTORS = [('keluarga', 'Keluarga'),
           ('pekerjaan', 'Pekerjaan'),
           ('teman', 'Teman'),
           ('percintaan', 'Percintaan'),
           ('kesehatan', 'Kesehatan'),
           ('pendidikan', 'Pendidikan'),
           ('tidur', 'Tidur'),
           ('perjalanan', 'Perjalanan'),
           ('bersantai', 'Bersantai'),
           ('makanan', 'Makanan'),
           ('olahraga', 'Olahraga'),
           ('seni', 'Seni'),
           ('hobi', 'Hobi'),
           ('cuaca', 'Cuaca'),
           ('belanja', 'Belanja'),
           ('hiburan', 'Hiburan'),
           ('keuangan', 'Keuangan'),
           ('ibadah', 'Ibadah'),
           ('refleksi_diri', 'Refleksi Diri')]

class Journal(models.Model):
    date = models.DateTimeField(auto_now=True)
    feeling = MultiSelectField(choices=FEELINGS)
    anxiety_rate = models.IntegerField(default=0,choices=ANXIETY_RATE)
    summary = models.TextField()
    factor = MultiSelectField(choices=FACTORS, null=True)
