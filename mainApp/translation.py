from modeltranslation.translator import register, TranslationOptions
from mainApp.models import Option


@register(Option)
class OptionTranslationOptions(TranslationOptions):
    fields = ('name', 'link')

