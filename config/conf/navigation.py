from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

PAGES = [
    {
        "seperator": False,
        "items": [
            {
                "title": _("Bosh sahifa"),
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
                "title": _("Foydalanuvchilar"),
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
             {
                "title": _("Mahsulotlar"),
                "icon": "shopping_bag",
                "link": reverse_lazy("admin:api_productmodel_changelist"),
            },
            {
                "title": _("Kategoriyalar"),
                "icon": "category",
                "link": reverse_lazy("admin:api_categorymodel_changelist"),
            },
        ],
    },
    {
        "title": _("Buyurtmalar"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Buyurtma egasi"),
                "icon": "package",
                "link": reverse_lazy("admin:api_ordermodel_changelist"),
            },
             {
                "title": _("Buyurtmadagi mahsulotlar"),
                "icon": "box",
                "link": reverse_lazy("admin:api_orderitemmodel_changelist"),
            },
        ],
    },
    {
        "title": _("Malumotlar"),
        "separator": True,  # Top border
        "items": [
            {
                "title": _("Xabarlar"),
                "icon": "message",
                "link": reverse_lazy("admin:api_messagesmodel_changelist"),
            },
             {
                "title": _("Aloqa Malumotlari"),
                "icon": "phone",
                "link": reverse_lazy("admin:api_contactmodel_changelist"),
            },
        ],
    },
]
