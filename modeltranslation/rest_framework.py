from rest_framework import serializers
from modeltranslation.fields import TranslationField


class TranslatableModelSerializer(serializers.ModelSerializer):

    def get_default_field_names(self, declared_fields, model_info):
        return (
            [model_info.pk.name] +
            list(declared_fields) +
            [name for name, f in model_info.fields.items()
             if not isinstance(f, TranslationField)] +
            [name for name, rel in model_info.forward_relations.items()
             if not isinstance(rel.model_field, TranslationField)]
        )
