from django import forms

class PHQ9Form(forms.Form):
    CHOICES = [(0, ''), (1, ''),
               (2, ''), (3, '')]

    phq_1 = forms.ChoiceField(
        label='Kurang berminat atau bergairah dalam melakukan apapun',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    phq_2 = forms.ChoiceField(
        label='Merasa murung, sedih, atau putus asa',
        choices=CHOICES, 
        widget=forms.RadioSelect(attrs={'class':''}))

    phq_3 = forms.ChoiceField(
        label='Sulit tidur/mudah terbangun, atau terlalu banyak tidur',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_4 = forms.ChoiceField(
        label='Merasa lelah atau kurang bertenaga',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_5 = forms.ChoiceField(
        label='Kurang nafsu makan atau terlalu banyak makan',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_6 = forms.ChoiceField(
        label='Kurang percaya diri — atau merasa bahwa Anda adalah orang yang gagal atau telah mengecewakan diri sendiri atau keluarga',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_7 = forms.ChoiceField(
        label='Sulit berkonsentrasi pada sesuatu, misalnya membaca koran atau menonton televisi',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
    
    phq_8 = forms.ChoiceField(
        label='Bergerak atau berbicara sangat lambat sehingga orang lain memperhatikannya. Atau sebaliknya; merasa resah atau gelisah sehingga Anda lebih sering bergerak dari biasanya',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))

    phq_9 = forms.ChoiceField(
        label='Merasa lebih baik mati atau ingin melukai diri sendiri dengan cara apapun',
        choices=CHOICES,
        widget=forms.RadioSelect(attrs={'class': ''}))
