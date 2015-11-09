from .models import Condition

def condition_all(request):
	condition = Condition.objects.all()
	return {'condition': condition}