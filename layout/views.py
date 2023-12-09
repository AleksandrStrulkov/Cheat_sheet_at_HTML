from django.shortcuts import render


def home(request):
	return render(request, 'layout/home.html')


def start1(request):
	return render(request, 'layout/1_start1.html')


def color_bg(request):
	return render(request, 'layout/2_color_bg.html')


def color_text(request):
	return render(request, 'layout/3_color_text.html')


def color_text_bg(request):
	return render(request, 'layout/4_color_text_bg.html')


def space_1(request):
	return render(request, 'layout/5_space_1.html')


def space_2(request):
	return render(request, 'layout/6_space_2.html')


def space_3(request):
	return render(request, 'layout/7_space_3.html')


def aligment_1(request):
	return render(request, 'layout/8_aligment_1.html')


def aligment_2(request):
	return render(request, 'layout/9_aligment_2.html')


def border_1(request):
	return render(request, 'layout/10_border_1.html')


def border_2(request):
	return render(request, 'layout/11_border_2.html')


def border_color(request):
	return render(request, 'layout/12_border_color.html')


def border_radius(request):
	return render(request, 'layout/13_border_radius.html')


def border_radius_1(request):
	return render(request, 'layout/13_border_radius.html')


def start(request):
	return render(request, 'layout/15_start.html')


def start_1(request):
	return render(request, 'layout/16_start_1.html')


def table(request):
	return render(request, 'layout/17_table.html')


def table_1(request):
	return render(request, 'layout/18_table_1.html')

