from django.shortcuts import render
from .models import UserEntries

# Create your views here.
def index(request):
    return render(request, 'index.html')

def result(request):
    if request.method == 'POST':
        user_text = request.POST['text'] 
        total_chars = len(user_text)
        total_words = len(user_text.split(" "))
        vowels = ['a', 'e', 'i', 'o', 'u']
        vowel_count = consonant_count = 0
        for char in user_text:
            if char.isalpha():
                if char in vowels or char.upper() in vowels:
                    vowel_count += 1
                else: 
                    consonant_count += 1
        new_entry = UserEntries(text=user_text, words=total_words, chars=total_chars, vowels=vowel_count, consonants=consonant_count)
        new_entry.save()
        context = {
            'text' : user_text,
            'character': total_chars,
            'words': total_words,
            'vowels': vowel_count,
            'consonants': consonant_count,
        }
        return render(request, 'result.html', context)
    else: 
        return render(request, 'result.html')