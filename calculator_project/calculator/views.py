from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request, 'calculator/home.html')


def calculate(request):
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        operation = request.POST.get('operation')
        print(num1, type(num1))
        try:

            num1 = float(num1)
            num2 = float(num2)

            if operation == 'addition':
                result = num1 + num2
            elif operation == 'subtraction':
                result = num1 - num2
            elif operation == 'multiplication':
                result = num1 * num2
            elif operation == 'division':
                if num2 == 0:
                    raise ZeroDivisionError("Cannot divide by zero.")
                result = num1 / num2
            else:
                result = None

            return render(request, 'calculator/home.html', {'result': result})

        except ValueError:
            error = "Invalid input. Please enter numeric values."
        except ZeroDivisionError as zde:
            error = str(zde)

        return render(request, 'calculator/home.html', {'error': error})

    return render(request, 'calculator/home.html', {'result': None})


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
