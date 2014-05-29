__author__ = 'mwalker'

from django import forms

from .models import HomeMultiArticle, HomeFullArticle


class HomeMultiArticleAdminForm(forms.ModelForm):
    left_url_1 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://'
    )
    left_url_2 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    left_url_3 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    left_url_4 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    left_url_5 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    left_url_6 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )

    right_url_1 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://'
    )
    right_url_2 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    right_url_3 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    right_url_4 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    right_url_5 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    right_url_6 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )

    class Meta:
        model = HomeMultiArticle

        fieldsets = (
            ('Left slide 1', {
                'fields': (
                    'left_title_1',
                    'left_text_1',
                    'left_url_1'
                ),
            }),
            ('Left slide 2', {
                'fields': (
                    'left_title_2',
                    'left_text_2',
                    'left_url_2'
                )
            }),
            ('Left slide 3', {
                'fields': (
                    'left_title_3',
                    'left_text_3',
                    'left_url_3'
                )
            }),
        )

    def clean(self):
        cleaned_data = super(HomeMultiArticleAdminForm, self).clean()
        required_fields = []

        for i in range(2, 7):
            l_fields = [
                'left_title_{}'.format(i),
                'left_text_{}'.format(i),
                'left_url_{}'.format(i)
            ]
            r_fields = [
                'right_title_{}'.format(i),
                'right_text_{}'.format(i),
                'right_url_{}'.format(i)
            ]
            for field in l_fields:
                if cleaned_data.get(field) != '':
                    required_fields.append(l_fields)

            for field in r_fields:
                if cleaned_data.get(field) != '':
                    required_fields.append(r_fields)

        for field in required_fields:
            if cleaned_data.get(field) == '':
                msg = 'This field is required.'.format(field=field)
                self._errors[field] = self.error_class([msg])

        return cleaned_data


class HomeFullArticleAdminForm(forms.ModelForm):
    url_1 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://'
    )
    url_2 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    url_3 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    url_4 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    url_5 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )
    url_6 = forms.URLField(
        max_length=200,
        help_text="Input full URL e.g. http://www.google.com",
        initial='http://',
    )

    class Meta:
        model = HomeFullArticle

    def clean(self):
        cleaned_data = super(HomeFullArticleAdminForm, self).clean()
        required_fields = []

        for i in range(2, 7):
            fields = [
                'title_{}'.format(i),
                'text_{}'.format(i),
                'url_{}'.format(i),
            ]

            for field in fields:
                if cleaned_data.get(field) != '':
                    required_fields.append(fields)

            if cleaned_data.get("image_{}".format(i)) != u'[]':
                required_fields.append('title_{}'.format(i))
                required_fields.append('text_{}'.format(i))
                required_fields.append('url_{}'.format(i))

        for field in required_fields:
            if cleaned_data.get(field) == '':
                msg = 'This field is required.'.format(field=field)
                self._errors[field] = self.error_class([msg])

        return cleaned_data