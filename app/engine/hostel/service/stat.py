from hostel.models import Student


class Statistics():

	all_count = Student.objects.all().count()

	male_places = Student.objects.filter(place_status__icontains= 'мужское').count()
	female_places = Student.objects.filter(place_status__icontains= 'женское').count()
	empty_place = Student.objects.filter(place_status__icontains= 'пусто').count()
	save_places = Student.objects.filter(place_status__icontains= 'занято').count()

	num_of_residents = all_count - male_places - female_places -  empty_place - save_places
	all_free_places = male_places + female_places + empty_place + save_places

	flurog_cert = num_of_residents - Student.objects.filter(fluorography__contains='+').count()
	pedicul_cert = num_of_residents - Student.objects.filter(pediculosis__contains='+').count()


	def citizenship_sort():
		country_dict = {'РФ':0, 'Казахстан':0}
		students = Student.objects.all()

		for student in students:
			if student.name == '':
				continue

			else:
				if student.citizenship in country_dict.keys():
					country_dict[student.citizenship] += 1
				else :
					country_dict[student.citizenship] = 1
		return country_dict


	def faculty_sort():
		faculty_dict = {}
		students = Student.objects.all()

		for student in students:
			if student.name == '':
				continue

			else:
				if student.faculty in faculty_dict.keys():
					faculty_dict[student.faculty] += 1
				else :
					faculty_dict[student.faculty] = 1
		return faculty_dict



	def stat_group():
		students = Student.objects.all()
		group_dict = {}

		for student in students:
			if student.group in group_dict.keys():
				group_dict[student.group] += 1
			else:
				group_dict[student.group] = 1
		print(group_dict.keys())


