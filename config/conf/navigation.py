from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Home page"),
                "icon": "home",
                "link": reverse_lazy("admin:index"),
            }
        ],
    },
    {
        "title": _("Foydalanuvchilar"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Users"),
                "icon": "person",
                "link": reverse_lazy("admin:accounts_user_changelist"),
            },
        ],
    },
    {
        "title": _("Mahsulotlar"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Bannerlar"),
                "icon": "shopping_cart",
                "link": reverse_lazy("admin:api_bannermodel_changelist"),
            },
        ],
    },
]
