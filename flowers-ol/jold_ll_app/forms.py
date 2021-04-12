from django import forms
from django.utils.translation import gettext_lazy as _
from django.core.exceptions import *
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Div, HTML


class ConsentForm(forms.Form):
    understood = forms.BooleanField(label=_("En cochant cette case, vous reconnaissez avoir lu et compris les informations fournies sur l'étude."), required=True)
    agreed = forms.BooleanField(label=_("En cochant cette case, vous donnez votre consentement éclairé à participer à l'étude."), required=True)
    request_reminder = forms.BooleanField(label=_('En cochant cette case, vous acceptez de tecevoir un rappel 1 jour avant la prochaine session (optionel).'), required=False)
    email = forms.EmailField(label=_('À quelle adresse souhaitez-vous recevoir le(s) rappel(s) ? Indiquez votre adresse électronique ci-dessous (optionel)'), required=False)
    fields = ['understood', 'agreed']

    def __init__(self, *args, **kwargs):
        super(ConsentForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.add_input(Submit('submit', _('Soumettre le consentement éclairé')))
    
    def clean(self):
        cleaned_data = super(ConsentForm, self).clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('password_confirm')

        if cleaned_data['request_reminder'] and not cleaned_data['email']:
            self.add_error('email', _('Veuillez fournir une adresse électronique si vous souhaitez recevoir un rappel de la future session 1 jour à l\'avance.'))

        if not cleaned_data['request_reminder'] and cleaned_data['email']:
            self.add_error('request_reminder', _('Si vous souhaitez recevoir un rappel par courriel au sujet de la prochaine session, veuillez cocher cette case. Si vous ne souhaitez pas recevoir de tels rappels, décochez cette case et supprimez votre courriel ci-dessous.'))

        return cleaned_data