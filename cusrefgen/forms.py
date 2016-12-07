from django import forms
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import RefGen


class DateInput(forms.DateInput):
  input_type = 'date'


class RefGenForm(forms.ModelForm):

  def __init__(self, *args, **kwargs):
    super(RefGenForm, self).__init__(*args, **kwargs)
    self.helper = FormHelper()
    self.helper.form_id = 'cusrefform'
    self.helper.form_method = 'post'

    self.helper.add_input(Submit('submit', 'Generate Reference Code', css_class='btn-danger'))

  class Meta:
    model = RefGen
    fields = ['letter_date', 'dispatch_date',
              'to_whom', 'letter_subject', 'org_units']
    labels = {
        'letter_date': _('Date of Letter'),
        'dispatch_date': _('Date to Dispatch'),
        'to_whom': _('To Whom'),
        'letter_subject': _('Subject'),
        'org_units': _('Organisational Unit'),
    }
    widgets = {
        'dispatch_date': DateInput(),
        'letter_date': DateInput(),
    }
