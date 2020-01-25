from hostel.models import Student


class Statistics():

	qwe = Student.objects.filter(name__icontains= 'мужское').count()
		
	def free_man():
		return Student.objects.filter(name__icontains= 'мужское').count()

	def free_women():
		return Student.objects.filter(name__icontains= 'женское').count()
	
	def free():
		return Student.objects.filter(name__icontains= 'занято').count()
	
	
	def places():

		hostel_palces = {'number_of_residents': 0,'num_of_free_place': 0,'man': 0, 'women': 0, 'busy': 0, 'blank': 0}		

		for key in hostel_palces.keys():
			places = Student.objects.filter(name__icontains= key).count()
			hostel_palces[key] = places
			hostel_palces['num_of_free_place'] += places

		hostel_palces['number_of_residents'] = Student.objects.all().count() - hostel_palces['num_of_free_place']
		return hostel_palces



	def citizenship_sort():
		
		hostel_palces = {'Количество проживающих': 0,'Количество свободных мест': 0,'мужское': 0, 'женское': 0, 'занято': 0, 'пустоe': 0}		
		country = {'РФ': 0, 'Казахстан': 0}
		students = Student.objects.all()

		for student in students:

			if student.name in hostel_palces.keys():
				continue

			else:
				if student.citizenship in country.keys():
					country[student.citizenship] += 1
				else :
					country[student.citizenship] = 1

	
	def stat_group():
		students = Student.objects.all()
		group_dict = {}

		for student in students:
			if student.group in group_dict.keys():
				group_dict[student.group] += 1
			else:
				group_dict[student.group] = 1
		print(group_dict.keys())


	def medical_certificates():
		
		print(free_man())
		flurog_cert = Student.objects.all().count() - Student.objects.filter(fluorography__icontains='+').count()
		pedicul_cert = Student.objects.all().count() - Student.objects.filter(pediculosis__icontains='+').count()
		print('|||||||||||||||||||||||||||||||||')
		print(flurog_cert )
		print()
		print('|||||||||||||||||||||||||||||||||')
		