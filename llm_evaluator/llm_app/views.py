from django.shortcuts import render
import random
import json
import os
import csv
from django.http import JsonResponse,HttpResponseNotFound
from django.conf import settings

def evaluation_options(request):
    return render(request, 'evaluation_options.html')

def get_random_line(request):
    file_path = os.path.join(settings.BASE_DIR, 'datasets/cnndm/model_annotations.aligned.jsonl')

    try:
        random_line_number = random.randint(1, 1600)

        with open(file_path, 'r') as file:
            for i, line in enumerate(file, start=1):
                if i == random_line_number:
                    line_data = json.loads(line.strip())
                    return JsonResponse({'line': line_data})
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Line not found'}, status=404)

def get_random_nli(request):
    file_path = os.path.join(settings.BASE_DIR, 'datasets/snli/snli_1.0/snli_1.0_test_batch.jsonl')

    try:
        random_line_number = random.randint(1, 500)

        with open(file_path, 'r') as file:
            for i, line in enumerate(file, start=1):
                if i == random_line_number:
                    line_data = json.loads(line.strip())
                    return JsonResponse({'line': line_data})
    except FileNotFoundError:
        return JsonResponse({'error': 'File not found'}, status=404)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

    return JsonResponse({'error': 'Line not found'}, status=404)

def get_file_content(request, storyId, type):
    if (type == "dm"):
        file_path = os.path.join(settings.BASE_DIR, 'datasets', 'cnndm', 'dailymail', 'stories', str(storyId)+".story")
    else:
        file_path = os.path.join(settings.BASE_DIR, 'datasets', 'cnndm', 'cnn', 'stories', str(storyId)+".story")

    if not os.path.isfile(file_path):
        return HttpResponseNotFound(f"File {storyId} not found.")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
        return JsonResponse({'file_content': content})
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
    
def get_pairwise(request):
    try:
        file_path = os.path.join(settings.BASE_DIR, 'datasets/arena/random_200.csv')
        with open(file_path, 'r', encoding='utf-8') as csv_file:  # Specify UTF-8 encoding
            reader = csv.DictReader(csv_file)

            # Convert the reader to a list to access rows
            rows = list(reader)

            # Ensure there is at least one row
            if not rows:
                return JsonResponse({"error": "The file is empty or has no rows."}, status=400)

            # Randomly select a row index
            random_index = random.randint(0, len(rows) - 1)

            # Extract the randomly selected row as a dictionary
            selected_row = rows[random_index]
            return JsonResponse({'line': selected_row})

    except FileNotFoundError:
        return JsonResponse({"error": "File not found."}, status=404)
    except UnicodeDecodeError as e:
        return JsonResponse({"error": f"Encoding error: {str(e)}"}, status=500)