from django import forms


class WeightLossAnalysisForm(forms.Form):
    gender = forms.ChoiceField(label='Gender',
                               choices=[('woman', 'Woman'),
                                        ('man', 'Man')])
    current_weight = forms.ChoiceField(label='Current Weight span',
                                       choices=[('< 60 kg', '< 60 kg'),
                                                ('60-70 kg', '60-70 kg'),
                                                ('70-80 kg', '70-80 kg'),
                                                ('80-90 kg', '80-90 kg'),
                                                ('90-100 kg', '90-100 kg'),
                                                ('100-110 kg', '100-110 kg'),
                                                ('110-120 kg', '110-120 kg'),
                                                ('+120 kg', '+120 kg')]
                                       )
    expected_weight_loss = forms.ChoiceField(label='Expected weight loss?',
                                             choices=[('1-3 kg', '1-3 kg'),
                                                      ('3-6 kg', '3-6 kg'),
                                                      ('6-9 kg', '6-9 kg'),
                                                      ('9-12 kg', '9-12 kg'),
                                                      ('12-15 kg', '12-15 kg'),
                                                      ('+15 kg', '+15 kg')]
                                             )
    current_age = forms.ChoiceField(label='Current age span?',
                                    choices=[('< 20', '< 20'),
                                             ('20-30', '20-30'),
                                             ('30-40', '30-40'),
                                             ('40-50', '40-50'),
                                             ('50-60', '50-60'),
                                             ('60 +', '60 +')]
                                    )
    training_level = forms.ChoiceField(label='Your current training level?',
                                       choices=[('lev_1', 'Starting Out'),
                                                ('lev_2',
                                                 'Firm Tummy and Thighs'),
                                                ('lev_3',
                                                 'Fast results'),
                                                ('lev_4', 'Want a challenge'),
                                                ('lev_5',
                                                 'Pregnant or delivered \
                                                 within 3 years')]
                                       )
