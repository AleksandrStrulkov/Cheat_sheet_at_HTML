from django.urls import path
from .apps import LayoutConfig
from .views import start1, home, color_bg, color_text, space_1, space_2, space_3, aligment_1, aligment_2, border_1, \
	border_2, border_color, border_radius, border_radius_1, start, start_1, table, table_1, color_text_bg

app_name = LayoutConfig.name


urlpatterns = [
		path('', home, name='home'),
		path('start1/', start1, name='start1'),
		path('color_bg/', color_bg, name='color_bg'),
		path('color_text/', color_text, name='color_text'),
		path('color_text_bg/', color_text_bg, name='color_text_bg'),
		path('space_1/', space_1, name='space_1'),
		path('space_2/', space_2, name='space_2'),
		path('space_3/', space_3, name='space_3'),
		path('aligment_1/', aligment_1, name='aligment_1'),
		path('aligment_2/', aligment_2, name='aligment_2'),
		path('border_1/', border_1, name='border_1'),
		path('border_2/', border_2, name='border_2'),
		path('border_color/', border_color, name='border_color'),
		path('border_radius/', border_radius, name='border_radius'),
		path('border_radius_1/', border_radius_1, name='border_radius_1'),
		path('start/', start, name='start'),
		path('start_1/', start_1, name='start_1'),
		path('table/', table, name='table'),
		path('table_1/', table_1, name='table_1'),
]
