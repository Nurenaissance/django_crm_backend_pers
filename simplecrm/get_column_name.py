from django.http import JsonResponse
import pandas as pd
import os

from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def get_excel_columns(request):
    if request.method == 'POST' and request.FILES.get('file'):
        excel_file = request.FILES['file']
        num = int(request.POST.get('startrow'))
        try:
            file_extension = os.path.splitext(excel_file.name)[1].lower()
            encoding = 'latin1' if file_extension in ('.xlsx', '.xls', '.csv') else None

            if file_extension == '.xlsx':
                df = pd.read_excel(excel_file, engine='openpyxl', header=num)
            elif file_extension == '.xls':
                df = pd.read_excel(excel_file, header=num)
            elif file_extension == '.csv':
                df = pd.read_csv(excel_file, header=num)
            else:
                return JsonResponse({'error': 'Unsupported file format'}, status=400)

            column_names = df.columns.tolist()

            return JsonResponse({"columns": column_names})
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'No file uploaded'}, status=400)
