from django.shortcuts import render
def index(request):
    r = None
    if request.method == 'POST':

        num1 = request.POST.get('case_1')
        num2 = request.POST.get('case_2')
        operation = request.POST.get('operation')

        #les opérations
        if num1 is not None and num2 is not None :
            num1 = int(num1)
            num2 = int(num2)
            if operation == 'plus' :
                r = num1 + num2
            elif operation == 'moins':
                r = num1 - num2
            elif operation == 'multiplication' :
                r = num1 * num2
            elif operation == 'division' :
                if num2 != 0:
                    r = num1 / num2
                else:
                    r = 'Erreur!! Division par 0'

    return render(request, 'index.html', {'r': r})

# Create your views here.
