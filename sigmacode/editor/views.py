from django.shortcuts import render
from django.views import View
from django import forms
import subprocess

# Create a form for the code input
class CodeForm(forms.Form):
    code = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'Write your code here...'}), label='Enter your code')

class CodeEditorView(View):
    # Handle GET request for the code editor
    def get(self, request):
        form = CodeForm()
        return render(request, 'editor/editor.html', {'form': form})

    # Handle POST request to execute the code
    def post(self, request):
        form = CodeForm(request.POST)
        output = ''
        message_class = ''  # Initialize message class for styling

        if form.is_valid():
            code = form.cleaned_data['code']
            language = request.POST.get('language', 'python')  # Get selected language from hidden input
            try:
                if language == "python":
                    # Execute Python code
                    result = subprocess.run(['python3', '-c', code], capture_output=True, text=True, check=True)
                    output = result.stdout
                    message_class = "success"  
                elif language == "javascript":
                    # Execute JavaScript (example for future implementation, cannot be run server-side)
                    output = "JavaScript cannot be executed server-side. Please run in a browser."
                elif language == "htmlmixed":
                    output = "HTML cannot be executed directly. Please view in a browser."
                elif language == "css":
                    output = "CSS code cannot be executed directly. Please apply in a browser."
                else:
                    output = "Unsupported language"
            except subprocess.CalledProcessError as e:
                output = e.stderr
                message_class = "error"  # Assign class for error output

        return render(request, 'editor/editor.html', {
            'form': form,
            'output': output,
            'message_class': message_class
        })