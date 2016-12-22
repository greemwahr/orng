from __future__ import unicode_literals  # Default import from django framework

from django.db import models
from django.utils import timezone
from django.utils.encoding import python_2_unicode_compatible
#from django import forms
#from django.forms import widgets

DEPARTMENTAL_NAMES = (
    (None, 'Select from dropdown'),
    ('AD/DI', 'Admin Services'),
    ('FIN/BO', 'Chief Finance Office'),
    ('CS/SEB', 'Corporate Services'),
    ('CC/KE', 'Customer Care'),
    ('DCO/SO', 'Data Centre Operations'),
    ('FIN/TO', 'Finance'),
    ('GMD/EA', 'Group Managing Director'),
    ('HR/TA', 'Human Capital Management'),
    ('IST/AS', 'Information Systems & Technology'),
    ('ME/TA', 'Media & Entertainment'),
    ('MKT/KS', 'Marketing'),
    ('NIU/GJ', 'Network Infrastructure Unit'),
    ('NSD/SO', 'Network Services Division'),
    ('PD/KJ', 'Product Development'),
    ('PM/TO', 'Program Management'),
    ('RD/SO', 'Research & Development'),
    ('SCM/RO', 'Supply Chain Management'),
)


class RefNo(models.Model):
  generated_ref_no = models.CharField(max_length=60)

  def reference_number(self):
    return self.generated_ref_no
  reference_number.short_description = 'Reference number'


@python_2_unicode_compatible  # only if you need to support Python 2
class RefGen(models.Model):
  letter_date = models.DateField(default=timezone.now)
  dispatch_date = models.DateField(null=True, blank=False)
  to_whom = models.CharField(max_length=50)
  letter_subject = models.CharField(max_length=100)
  org_units = models.CharField(max_length=50, choices=DEPARTMENTAL_NAMES)
  ref_number = models.IntegerField(default=0000)

  def __str__(self):
    return self.letter_subject

  def date_on_letter(self):
    return self.letter_date
  date_on_letter.short_description = 'Date on letter'

  def date_of_dispatch(self):
    return self.dispatch_date
  date_of_dispatch.short_description = 'Date of dispatch'

  def whom_to(self):
    return self.to_whom
  whom_to.short_description = 'To whom'

  def subject(self):
    return self.letter_subject
  subject.short_description = 'Subject'
