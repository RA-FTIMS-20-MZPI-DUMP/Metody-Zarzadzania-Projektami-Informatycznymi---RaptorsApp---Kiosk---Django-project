from django import forms

from kiosk.models import KioskModel, TargetPosition, TargetParking


class KioskSelect(forms.ModelForm):
    class Meta:
        model = KioskModel
        fields = [
            'kiosk',
        ]


class KioskTargetPosition(forms.ModelForm):
    class Meta:
        model = TargetPosition
        fields = [
            'pozycja',
        ]


class KioskTargetParking(forms.ModelForm):
    class Meta:
        model = TargetParking
        fields = [
            'pozycja',
        ]