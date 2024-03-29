from django.contrib import admin
from mainApp.models import Option
from modeltranslation.admin import TranslationAdmin
from mptt.admin import MPTTModelAdmin


@admin.register(Option)
class OptionAdmin(TranslationAdmin, MPTTModelAdmin):
    class Media:
        js = (
            "https://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js",
            "https://ajax.googleapis.com/ajax/libs/jqueryui/1.10.2/jquery-ui.min.js",
            "modeltranslation/js/tabbed_translation_fields.js",
        )
        css = {
            "screen": ("modeltranslation/css/tabbed_translation_fields.css",),
        }
