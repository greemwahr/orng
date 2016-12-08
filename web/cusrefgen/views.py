from django.shortcuts import render  # Default import from django framework
from django.urls import reverse
from django.http  import HttpResponseRedirect
from .forms import RefGenForm
from .models import *

def display(request):
  dispRefInstance = RefNo.objects.all().last()
  return render(request, 'cusrefgen/refno.html', {'dispRefInstance': dispRefInstance.generated_ref_no})


def form(request):
  form = RefGenForm(request.POST or None)
  temp = RefGen.objects.all().last()
  refnoInstance = RefNo()

  if temp is None:
    if form.is_valid():
      form.save()
  else:
    if form.is_valid():
      referenceInstance = form.save()
      referenceInstance.ref_number = temp.ref_number + 1
      referenceInstance.save()

      month = str(referenceInstance.letter_date)
      year = str(referenceInstance.letter_date)
      refnoInstance.generated_ref_no = 'ipNX/{}/{}/{}/{}'.format(temp.org_units, temp.ref_number, month[5:7], year[2:4])
      refnoInstance.save()

      return HttpResponseRedirect(reverse('cusrefgen:display'))

  return render(request, 'cusrefgen/index.html', {'form': form})
