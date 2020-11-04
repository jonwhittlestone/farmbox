import base64
from django.db import models
from django.apps import apps
from django.forms.models import model_to_dict


def calculate_model_signature(model_spec):
    """
    Calculates a unique fingerprint/signature for a given model.

    Only Order field is supported currently.
    """

    to_concatenate = []
    pre_base64: str = ""
    order_model_attrs = [
        "f_number",
        "fulfillment_method",
        "notes",
        "repeated_order_original",
        "products.name",
    ]

    mdl = apps.get_model("order", model_spec.get("model"))
    obj = model_to_dict(mdl.objects.get(id=model_spec.get("id")))
    for prop in order_model_attrs:
        if "." in prop:
            # the attribute has a child model relation
            # which should get its own string comprising relation
            continue
        else:
            to_concatenate.append(str(obj.get(prop)))

    pre_base64 = "".join(to_concatenate)
    post_base64 = base64.b64encode(pre_base64.encode("utf-8")).decode("utf-8")

    return post_base64
