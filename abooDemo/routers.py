from ebooks.viewsets import AbooViewSets
from rest_framework import routers

router = routers.DefaultRouter()
router.register('ebooks', AbooViewSets)
