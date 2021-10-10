def get_rating(id, model):
	ratings = model.objects.get(id=id).ratings.all()
	quantity = model.objects.get(id=id).ratings.count()
	total = 0

	for rate in ratings:
		total += rate.rating

	if total == 0:
		return total

	total = round(total / quantity, 1)
	return total
