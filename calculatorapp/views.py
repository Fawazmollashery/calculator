from django.shortcuts import render

def calculator_view(request):
    if request.method == 'POST':
        number1 = float(request.POST.get('number1', 0))
        number2 = float(request.POST.get('number2', 0))
        operation = request.POST.get('operation')

        result = None
        if operation == 'add':
            result = number1 + number2
        elif operation == 'subtract':
            result = number1 - number2
        elif operation == 'multiply':
            result = number1 * number2
        elif operation == 'divide':
            result = number1 / number2 if number2 != 0 else 'Error (division by zero)'

        context = {'result': result}
        return render(request, 'index.html', context)
    return render(request, 'index.html')
