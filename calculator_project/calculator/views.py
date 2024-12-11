from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'calculator/home.html')



def calculate(request):
    if request.method == 'POST':
        numbers = request.POST.getlist('numbers')  # Get all number inputs
        operation = request.POST.get('operation')

        try:
            # Filter and convert inputs to floats
            numbers = [float(num) for num in numbers if num.strip()]

            if len(numbers) < 2:
                raise ValueError("At least two numbers are required.")

            result = numbers[0]

            # Sequential calculation
            for num in numbers[1:]:
                if operation == 'addition':
                    result += num
                elif operation == 'subtraction':
                    result -= num
                elif operation == 'multiplication':
                    result *= num
                elif operation == 'division':
                    if num == 0:
                        raise ZeroDivisionError("Cannot divide by zero.")
                    
                    result /= num
                else:
                    raise ValueError("Invalid operation selected.")

            return render(request, 'calculator/home.html', {'result': result})

        except ValueError as ve:
            error = str(ve)
        except ZeroDivisionError as zde:
            error = str(zde)

        return render(request, 'calculator/home.html', {'error': error})

    return render(request, 'calculator/home.html', {'result': None})
